# Arrays 101

## A. Array - A DVD box?

What is an array?

> An Array is a collection of items. The items could be integers, strings, DVDs, games, books—anything really. The items are stored in neighboring (contiguous) memory locations. Because they're stored together, checking through the entire collection of items is straightforward.

On a computer, arrays can hold up to `N` items where `N` is chosen by the programmer.

Here is the code for creating an array to hold 15 DVDs in `Java`.

```Java
DVD[] dvdCollection = new DVD[15];

public class DVD {
    public string name;
    public int releaseYear;
    public string director;

    public DVD (String name, int releaseYear, String director) {
        this.name = name;
        this.releaseYear = releaseYear;
        this.director = director;
    }

    public String toString() {
        System.out.println(
            this.name + ", directed by " + this.director + ", released in " + this.releaseYear));
    }
}
```

Each place in our storage box has an identification number in the range of `0` to `N - 1`. `0` being the first. These numbers are called `indices`.

Lets put Avengers in the 7th index spot

```Java
DVD avengersDVD = new DVD("Avengers", 2012, "Joss Wendon");

dvdCollection[7] = avengersDVD;

```

Let's add a few more

```Java
DVD incrediblesDVD = new DVD("The Incredibles", 2004, "Brad Bird");
DVD findingDoryDVD = new DVD("Finding Dory", 2016, "Andrew Stanton");
DVD lionKingDVD = new DVD("The Lion King", 2019, "Jon Favreau");

// Put "The Incredibles" into the 4th place: index 3.
dvdCollection[3] = incrediblesDVD;

// Put "Finding Dory" into the 10th place: index 9.
dvdCollection[9] = findingDoryDVD;

// Put "The Lion King" into the 3rd place: index 2.
dvdCollection[2] = lionKingDVD;
```

`Java` always initializes data in an array to `null` if the data typ is an object. If it is a primitive data type it is initialized with 0, 0.0, or false.

Reading from an array

```Java
System.out.println(dvdCollection[7]);
System.out.println(dvdCollection[10]);
System.out.println(dvdCollection[3]);
```

Java `for each` loop syntax with an array:

```Java
for (int square : squareNumbers) {
    // Print the current value of square.
    System.out.println(square);
}
```

## Inserting Items into an Array

The three key operations for Arrays:

-   Inserting data into the array
-   Removing data from the array
-   Searching for data in the array

An array is a data structure which means that it stores data in a specific format
and supports certain operations on that data store.

There are three ways to insert data into an array:

-   insert data at the beginning of the array
-   insert data at the end of the array
-   insert data at a givin index in the array

#### Inserting data at the end of an array

This is the most simple of the three operations. Because the length is tracked for the array, all we do is add an element to the array at the base address + length + 1. As long as the array has enough pre-defined space for the new element, the time complexity is `O(1)`.

#### Inserting data at the beginning of an array

This is a less efficient operation. In order to insert at the beginning, every other element in the array must be moved forward one index to make space for the new data. This is `O(N)` time complexity.

#### Inserting data at a givin index in an array

This operation is similar to adding data to the beginning of the array. In this case only the elements with the givin index or grater need to be shifted to the right. If you think about it, adding to the beginning of an array is just a special case of inserting at a specific index, if that index was `0`. I believe this is `O(N)` in terms of time complexity.
 
## Array Deletions
Array deletions, like insertions, have 3 cases.
- Deleting an element at the end of the array.
- Deleting an element at the beginning of the array.
- Deleting an element at a givin index


### Deleting the last element of an array
This is the lest time consuming of all three cases. This simply removes the last element and nothing else needs to be done.

### Deleting an element at the beginning of an array
This is the most time consuming because once the first element is deleted, all of the other elements now need to be shifted to the right to fill the space. Here is an example of how that would look:

```java
for (int i = 1; i < length; i++) {
    // Shift each element one position to the left
    int_array[i - 1] = int_array[i];
}

length--;
```

### Deleting an element at a givin index
This is much like deleting an element at the beginning of an array accept that the process begins at a givin index and the elements before the givin index are preserved.


# Searching an Array
Searching through an array is the most important operation that is involved in dealing with arrays. It is the speed of the algorithm that helps programmers design their code base. 

Searching means finding a particular element in an array and returning it's position. We may want to search an array to find out if an element exists within, or we may be looking through an array with it's elements arranged in a particular order. 

### Linear Search
This is searching the array one element after another until you land on the one your looking for. This is the most inefficient way to search an array because it has the potential to search through every index. This is O(N) operation. 

### Binary Search
This method has us check the middle element of a sorted array and deciding if the target element is on the left or right side of the element in question. This operation is repeated on the sub array containing the target index. This is a O(N log N) operation. 