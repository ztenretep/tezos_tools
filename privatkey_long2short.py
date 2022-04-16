#!/usr/bin/python3
"""Convert a full edsk to a short edsk.

The Tezos privatekey (secret key) is a Ed25519 seed (32 bytes) or a secret
exponent (64 bytes) derived from the seed. Both variants are used in wallets.
This script converts the secret exponent variant in the Ed25519 seed variant.

If the short version is given as input, the output will be the previous given
short version.
"""
# pylint: disable=C0103

# Import Key from pytezos.crypto.key
from pytezos.crypto.key import Key

# Get user input.
key = input("Provide full edsk key: ")

# Create edsk object.
edsk = Key.from_encoded_key(key)

# Determine full secret key.
full_edsk = edsk.secret_key(ed25519_seed=True)

# Print full secret key to screen.
print("{0}{1}".format("Short secret key: ", full_edsk))
