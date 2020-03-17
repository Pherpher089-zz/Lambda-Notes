# Arrays

## Training Kit

### Objective

1. Understanding the memory structure of an array.
2. Understanding how inserting into an array works.
3. Understanding the difference between arrays and python lists.

**What is an array?**
A sequence of homogenous data stored in a contiguous block of memory

**Declaring an array**

1. Determine the size of the array
2. Request a block of memory that will fit that array
3. Receive the address of the memory block that will fit that array
4. Write your values into the array

**Example**

Declaring the array:[2,3,4,5]

1. an integer is 4 bytes, so the array needs to be 16 bytes.
2. Request 16 bytes of memory from the computer.
3. Receive the 16 bytes of memory.
4. Write the values 2, 3, 4 and 5 into the array.

```
// Memory

25600    25601    25602    25603
00000000 00000000 00000000 00000010

25604    25605    25606    25607
00000000 00000000 00000000 00000011

25608    25609    25610    25611
00000000 00000000 00000000 00000100

25612    25613    25614    25615
00000000 00000000 00000000 00000101
```

```
// To access the index of an array
//  index * sizeOf(type) + start_address
```

This is very `time efficient` due to the three operations that are used. Addition and multiplication are very fast operations for a computer. Finding a spot in memory is also extremely fast. This operation happens in constant time `0(1)`. Arrays are also very `space efficient` because the amount of space that will be needed is exact to the amount of data that will be stored within.

** Adding**

1. Request a block of memory of the new size.
2. Copy each element of the new array one at time.
3. Free the memory of the old array.
    - This is an O(n) operation.

The issue with arrays is that `resizing is very inefficient`. Computers can only do one operation at a time and so recopying is very relatively slow. Furthermore, releasing the old array from memory creates `garbage` in memory. This space is then useless until garbage collection frees it up and creates `fragmentation` within the heap.

**How does Python add data an element to the end of an array?**

-   Python will allocate a few empty spaces to the end of the array each time it grows.
-   The amount of space it adds each time grows as well.
-   Thus adding an element to the end of an array is considered to be O(1) but can occasionally be considered to be O(n)

**How does python add an element to the BEGINNING of a list?**

1. Check to see if there is space at the end of the array
2. if not:
    1. Python will request more memory that needed and copy the new list over to that block with the new data first.
    2. Free memory up from the end of the array.
3. if so:
    1. python wil move all of the elements over one space toward the end and place the new element in front.
        - This is O(n) no mater what

**Conclusion**

-   Arrays are extremely time and space efficient.
    -   Accessing data from an array is the the fastest data retrieval.
    -   ...But not always
-   Python lists take care of simple operations
    -   ...But it's not magic
-   Understanding arrays can make your code much more efficient
