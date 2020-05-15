# Guided Project - 01/14/19

## why python?

- easy to read
- very popular language. Many jobs will request
- popular back-end language

## Single vs double quotes

Can print "" within ''

## what about F strings?

f strings are used when you need to insert variables within a string

ex.

```python
name = 'Chris'
print(f'My name is {name}')
```

output

```
My name is Chris
```

## pass key word

this key word allows you to defign a function without any code

```python
def my_function():
    # nothing here
    pass
```

## out[a:b]

this function will cut you a pice of a list with the starting index `a` and ending just before index `b`

### REMEMBER!

lists may not alwase be the most efficient data structure

### Boleans

```python
def sum67(nums):
    sum = 0
    adding = True

    for i in nums:
        if i == 6:
            adding = False
        elif i == 7 and adding == False:
            adding = True
        elif adding == True:
            sum += i

    return sum
```

this is valid but is poor styling. This is the correct way:

```python
def sum67(nums):
    sum = 0
    adding = True

    for i in nums:
        if i == 6:
            adding = False
        elif i == 7 and not adding:
            adding = True
        elif adding:
            sum += i

    return sum
```

the `not` opperator is the same a calling false

## List comprehention

performing operations to create a new colection from an existing one

ex.

```python
numbers = [1, 2, 3, 4, 5]
squares = [i*i for i in numbers]
print(squares)
```

##### with conditions

```python
evens = [i for i in numbers if i % 2 == 0]
```

same as

```python
evens_two = []
for i in numbers:
    if i % 2 == 0:
        evens_two.append(i)
```

here is a cool example of a list comprehention that eddits a string that starts with the letter 's'

```python
 with_s = [s.capitalize() for s in names if s[:1].capitalize() == 'S']
```

### List comprehention quick guide

```
list = [operation - loop - condition]
```

# DATA STRUCTURES

### lists

- int index
- duplicate elements
- mutable

### strings

- not mutable ~ you can change the contents of a string but you can not modify the contents of a string

### Dictionary

- key value pairs
- unorderedf

```python

```

output

```python
value_1
```

DICTIONARIES ARE NOT ORDERED!!!!

elements can only be refed via key.

### Set

- no duplicates
- unordered
  sets have the same syntax as dicts but there is only a value and no key

```python
my_set
```

### Tuple

- immutable
- otherwise same as lists
- use parenthesies

```python
my_tuple = (1, 3, 5, 45)
```
