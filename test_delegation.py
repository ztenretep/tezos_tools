#!/usr/bin/python3
"""Perform a delegation test.

This script demonstrates how a delegation from a Tezos account to a baker will
work. One needs a secret key (private key) of the own Tezos account and the
bakers Tezos address. The output shows if the delegation is possible without
producing errors.

Exchange run_operation() by inject() for a real not simulated delegation in
the Mainnet.

Be careful. If account or delegate are empty, the account will be registered
as baker. An unregistration is not possible. A redelegation is also not
possible.

If there is no error and 'source' and 'delegate' in the printed json data are
different, then a real delegation would work.

For demonstration purposes errors are not catched yet.
"""
# pylint: disable=invalid-name

# Import the standard Python modules.
import json

# Import the third party Python modules.
from pytezos import pytezos

# Set the Tezos network.
TEZOS_NETWORK = "mainnet"

# Get the secret key from the user input.
secretkey = input("Secret key (private key): ")

# Get the baker Tezos address from the user input.
pkh_baker = str(input("Public key hash (public key) of baker: "))

# Create a new pytezos instance using the Tezos mainnet.
pytezos = pytezos.using(shell=TEZOS_NETWORK, key=secretkey)

# Prepare the delegation operation group.
opg = pytezos.delegation(delegate=pkh_baker).autofill().sign()

# Test the validity of the delegation.
opg_run_operation = opg.run_operation()

# Create a json format string. Indent is set to 4.
json_fmtstr = json.dumps(opg_run_operation, indent=4)

# Print the result of run operation.
print("{0}{1}".format("\n", json_fmtstr))
