# Intro to Python III 1/20/20

## Classes

Classes are like blue prints for objects. These are defigned spesific sets of data. Objects are instances of classes.

### Inicialisaion of classes in Python

```python
class NewClass:
    def __init__(self, init_val1, init_val2):
        #This is the constructor. Self means this
        self.init_val1 = init_val1
        self.init_val2 = init_val2

```

GThe self key word is what is used to point to the spesific instance of the class. It is used to initialize data passed into the constructor

#### **str** method

This method tels the class how to print it's self. It must return a string to print however you decide to do that.

```python
class Waypoint:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'name: {self.name}\n latitude: {self.lat}\n longitude: {self.lon}'
```

#### !NOTE!

the '\' character will denote that a string (literal) is multilined and can be returned in python code.

```python
my_string = f'This is a super duper long line' \
    f'that continues down here!'
```

### Importing

```python
from fileName import className
```

this line of code is how another class is imported to another
