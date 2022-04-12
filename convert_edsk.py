#!/usr/bin/python3
"""Convert a short edsk to a full edsk.

The Tezos privatekey (secret key) is a Ed25519 seed (32 bytes) or a secret
exponent (64 bytes) derived from the seed. Both variants are used in wallets.
This script converts the Ed25519 seed variant in the secret exponent variant.

If the full version is given as input, the output will be the prvious given
full version.
"""
# pylint: disable=C0103

# Import Key from pytezos.crypto.key
from pytezos.crypto.key import Key

# Get user input.
key = input("Provide short edsk key: ")

# Create edsk object.
edsk = Key.from_encoded_key(key)

# Determine full secret key.
full_edsk = edsk.secret_key(ed25519_seed=False)

# Print full secret key to screen.
print("{0}{1}".format("Full secret key: ", full_edsk))
