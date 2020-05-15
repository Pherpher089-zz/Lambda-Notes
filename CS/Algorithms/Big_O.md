# Big O Notation
https://www.youtube.com/watch?v=8txRWyV6cnQ&feature=youtu.be

## The secret of coding
Beautiful code is both ELEGANT and EFFICIENT 
- BEAUTIFUL: concise, easy to read, easy to understand, easy to maintain and easy to modify
- EFFICIENT: Minimal CUP operations, minimal memory/storage requirements

```python
```
**O(1)**
```python
def get_books():
    return books
```
There is only 1 operation in this function. 

This is **Constant Time**. This is an operation that runs in the same amount of time every single time. This is regardless of the size of the books variable. Wouldn't a bigger list take longer to return? No because every time this function is returning a pointer to the list books.

*~Computers love constant time~*

**O(n)**
```python
def get_num_books():
    num_books = 0
    for i in books:
        num_books += 1
    return num_books
```
This function runs in **Linear Time**. This means that the number of operations is equal to the number of strings in the books list. As books gets bigger, so does the number of operations.
