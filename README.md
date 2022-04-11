# tezos
Crypto Coin Tezos Tools

While using crypto coins I figured out, that a Tezos private key can be short or long. Importing a short private key from one wallet in another wallet failed. So I took a deeper look into this problem. The result is that I am now able to write different tools, which can be used together with Tezos. The first result was a snippet which converts a short Ed25519 seed (secret key, 32 bytes) to a secret exponent (secret key, 64 bytes). This solved the import problem.

Development will be done on different Linux distributions using Python3. For Tezos the Python module PyTezos does, what I am expected from. Snippets are in the pipeline for creating accounts, making transactions, requesting account and balance informations as well as delegation of a given account to a new baker. 

Small donations are welcome:\n
tz1SAXFTMxyer8MGuUya4aALDm6j3185ivJt 
