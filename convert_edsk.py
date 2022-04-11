#!/usr/bin/python3

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
