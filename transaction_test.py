#!/usr/bin/python3
"""Perform a transaction test.

The script shows how a transaction will work between source and destination.

Exchange run_operation() by inject() for a real not simulated transaction in
the Mainnet.

Truncating the given Tezos amount can be controlled by ROUND_DOWN or ROUND_UP.

For demonstration purposes error messages are not catched.
"""
# pylint: disable=C0103
# pylint: disable=W0212
# pylint: disable=W0702
# pylint: disable=W0611

# Import the standard Python modules.
import json
import ast
import os
from decimal import Decimal, ROUND_DOWN, ROUND_UP

# Import the third party Python modules.
from pytezos import pytezos

# Set the Tezos network.
TEZOS_NETWORK = "mainnet"

# Get the secret key from the user input.
secretkey = str(input("Secret key (private key): "))

# Create a new pytezos instance using the Tezos mainnet.
pytezos = pytezos.using(shell=TEZOS_NETWORK, key=secretkey)

# Get the Tezos address of the destination.
destination = str(input("Destination (Tezos address): "))

# Get the Tezos address of the destination.
amount = str(input("Amount of Tezos to transfer: "))

# Try to create a floating point number.
try:
    amount = float(amount)
except:
    print("The given input is not a decimal number. Bye!")
    os._exit(1)

# Get numbers after the decimal point.
numbers = Decimal(amount).as_tuple().exponent

# Print a warning if numbers is larger than 6.
if numbers <= -6:
    print("The given amount will be truncated and rounded (up/down) to 6 numbers after the decimal point.")

# Finally get the amount for transaction.
#amount = Decimal(str(amount)).quantize(Decimal('0.000001'), rounding=ROUND_DOWN)
amount = Decimal(str(amount)).quantize(Decimal('0.000001'), rounding=ROUND_UP)

# Prepare the transaction operation group.
opg = pytezos.transaction(destination=destination, amount=Decimal(amount)).autofill().sign()

# Test the validity of the delegation.
opg_run_operation = opg.run_operation()

# Create json data from a dictionary.
json_data = str(opg_run_operation)

# Make sure that the data is of type json.
json_data = json.dumps(ast.literal_eval(json_data))

# Create a json object from the jason data.
json_obj = json.loads(json_data)

# Create a json format string. Indent is set to 4.
json_fmtstr = json.dumps(json_obj, indent=4)

# Print the result of run operation.
print("{0}{1}".format("\n", json_fmtstr))

