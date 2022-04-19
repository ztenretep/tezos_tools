#!/bin/usr/python3
"""Create a simple Tezos paper wallet. """
# pylint: disable=C0103

# Import the Python modules.
import os
from fpdf import FPDF
import qrcode
from pytezos.crypto.key import Key
from mnemonic import Mnemonic

# Set the variables.
STRENGTH = 128
LANGUAGE = 'english'

# Get the 12 word mnemonic.
mnemonic = Mnemonic(LANGUAGE).generate(STRENGTH)

# Print the 12 word mnemonic.
print("{1}{0}{2}{0}".format("\n", "12 word mnemonic:", mnemonic))

# Set mn.
mn = "{0}".format(mnemonic)

# Create a secret key object.
sk = Key.from_mnemonic(mnemonic=mnemonic, email='', passphrase='')

# Determine the secret key.
edsk = sk.secret_key()
print("{1}{0}{2}{0}".format("\n", "Secret key (private key):", edsk))

# Determine the full secret key.
edsk_full = sk.secret_key(ed25519_seed=False)
print("{1}{0}{2}{0}".format("\n", "Full secret key (full private key):", edsk_full))

# Get the public key from the secret key object.
pk = sk.public_key()
print("{1}{0}{2}{0}".format("\n", "Public key (is not a public key):", pk))

# Get the public key hash from the secret key object.
pkh = sk.public_key_hash()
print("{1}{0}{2}".format("\n", "Public key hash (tezos address is public key):", pkh))

# Create an instance of FPDF.
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Create a new page.
pdf.add_page()

# Create content.
pdf.set_font(family="Helvetica", style="B", size=16)
pdf.cell(200, 10, txt="Tezos Paper Wallet", ln=1, align="L")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Mnemonic:", ln=1, align="L")
pdf.cell(200, 10, txt=mn, ln=1, align="L")

img = qrcode.make(mn)
type(img)
img.save("mn.png")
pdf.image("mn.png", x = None, y = None, w = 60, h = 60, type = '', link = '')
os.remove("mn.png")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Public key:", ln=1, align="L")
pdf.cell(200, 10, txt=pkh, ln=1, align="L")

img = qrcode.make(pkh)
type(img)
img.save("publickey.png")
pdf.image("publickey.png", x = None, y = None, w = 60, h = 60, type = '', link = '')
os.remove("publickey.png")

pdf.cell(200, 10, txt="Private Key:", ln=1, align="L")
pdf.set_font("Arial", size=8.5)
pdf.cell(200, 10, txt=edsk_full, ln=1, align="L")

img = qrcode.make(edsk_full)
type(img)
img.save("privatekey.png")
pdf.image("privatekey.png", x = None, y = None, w = 60, h = 60, type = '', link = '')
os.remove("privatekey.png")

# Write to PDF.
pdf.output(pkh + ".pdf")
