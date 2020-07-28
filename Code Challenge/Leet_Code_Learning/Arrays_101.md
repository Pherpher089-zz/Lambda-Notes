# Arrays 101

## A Array - A DVD box?

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
