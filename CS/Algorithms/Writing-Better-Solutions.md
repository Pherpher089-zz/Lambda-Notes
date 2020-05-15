# Writing better solutions
## TK
Take this fib function for example
```python
def nth_fib(n):
    if n < 2:
        return n
    else:
        return nth_fib(n-1) + nth_fib(n-2)
```
This is a recursive function that is very inefficient with a runtime complexity of O(2^n). This is very very bad and completely unscaleable

#### Caching / Memoization Approach

The process of saving function calls and their return values so that a recursive function does not need to perform the same function twice.

This can be done with a dictionary. {n: function(n), n-1: function(n-1)}
 ```python
 def nth_fib(n, cache):
    if n < 2:
        return n
    elif cache[n]:
        return cache[n]
    else:
        cache[n] = nth_fib(n-1, cache) + nth_fib(n-2, cache)
        return cache[n]    
 ```
 this function is O(n)

#### An Iterative Approach
using a for loop can sometimes be the a good answer as well
```python
def nth_fib(n):
    n_1 = 1
    n_2 = 0
    answer = 0
    for i in range(n-1):
        answer = n_1 + n_2
        n_2 = n_1
        n_1 = answer
    return answer
```
This function is also O(n)
### Dig Deeper

Analysis - Problem solving with Algorithms and Data Structures using Python

https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/toctree.html

Only once array problem - first pass solution

**https://youtu.be/9_3-PuzH26A**

Only once array problem - second pass solution

**https://youtu.be/Fy8b5YAYzw4**

## Lecture

**Runtime Complexity** - A measure of the efficiency of an algorithm based on the number of operations that are performed in relation to input

**Space Complexity** - A measure of the efficiency of an algorithm based on the amount of space is used in relation to input
