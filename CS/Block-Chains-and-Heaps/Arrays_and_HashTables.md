# Lecture

## Hash Tables

-   used a lot in encryption
-   AKA hash maps
-   Used to implement objects
    -   objects are objects with extra functionality
-   Cost of O(1) for access, addition and deletion

Hash tables are made up of an `array` and a `hash function`.

## Hash

-   Deterministic: for a given input, the output will always be the same
-   Defined out put range: All values must hash to a value within the givin range
-   Predicable speed: Hash tables are fast but cryptographic hashes are very slow
-   Non-invertible: Can not figure our what was put in based on what came out
-   Avoid collisions:
    -   collisions are two different key values that hash out to the same thing

#### djb2 hash function

A method of scrambling a value using bit shifting

```python
def djb2(key):
    # start with a high prime number
    hash_value = 5381

    # scramble this bitch up
    for char in key:
        hash_value = hash_value + (hash_value << 5) + char

    return hash_value
```

`sha256` is a hashing algorithm that is so complicated that the government cant break it. It produces almost no collisions and it is lightning fast

some common hashing libs are

-   `hashlib`
-   `bcrypt`

salt - a value used to add to the hash function to further complicate it. Like an additional seed to add to the function
