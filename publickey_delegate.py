#!/usr/bin/python3
"""Request the delegate for a given public key hash

This script is able to retrieve the delegate for a given public key hash
(public key). If no delegate is found in the account data an exception is
raised.
"""
# pylint: disable=C0103
# pylint: disable=W0212
# pylint: disable=W0702

# Import the standard Python module.
import os

# Import the third party Python module.
from pytezos import pytezos

# Set the Tezos network.
TEZOS_NETWORK = "mainnet"

# Create a new pytezos instance using the Tezos mainnet.
pytezos = pytezos.using(shell=TEZOS_NETWORK)

# Get the public key hash from the user input.
publickeyhash = input("Public key hash (public key): ")

# Try to retrieve the delegate for a given public key hash.
try:
    # Request the balance from the Tezos mainnnet.
    delegate = pytezos.account(publickeyhash)['delegate']
except:
    print("{0}{1}".format("\n", "No delegate found in the account data! Bye!"))
    os._exit(1)

# Print the delegate to the screen.
print("{0}{1}{2}".format("\n", "Delegate: ", delegate))
