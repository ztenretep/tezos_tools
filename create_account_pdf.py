#!/bin/usr/python3
"""Create a simple Tezos paper wallet. """
# pylint: disable=C0103

# Import the standard Python modules.
import os
import sys

# Import the third party Python modules.
import qrcode
from fpdf import FPDF
from pytezos.crypto.key import Key
from mnemonic import Mnemonic

# Set the mnemonic variables.
STRENGTH = 128
LANGUAGE = 'english'

# ================
# Function reset()
# ================
def reset():
    """Reset terminal window."""
    # Write ANSI code to terminal.
    sys.stdout.write("\033c")
    # Write buffer to screen immediately.
    sys.stdout.flush()

# ====================
# Function create_qr()
# ====================
def create_qr(data, fn):
    """Function create_qr()."""
    img = qrcode.make(data)
    img.save(fn)
    PDF.image(fn, x=None, y=None, w=40, h=40, type='', link='')
    os.remove(fn)

# =======================
# Function account_data()
# =======================
def account_data():
    """Function account_data()."""
    # Get the 12 word mnemonic.
    mnemonic = Mnemonic(LANGUAGE).generate(STRENGTH)
    # Print the 12 word mnemonic to screen.
    print("{1}{0}{2}{0}".format("\n", "12 word mnemonic:", mnemonic))
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
    # Return account data.
    return mnemonic, edsk, edsk_full, pkh

# ====================
# Function write_pdf()
# ====================
def write_pdf(mnemonic, edsk, edsk_full, pkh):
    """Function write_pdf()."""
    # Create a new PDF page.
    PDF.add_page()
    # Set the font, style and size.
    PDF.set_font(family="Helvetica", style="B", size=16)
    # Write to PDF.
    PDF.cell(200, 10, txt="Tezos Paper Wallet", ln=1, align="L")
    # Set the font, style and size.
    PDF.set_font("Helvetica", size=12)
    # Write to PDF.
    PDF.cell(200, 10, txt="Mnemonic:", ln=1, align="L")
    PDF.cell(200, 10, txt=mnemonic, ln=1, align="L")
    # Create QR code.
    fn = "mnemonic.png"
    create_qr(mnemonic, fn)
    # Create the PDF content.
    PDF.set_font("Arial", size=12)
    # Write to PDF.
    PDF.cell(200, 10, txt="Public key:", ln=1, align="L")
    PDF.cell(200, 10, txt=pkh, ln=1, align="L")
    # Create QR code.
    fn = "pkh.png"
    create_qr(pkh, fn)
    # Write to PDF.
    PDF.cell(200, 10, txt="Private Key (short):", ln=1, align="L")
    # Set the font, style and size.
    PDF.set_font("Arial", size=12)
    # Write to PDF.
    PDF.cell(200, 10, txt=edsk, ln=1, align="L")
    # Create QR code.
    fn = "edsk.png"
    create_qr(edsk, fn)
    # Write to PDF.
    PDF.cell(200, 10, txt="Private Key (long):", ln=1, align="L")
    # Set the font, style and size.
    PDF.set_font("Arial", size=8.5)
    # Write to PDF.
    PDF.cell(200, 10, txt=edsk_full, ln=1, align="L")
    # Create QR code.
    fn = "edsk_full.png"
    create_qr(edsk_full, fn)
    # Write everything to PDF.
    PDF.output(pkh + ".pdf")

# #############
# Main function
# #############
def main():
    """Main function."""
    # Get account data.
    mnemonic, edsk, edsk_full, pkh = account_data()
    # Write PDF.
    write_pdf(mnemonic, edsk, edsk_full, pkh)

# Execute script as program or as module.
if __name__ == "__main__":
    # Reset screen.
    reset()
    # Create an instance of FPDF.
    PDF = FPDF(orientation='P', unit='mm', format='A4')
    # Call main function.
    main()
