# Itorative Sorting

## Training Kit

### Linear and Binary search

#### Linear

linear search - search one item at a time in order. This is however very inefficient. The runtime for this algorthm is O(n) (I think)

#### Binary

For a binary search, your data must be sorted in a liner order.

```python
def linear_search(arr, target):
    for i in range(0, arr.len()):
        if arr[i] == target:
            return 1
    return -1
```

The first element we search in a binary search is the middle element. If the value we are searching for grater than this value, we search the grater half of the list in the same way. If the value is lower we search the former half. This process is repeated until the value is found. O(log(n)) is the run time for this search.

```python
def binary_search(arr, target):
    low = 0
    high = arr.len() - 1
    while low <= high:
        middle = low + high / 2
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return middle
    return -1
```

To make this algorithm useful though, we must sort the data

### Iterative sorting

**algorithm** - A set of steps to solve a problem

**Iterative algorithm** - Repeat one or many steps until a problem is solved.

#### Insertion sort

Sorting against the first element first. If the second element is less than the first, shift the first over and insert the second before it. At this point, the number of sorted elements is +1. Continue with the next element until this process is complete. You must track the size of the sorted elements sublist.

```
TRAINING KIT

Insertion Sort
How It Works

Conceptually, split the collection into “sorted” and “unsorted” sections
Remember, a single element is always sorted…so we can think about the first element as a sorted list containing a single element, while everything else is unsorted

For every index in the collection from 1 to length-1:
Compare the element at the current index, i, with everything on its left to identify it’s correct position in the sorted subcollection
Shift those elements over to the right until the correct position is reached
i++

Runtime
The original order of the collection can affect the number of comparisons and swaps that need to be performed, which can make this algorithm more efficient in specific cases. However, in a worst case scenario, it will run in polynomial time. In the next module, we’ll spend more time exploring what is significant about the different runtime classifications. For now, just know that a polynomial runtime is not good.
```

#### Selection Sort

In this algorithm, start with searching for the lowest value and swap it with first element(arr[0]) in the list. Next start with the first unsorted element (arr[1]) and search for the next value in line and replace it with the value in [1]. Continue until the list is sorted.

```
TRAINING KIT

Selection Sort
How It Works

For every index in the collection from 0 to length-2:
Compare the element at the current index, i, with everything on its right to identify the position of the smallest element
Swap the element at i with the smallest element
i++

Runtime
There is no original order of elements that can be sorted more efficiently using this algorithm. Best case, average case, and worse case scenarios are all the same. Like Insertion Sort, this algorithm’s runtime is polynomial ( O(n^2) ).
```

#### Bubble sort

Compare the first two elements of the list and reorder them if left is grater than right. Continue by checking the previous left with its new left. ie ([0] with [1] then [1] with [2] ect).
Continue to the end of the list. If one pare was reordered, repeat the process.

```
TRAINING KIT

Bubble Sort
How It Works
In this sorting algorithm, we start at the beginning and compare each element to its right hand neighbor. If the right hand neighbor is smaller, we swap the two neighbors.

The above process is repeated until we pass through the entire collection without performing a single swap. With each pass, the larger elements will “bubble” toward the right hand side of the collection.

Runtime
If we get really lucky, our collection will already be in (or mostly in) order. In this case, we only need to pass through the collection a few times to sort everything. However, in a worse case scenario (a collection in reverse order), we need n-1 passes through the collection for every element to “bubble up” to its correct position. This leads to a runtime of O(n^2).
```

#### Polya's Problem Solving Techniques

https://github.com/LambdaSchool/CS-Wiki/wiki/Polya%27s-Problem-Solving-Techniques

### Follow Along

A few general things that you can think about when working to translate the overviews of the algorithms above into Python are…

Keywords that imply a loop is required

- while / for
- as long as
- until

Conditions that can be checked with if/else blocks

- when we find \_\_
- if \_\_ happens
- once this value is large/smaller

What type of value should be returned?

```python
def insertion_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # How many loops will be needed to complete this algorithm?
    # How do we know how many items should be shifted over to the right?
    # What do we need to do so that we don't overwrite the value we are `inserting`?

  # What, if anything needs to be returned?
```

```python
def selection_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # How many loops will be needed to complete this algorithm?
    # How do we know when we are ready to swap values?
    # And how do we keep track of which values should be swapped?

  # What, if anything needs to be returned?
```

```python
def bubble_sort(elements):  # If `elements` is a collection, remember it will be passed by reference, not value

  # We only need to loop through `elements` until we make a pass that leads to 0 swaps. How do we keep track of whether or not any swaps have occurred?
  # Do we always need to loop through all elements?
    # Depending on how our loop was set up, which neighbors should be compared?
    # Can we do swaps in Python without a `temp` variable?

  # What, if anything needs to be returned?
```

## Lecture
