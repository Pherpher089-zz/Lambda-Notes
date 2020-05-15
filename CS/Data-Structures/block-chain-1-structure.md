# Block Chain I - Structure

## TK

Block chains are data structures that are useful for storing a ledure of transactions that is univeraly agreed upon. This forms the basis for cryptocurrency and is usefull for a veriety of different fields such as voting

The core principal of block chain tech moves from the consept of trust to the consept of proof. The consept of proof attempts to resolve 

This sounds simple but it's a form of a classic pronlem called the [Byzantine Generals](https://en.wikipedia.org/wiki/Byzantine_fault)

As with most of human endeavor, the problem arises with bad actors seeking to cheat the system for their own benifit. Blockchain is an elegent solution to this problem. 

The most famous, and most valuable, blockchain is called Bitcoun. it was first described in a [whitepaper](https://bitcoin.org/bitcoin.pdf) released by a person or entity called `Satochi Nakamoto`.

A technical glossary of thers can be found [here](https://bitcoin.org/en/developer-glossary)

### Learn
Block chains are linked by hash values in order to maintain integrity.

#### The Block
Each block has the folowing components:
- Index - The nimber of blocks in the chain. This starts at 0 or 1, depending on the chain.
- Timestamp - The time at which the block was created. This is not required but is often useful.
- Transactions - The monetary transactions, or any type of data, that is proofed by the block.
- Proof - The proof for this block.
- Previous Hash - The hash of the previous block.

The hash of the previous block is what preserves the integrety. This means that if a bad actor attempts to change a block in the middle of the chain, they must recreate all of the following blocks in the chain. Otherwise, the invalid chain can be identified very easily. 

In the example project, we use the `sha256`. This is used for both creating hashes for blocks as well as proof of work. This algorithm is used because:
- The outcomes are unpredictable but deterministic.
- A proposed solution using a specific hash can be quickly and easily verified by hashing that solution and seeing if it passes. 

#### Proof of work 
[Proof of work](https://en.wikipedia.org/wiki/Proof_of_work) is an arbitrarily difficult problem to solve. For example, it would take the average computer 100 years to mine a bitcoin block on it's own

Proof of work secures the chain by making it nearly computationally impossible to cheat, because the cheater would have to do a feater amount of work than everyone else.

When a solution is discovered, a block i mined and added to the chain by the node that discovered it, or the first one that was reported - assuming the node finds the solution to be valid. Then the node hashes the previous block and add the rest of the properties, including a timestamp, index, and the list of pending transactions, which are now confirmed. It then shares the new block with the nodes in it's network, which checks the new block to make sure that is has an index one higher than the last block, and a valid solution. If these checks pass, then the new block is added and spreads through the network, bearing in mind that `consensus` is determined by the longest valid chain. 

- Created as a technique to combat spam - see Hashcash
- An Arbitrarily difficult problem that is solved by spending a large amount of computation time.
- Work can not be reused - though some systems are vulnerable to this kind of exploit.
- Solutions are difficult to compute and easy to verify.
### Take away 
- How blocks are chained together by the hashes of their predecessors
- How proof of work makes it nearly impossible for an individual attacker to compromise the chain
- How to write a program that can mine coins
- How to derive an account balance from the transactions in the ledger

Block chains work if there are miners. 

```python
hash('key') - -> integer
hash('string with spaces')
hash('{key, value}')
# Any string can be hashed so any data that can be 
# stringified can be hashed.
chain = [
    {index, timestamp, transactions: [], proof},
    {index, timestamp, transactions[], prev_hash, proof},
    {},
]
```
The first block is called the `genesis block`

```python
# Turns the object passed in, into a string
json.dumps({'myObj': myObj}, sort_keys=True) --> "{'myObj': myObj}"
# The second parameter us used to make sure the dict. is ordered and creates a 
# consistent hash
```

## Flask

```py
    # causes the method below to be static
    @staticmethod 
```

# Notes during project

```python
string.encode()
#This method is used to make sure all of the string data in `string` is of a
#  uniform type. There are many different byte patterns used for chars and this
#  method will return the string of chars in a uniform type.

# We are using it in our valid_proof method in order to pass the string in 
# question into the sha256 method. It formats the string data so that it 
# complies with the hash method.
```