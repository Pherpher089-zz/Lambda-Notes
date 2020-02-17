# Linked Lists

```python
arr[::-1]
```

This will revers a list in python

```python
a[i], a[j] = a[j], a[i]
```

This will swap the item at index _`i`_ with the item at index _`j`_

## Array operation and run time

### inserting and deleting

inserting and deleting data from an array is `O(n)`. The array must move all the other elements in an array in order to make new space or close newly created space in the array.

for example, adding '5' at index 2

```
|1|2|3|4|
|1|2|3|4| |
|1|2|3| |4|
|1|2| |3|4|
|1|2|5|3|4|
```

and deleting the same '5'

```
|1|2|5|3|4|
|1|2| |3|4|
|1|2|3| |4|
|1|2|3|4| |
|1|2|3|4|
```

### Accessing elements

Accessing elements in an array is constant time or `O(1)`

## Linked lists

### Singly linked list

Singly linked list use node objects that hold a `value` and a `pointer` to the next node in memory.

The `tail` node will always point to `None`.

**Insertion and deletion in linked lists** is `O(1)` or constant time

**Searching** a linked list is linear or `O(n)`
