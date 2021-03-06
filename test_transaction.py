#!/usr/bin/python3
"""Perform a transaction test.

The script shows how a transaction will work between source and destination.

Exchange run_operation() by inject() for a real not simulated transaction in
the Mainnet.

Truncating the given Tezos amount can be controlled by ROUND_DOWN or ROUND_UP.

For demonstration purposes error messages are not catched.
"""
# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=unused-import
# pylint: disable=bare-except
# pylint: disable=line-too-long

# Import the standard Python modules.
import json
import os
from decimal import Decimal, ROUND_DOWN, ROUND_UP

# Import the third party Python modules.
from pytezos import pytezos

# Set the Tezos network.
TEZOS_NETWORK = "mainnet"

# Get the secret key from the user input.
secretkey = input("Secret key (private key): ")

# Create a new pytezos instance using the Tezos mainnet.
pytezos = pytezos.using(shell=TEZOS_NETWORK, key=secretkey)

# Get the Tezos address of the destination.
destination = input("Destination (Tezos address): ")

# Get the Tezos address of the destination.
amount = input("Amount of Tezos to transfer: ")

# Try to create a floating point number.
try:
    amount = float(amount)
except:
    print("The given input is not a decimal number. Bye!")
    os._exit(1)

# Get numbers after the decimal point.
numbers = len(str(amount).split('.')[1])

# Print a warning if numbers is larger than 6.
if numbers > 6:
    print("The given amount will be truncated and rounded (up/down) to 6 numbers after the decimal point.")

# Finally get the amount for transaction.
#amount = Decimal(str(amount)).quantize(Decimal('0.000001'), rounding=ROUND_UP)
amount = Decimal(str(amount)).quantize(Decimal('0.000001'), rounding=ROUND_DOWN)

# Prepare the transaction operation group.
opg = pytezos.transaction(destination=destination, amount=Decimal(amount)).autofill().sign()

# Test the validity of the delegation.
opg_run_operation = opg.run_operation()

# Convert dictionary to string. Set indent to 4 for printing.
json_data = json.dumps(opg_run_operation, indent=4)

# Print the result of run operation.
print("{0}{1}".format("\n", json_data))
