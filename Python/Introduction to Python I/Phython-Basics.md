# Python Basics

## Why Python?

- First release: 1991
- Emphasizes readablility
- Supports multiple programming paradigms
- Named after Monty Python

Latest version = 3.7

### Some common operations and statments

- comparitor operators = and or not
- comparitor statements = if elif else
- loops = for i in range(10)

### Comments

```python
#Single line comment
"docstring comments => are availible at runtime by accessing __doc__ variable"
```

### Operators

incrament and decrement oporators

```python
i += 1
i -= 1
```

logical operators

```python
and
or
not
```

strings

```python
"strings are the same as JS"
# However, we can't concatinate them like in js
# for example:
s = "bob"
x = 5
# we would have to type cast the int to a string
print(s + str(x))
```

conditional statment

```python
if grade > 85:
    return "E"
elif grade >= 70:
    return "S"
else:
    return "F"
```

arrays and lists

```python
# In python arrays are called lists
nums = [1,2,3,4]

# Need to watch your bounds
nums[99] = 100 #NOT OK

# A loop with this list
for n in nums:
    #some code
```

White space must be used to format your code
