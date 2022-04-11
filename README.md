# Snippets and Tools for use with Tezos
<b>Introduction</b>

<p align="justify">While using Tesoz I figured out, that a Tezos private key can be given in short or in long form. Importing a short private key from one wallet into another wallet failed. I took a deeper look into this problem. The result was that I installed everything to program tools I need to overcome my problems. I am now able to write different tools, which can be used together with Tezos. The first result was a snippet or tool which converts a short Ed25519 seed (secret key, 32 bytes) to a secret exponent (secret key, 64 bytes). From the Tezos point of view short and long versions of the secret key works the same way. For the wallets it makes a difference.</p>

<b>Current Development</b>

<p align="justify">Development will be done on different Linux distributions using Python3. For Tezos the Python module PyTezos does, what one is expected from. Snippets or/and tools are in the pipeline for creating accounts, making transactions, requesting account and balance informations as well as delegating of a given account to a new baker. Open issue is how to get all Tezos transactions of the past in a short period of time.</p>

<b>Lesson Learned</b>

<p align="justify">Delegation of an account to a baker is somehow tricky. A delegation to yourself is registering yourself as baker. The problem doing this is that this account cannot be unregistered. This seems a be a restriction of PyTezos or Tezos itself.</p>

<p align="justify">I also learned up to now, that the funds of an account can be removed in principle down to 0,000001 ꜩ. I played arround with transactions and this was the result of doing so. It seems that a minimum amount of 0.275 ꜩ is needed for delegation not for the account itself.</p>

<b>General Prerequisites</b>

<p align="justify">General prerequisite for using the scripts is that PyTezos is installed. Installation can be done from PyPi using pip. Python3 is automatically pre-installed in the newer Linux distributions. At the moment I am using Python 3.8 as standard version. I generally limit myself to Linux or its derivatives. Taking care on other OS is not done. Python code check is done using Pylint.</p>

<b>Final Remark</b>

<p align="justify">If you like the snippets or/and little tools and if you find it helpful to use, I appreciate a small donation to my Tezos public key address:</p>

tz1SAXFTMxyer8MGuUya4aALDm6j3185ivJt 
