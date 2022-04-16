# Snippets and Tools for use with Tezos
## Motivation

<p align="justify">While using Tesoz I figured out, that a Tezos private key can be given in short or in long form. Importing a short private key from one wallet into another wallet failed. I took a deeper look into this problem. The result was that I installed everything to program tools I need to overcome my problems. I am now able to write different tools, which can be used together with Tezos. The first result was a snippet or tool which converts a short Ed25519 seed (secret key, 32 bytes) to a secret exponent (secret key, 64 bytes). From the Tezos point of view short and long versions of the secret key works the same way. For the wallets it makes a difference.</p>

##Development Environment

<p align="justify">Development will be done on different Linux installations which are based on Debian distributions. I generally don't use any other OS on desktop computer or laptop. I use systems based on AMD and ARM architecture. I use Bash or Python as programming language. In general Python is used in version 3. Mainly PyTezos from PyPi is used for the Tezos developments. Python code check is done using Pylint.</p>

## Open Issues

Open issue is how to get all Tezos transactions of the past in a short period of time. It is not clear how to mint and burn NFT's.

## Lessons Learned

<p align="justify">Delegation of an account to a baker is somehow tricky. A delegation to yourself is registering yourself as baker. The problem doing this is that this account cannot be unregistered. This seems a be a restriction of PyTezos or Tezos itself.</p>

<p align="justify">I also learned up to now, that the funds of an account can be removed in principle down to 0,000001 ꜩ. I played arround with transactions and this was the result of doing so. It seems that a minimum amount of 0.275 ꜩ is needed for delegation not for the account itself.</p>

<h2>Donation</h2>

<p align="justify">If you like the snippets or/and little tools and if you find it helpful to use, I appreciate a small donation to my Tezos public key address:</p>

<div class="snippet-clipboard-content position-relative overflow-auto" data-snippet-clipboard-copy-content="tz1SAXFTMxyer8MGuUya4aALDm6j3185ivJt"><pre><code>tz1SAXFTMxyer8MGuUya4aALDm6j3185ivJt</code></pre></div>

<p align="justify">If you do so. Thank you very much! Every Mutez is welcome.</p>
