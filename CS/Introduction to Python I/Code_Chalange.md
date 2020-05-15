### Tuples

!!!you have to add a commo after a single element declaration or python will conver the tuple into the type of the element

### Function Arguments

- Positional Arguments
- Arbitrary Arguments
- Key-word Arguments

#### Positional Arguments

So far, I belive that these are the arguments that appear in the parantheseies of your function definitions

#### Arbitrary Arguments

the `*` oporator allows us to defingn an arbitrary argument. These arguments allow any number of values to be passed in without explicity defigning the function with that number of values

```python
def f2(*args):
    _sum = 0
    for i in args:
        _sum += i
    return _sum

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33
```

Traditionaly, `args` is the standard name for an arbitrary argument

--NOTE--

When passing a list into a function with an arbitrary argument, you must use the `*` argument to spread that list out into the function

```python
a = [7, 6, 5, 4]

print(f2(*a))
```

#### Key-word argumnets

key word arguments are called by their key in a function call

```python
def add_nums(a, b)
    return  a + b

add_nums(a = 5, b = 7)
```

in key words can be referenced with the `**` operator

```python
def f4(**kwargs):
    for key, value in kwargs.items():
        my_str = "{} == {}"
        print(my_str.format(key, value))
```

### Scope

any variable defigned out side a function is a global variable. You can not modify the values of a global variable inside function scope however, without using the `global` key word

```python
x = 12

def change_x():
    global x
    x = 99
```

conversly you can use the key word `nonlocal` to tell a funtion to look outsied its scope for a variable.

```python
def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()
```

### File IO

the `open()` function returns a file object. There are two arguments that are passed into this function. The first is the file name and second is the mode

mode arguments

- w = write
- r = read (default)
- a = append
- r+ = read and write

### Classes

`Python Doc's`

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

- can have veirtual members
- can defingn oporators for the class
- Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object
