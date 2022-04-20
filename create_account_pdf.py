#!/bin/usr/python3
"""Create Tezos implicit account data.

After creating the Tezos implicit account data, the created data is written
to a PDF file. This is similar to creating a simple Tezos paper wallet.
"""
# pylint: disable=useless-return
# pylint: disable=invalid-name
# pylint: disable=global-statement
# pylint: disable=unused-argument
# pylint: disable=deprecated-method

# Import the standard Python modules.
import os
import sys
import base64
import subprocess
from datetime import datetime

# Import the third party Python modules.
import qrcode
from fpdf import FPDF
from pytezos.crypto.key import Key
from mnemonic import Mnemonic

# Set image data.
img_logo = """
iVBORw0KGgoAAAANSUhEUgAAAC8AAABACAMAAAC9W94RAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6
JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAB71BMVEUAAAApevUsffgsffctffckgP8v
e/YsffcwgPcrffcrffosfPYtffcsfvYtfvYsffcsffYtffctffgrfvcsffcsffcsfvcsffcAgP8tfvcs
ffcrfvcsffcsffcndv8sffcsfvcsfvcsfPcsevQugPMsfPcrgPktfvgsffYtffYzgP8rfPcsffcsffcr
ffcsfvZAgP8rgPQsffctffcAAP8rffcsffctffcsfPgqffUtgPgre/YtfPgtffctgPkrgPQsfvctfPgq
ffkqffYsfPgrffcufvdVVf8sffctffYrfPYrgP8tePAsffcuffcsffYsffYsfPcsffcrffcsffcrffcr
ffYsffYsfvcsffcsffgrfvctffgsffgsfvcufPgtffctffgsfvYoefItffUsfPYsffcsffcsffcrffcu
gPYsfvcsffcrffgtfPYzZv8se/UsfvgtfPcrfvYsffgsffcsfPcue/YsgPkngPUrgPcugPkrffcrffcs
ffcrffYsffcsffctfPgsffcsfPckbf8sffcsffcsffgrffYsffcsfvgsffcufPcsfPgsffcrfvgxefMt
fPcsfPctffcsfvctfvcsffgsffcwgO8tffcsfPcpfPgre/csffcsffcrffcrfPgtfvksfff///9fPLdc
AAAAo3RSTlMAGe7mfg4b7CCHL9HIUVXadGBmQfL8XcACYd6C/sQNusWAQBcWfypJVjkKQt36tlcEGOda
Aby+1G0xIjZn5Sgww0orN0zCQwOXsVQGEZs9spV5uN/z2VjQmOqLX2ytlie3iZATM3Xt+P2ZHMf5ancF
NEugWaq5qDguGh4sXp/rdp2nRL/TB8bXrLCjRfshb6GIFaaieGNbbukQg6QlPOH3ZGtPgV0MCgAAAAFi
S0dEpFm+erkAAAAHdElNRQfkAhcOLjI/QbrUAAACg0lEQVRIx+2W6VcTMRTFBwu4FJBWKyNqsQouKAW0
WhALxSIqAm4gIiqibIoKLrgjyqKI+wauuOQftcnLlEnzMqTn+NH3oWd67y8zd5I3kzEMqLRFrFzpGYZW
ZRJei5foDVhqDVhmpDZAlzfcKfJZ//l/wGfnWLUc+NwctDxe7wrKryTa5VuVGs8GpMKTPNNY7bUqH7Q1
XqnS14K1zq81P2YBOOv9evMZQHElv8GH4ip+owvHFTwPL+MKPqDCcR7CYzjKF7qUOMZDeBzH+IADjvAs
vAqXeRZeiUs8C6/GJb6IduSmzVu2Fmvx22j47VQpCZaWLciX77A/KPk7Q868uSvp0dpd7sjT8OGKyj1V
e4PQziRS7cDX+Ei0lkfYl8cHZIp8FOQYPa7bXz9vHDjII5kCfwjUBnp8mP40NjXzlTgCVqnAHwXxWOK0
x8kJa/dsYVarMK0ngW/jsc1ThLRb3mnwOux8I5yEnGH//Gfjh+csrxOs80KgLv7Wu1B5sbunPX7Um5bw
wszqE3bz4jZxifqz571LINUJF7g8YMeveGzWVdCuiUswWBFO4ANDduc6iDekLqq+2dV0a/h2UZUo3wE+
qLtZ3eUX1eVj/I2Omve67ydLtdgCQD2gs+SOieJD4EeQL6dHzGkR230U+B6Z56tMHgvqExDHZH6c8xN2
MRSBi07K/FPOP0Omfwq53SnOP7eL06C9QPhcIketecmkcAjhX/Wzzn1tkzLcyruN1xtqvbUJ76LKyWcL
0EvN91Z7DnoifP+dVPTKGKRt/fDx08zsyGd+PwVflM01UyJ9afR9LXPoxqGsJPrb9wX698f0nAX/HJ4t
1Ppkr2/49bvjT6cQ5C867T6qHbazEwAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMC0wMi0yM1QxNDo0Njo1
MCswMDowMC1NwncAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjAtMDItMjNUMTQ6NDY6NTArMDA6MDBcEHrL
AAAAAElFTkSuQmCC"""

# Create png image.
fn_logo = "tezos_logo.png"
img_bytestr = img_logo.encode('utf-8')
png_recovered = base64.decodestring(img_bytestr)
with open(fn_logo, 'wb') as fo:
    fo.write(png_recovered)

# Set the mnemonic variables.
STRENGTH = 128
LANGUAGE = 'english'

# Other constants.
EMAIL = ''
PASSPHRASE = ''

# ================
# Function reset()
# ================
def reset():
    """Reset terminal window."""
    # Write ANSI code to terminal.
    sys.stdout.write("\033c")
    # Write buffer to screen immediately.
    sys.stdout.flush()

# =======================
# Function account_data()
# =======================
def account_data():
    """Function account_data()."""
    # Get the 12 word mnemonic.
    mnemonic = Mnemonic(LANGUAGE).generate(STRENGTH)
    # Create a secret key object.
    sk = Key.from_mnemonic(mnemonic=mnemonic, email=EMAIL, passphrase=PASSPHRASE)
    # Determine the secret key.
    edsk = sk.secret_key()
    # Determine the full secret key.
    edsk_full = sk.secret_key(ed25519_seed=False)
    # Get the public key from the secret key object.
    pk = sk.public_key()
    # Get the public key hash from the secret key object.
    pkh = sk.public_key_hash()
    # Return account data.
    return mnemonic, edsk, edsk_full, pk, pkh

# =============================
# Function print_account_data()
# =============================
def print_account_data(mnemonic, edsk, edsk_full, pk, pkh):
    """Function print_account_data()."""
    # Print the 12 word mnemonic to screen.
    print("{1}{0}{2}{0}".format("\n", "12 word mnemonic:", mnemonic))
    # Print edsk to screen.
    print("{1}{0}{2}{0}".format("\n", "Secret key (private key):", edsk))
    # Print full edsk to screen.
    print("{1}{0}{2}{0}".format("\n", "Full secret key (full private key):", edsk_full))
    # Print pk to screen.
    print("{1}{0}{2}{0}".format("\n", "Public key (is not a public key):", pk))
    # Print pkh to screen.
    print("{1}{0}{2}".format("\n", "Public key hash (tezos address is public key):", pkh))
    return None

# ====================
# Function create_qr()
# ====================
def print_qr(data, fn):
    """Function create_qr()."""
    img = qrcode.make(data)
    img.save(fn)
    PDF.image(fn, x=None, y=None, w=38, h=38, type='', link='')
    os.remove(fn)
    return None

# ======================
# Function print_sline()
# ======================
def print_sline(w, h, text, size):
    """Print single line."""
    PDF.set_font("Helvetica", size=size)
    PDF.cell(w, h, txt=text, align='L')
    PDF.ln(10)
    return None

# ======================
# Function print_mline()
# ======================
def print_mline(w, h, text, size):
    """Print multiple line."""
    PDF.set_font("Helvetica", size=size)
    PDF.multi_cell(w, h, txt=text, align='L')
    PDF.ln(0)
    return None

# ======
# Header
# ======
def header():
    """Header."""
    PDF.set_font(family="Helvetica", style="B", size=16)
    PDF.set_text_color(r=44, g=125, b=247)
    PDF.image("tezos_logo.png", x=10, y=12, w=5)
    PDF.cell(6)
    PDF.set_font(family="Helvetica", style="", size=16)
    PDF.cell(20, 10, txt="Tezos", align="L")
    PDF.cell(120)
    PDF.set_font(family="Helvetica", style="B", size=16)
    PDF.set_text_color(r=0, g=0, b=0)
    PDF.cell(30, 10, txt="Paper Wallet", align="R")
    PDF.ln(10)
    return None

# ======
# Footer
# ======
def footer():
    """Footer."""
    PDF.set_font("Helvetica", size=10)
    presentime = datetime.now()
    dt = presentime.strftime('%d.%m.%Y %H:%M')
    PDF.cell(80)
    PDF.cell(200, 10, txt=dt, align="L")
    return None

# ====================
# Function write_pdf()
# ====================
def write_pdf(mnemonic, edsk, edsk_full, pk, pkh):
    """Function write_pdf()."""
    global EMAIL, PASSPHRASE
    # Create a new PDF page.
    PDF.add_page()
    # Print header.
    header()
    # Write to PDF.
    print_mline(200, 10, "Mnemonic:\n" + mnemonic, 12)
    if EMAIL == '':
        EMAIL = "None"
    if PASSPHRASE == '':
        PASSPHRASE = "None"
    print_sline(200, 10, "Email: " + EMAIL + "  " + "Passphrase: " + PASSPHRASE, 12)
    # Create QR code.
    fn = "mnemonic.png"
    print_qr(mnemonic, fn)
    # Write to PDF.
    print_mline(200, 10, "Public key:\n" + pkh, 12)
    # Create QR code.
    fn = "pkh.png"
    print_qr(pkh, fn)
    # Write to PDF.
    print_mline(200, 10, "Private Key (short):\n" + edsk, 12)
    # Create QR code.
    fn = "edsk.png"
    print_qr(edsk, fn)
    # Write to PDF.
    print_mline(200, 10, "Private key (long):\n" + edsk_full, 8.5)
    # Create QR code.
    fn = "edsk_full.png"
    print_qr(edsk_full, fn)
    # Print footer.
    footer()
    # Write everything to PDF.
    PDF.output(pkh + ".pdf")
    # Run evince to show PDF.
    subprocess.call(["evince", pkh + ".pdf", "-s"])
    #subprocess.call(["evince", pkh + ".pdf" ])

# #############
# Main function
# #############
def main():
    """Main function."""
    # Get account data.
    mnemonic, edsk, edsk_full, pk, pkh = account_data()
    # Print account data.
    print_account_data(mnemonic, edsk, edsk_full, pk, pkh)
    # Write PDF.
    write_pdf(mnemonic, edsk, edsk_full, pk, pkh)

# Execute script as program or as module.
if __name__ == "__main__":
    # Reset screen.
    reset()
    # Create an instance of FPDF.
    PDF = FPDF(orientation='P', unit='mm', format='A4')
    # Call main function.
    main()
