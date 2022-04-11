#!/usr/bin/python3
"""Create a public key from a 12 word mnemonic."""
# pylint: disable=C0103

# Remark:
# The created Tezos address is valid and can be used directly, e.g. a Tezos
# amount can be sent to this address. However, e.g. the amount contained cannot
# be delegated to a baker or can be used for a transaction. For this purpose it
# is necessary to obtain a reveal key.

# Import Python modules.
from pytezos.crypto.key import Key
from mnemonic import Mnemonic

# Set the variables.
STRENGTH = 128
LANGUAGE = 'english'

# Get the 12 word mnemonic.
mnemonic = Mnemonic(LANGUAGE).generate(STRENGTH)

# Print a 12 word mnemonic.
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
