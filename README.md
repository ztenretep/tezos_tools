# tezos
Snippets and tools for use with Tezos

While using crypto coins I figured out, that a Tezos private key can be short or long. Importing a short private key from one wallet in another wallet failed. So I took a deeper look into this problem. The result is that I am now able to write different tools, which can be used together with Tezos. The first result was a snippet which converts a short Ed25519 seed (secret key, 32 bytes) to a secret exponent (secret key, 64 bytes). This solved the import problem.

Development will be done on different Linux distributions using Python3. For Tezos the Python module PyTezos does, what I am expected from. Snippets are in the pipeline for creating accounts, making transactions, requesting account and balance informations as well as delegating of a given account to a new baker.

Delegation of an account to a baker is somehow tricky. A delegation to yourself is registering yourself as baker. The problem doing this is that this account cannot be unregistered. This seems a be a restriction of PyTezos or Tezos itself.

I also learned upt to now, that the funds of an account can be removed in principle down to 0,000001 ꜩ. I played arround with transactions and this was the result of doing so. It seems that a minimum amount of 0.275 ꜩ is needed for delegation not for the account itself.

If you like the snippets or/and little tool and if you find it helpful to use, I appreciate a small donation to my Tezos public key address:

tz1SAXFTMxyer8MGuUya4aALDm6j3185ivJt 
