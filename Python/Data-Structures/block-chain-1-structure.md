# Block Chain I - Structure

## TK

Block chains are data structures that are useful for storing a ledure of transactions that is univeraly agreed upon. This forms the basis for cryptocurrency and is usefull for a veriety of different fields such as voting

The core principal of block chain tech moves from the consept of trust to the consept of proof. The consept of proof attempts to resolve 

This sounds simple but it's a form of a classic pronlem called the [Byzantine Generals](https://en.wikipedia.org/wiki/Byzantine_fault)

As with most of human endeavor, the problem arises with bad actors seeking to cheat the system for their own benifit. Blockchain is an elegent solution to this problem. 

The most famous, and most valuable, blockchain is called Bitcoun. it was first described in a [whitepaper](https://bitcoin.org/bitcoin.pdf) released by a person or entity called `Satochi Nakamoto`.

A technical glossary of thers can be found [here](https://bitcoin.org/en/developer-glossary)

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
