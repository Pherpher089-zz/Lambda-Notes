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
- A proposed solution using a specific hash can be quickly and easily varified by hashing that solution and seeing if it passes. 

#### Proof of work 
Proof of work secures the chain by making it nearly computationaly impossible to cheat, because the cheeter would have to do a freater amount of work than everyone else.

[Proof of work](https://en.wikipedia.org/wiki/Proof_of_work) is an arbitrarily difficult problem to solve. For example, it 
# HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Lecture
### Take aways 
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
# The second parameter us used to make sure the dict. is ordered and creates a consistent hash
```

## Flask

```py
    # causes the method below to be static
    @staticmethod 
```
