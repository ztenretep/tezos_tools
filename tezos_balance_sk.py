#!/usr/bin/python3
"""Request the Tezos balance from the blockchain for a given secret key.

In the Tezos methology, the public key (Tezos account address) can be determined
from a given secret key (private key). Using the secret key the balance of the
related Tezos account can be retrieved from the Tezos Mainnet.

The balance is stored in form of a string. This string has to be converted into
a decimal number to get the Tezos value. The Tezos subunit is 0.000001 Mutez.
This results in the underlying calculation rule.
"""
# pylint: disable=C0103

# Import Python modules.
from decimal import Decimal
from pytezos import pytezos

# Set the Tezos network.
TEZOS_NETWORK = "mainnet"

# Set the Tezos constants.
TEZOS_SYMBOL = "\uA729"

# Get the secret key from the user input.
secretkey = input("Secret key (private key): ")

# Create a new pytezos instance using the Tezos mainnet.
pytezos = pytezos.using(shell=TEZOS_NETWORK, key=secretkey)

# Request the balance from the Tezos mainnnet.
raw_str = pytezos.account()['balance']

# Create decimal value from balance string.
raw_dec = (Decimal(raw_str) / 10 ** 6).quantize(Decimal('0.000001'))

# Convert decimal to string.
balance = str(raw_dec)

# Print balance to screen.
print("{0}{1} {2}".format("\n", balance, TEZOS_SYMBOL))
