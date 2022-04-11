#!/usr/bin/python3
"""Reveal key for public key hash (public key).

After performing the reveal key operation the public key hash (public key) can
be used in general.

This script is for demonstration purposes. Error messages are not catched at
the moment.
"""
# pylint: disable=C0103

# Import Python modules.
from pytezos import pytezos

# Set the Tezos network.
TEZOS_NETWORK = "mainnet"

# Get the secret key from the user input.
secretkey = input("Secret key (private key): ")

# Create a new pytezos instance using the Tezos mainnet.
pytezos = pytezos.using(shell=TEZOS_NETWORK, key=secretkey)

# Inject data for reveal key operation into the blockchain.
opg = pytezos.reveal().autofill().sign().inject()

# Print opg to screen.
print(opg)
