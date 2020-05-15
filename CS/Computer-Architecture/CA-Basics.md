# Training Kit

## CPU Functional Components

### The Beginning

-   _Transistors_, the most basic
-   _Gates_, made of transistors
-   Digital Logic common operations performed by gates
    -   `AND`, `OR`, `NOT` like we've seen in conditionals in code
    -   `XOR`, `NOR`, `NAND`
-   Gates can be combined together into far more complex structures like **ALU** and **CPU**

### RAM

-   Stands for "Random access memory"
-   This memory is very fast compared to hard drives (even SSDs)
-   Ram is a huge array of bytes with each index being an address
-   Each element in RAM can store 1 byte or 8 bits
-   Larger, multi byte values are stored in sequential addresses on RAM

### CPU words

-   Bytes of data are stored in in RAM
-   Larger 64b (8B) values are stored in sequential addresses on RAM, that the CPU can operate on all at once called `Words`
-   The exact number of bytes per word depends on architecture
    -   8B for a 64b processor
    -   4B for a 32b processor
    -   1B for a 16b processor
-

### CPU Registers

Registers store words that can be accessed at supper high speeds

-   This is data that is stored on deck for the CPU to access. Think of them as variables that the CPU has at it's disposal.
-   Similar to RAM but it's stored directly on the processor
-   There are a limited number. 8, 16, or 32 depending on the processor
-   They have fixed names. e.g **R1**, **R2** or **EAX**, **EBX** depending on the CPU
-   Many CPUs can _only_ perform math operations on registers which must be loaded from RAM first. (x86 family can perform math on registers quickly or on RAM slowly)

### CPU Instructions

-   Are also stored in RAM with other data
-   Are actually just numbers
-   Humans often use mnemonics to refer to the instructions in a human readable way.
-   The CPU keeps track of the current instruction in RAM and performs different tasks based on the instruction found there
-   The address of the currently-executing instruction is held in a special register called the `program counter`
-   CPUs usually have a significant number of instructions, around 50-200

### CPU Clock

-   Clock in a modern CPU triggers a few billion times per second
-   Clock cycle rates are measured in Hz, KHz, MHz, or GHz (Billions of cycles per second)
-   Each instruction takes one ore more clock cycles to execute
-   The faster the clock the more instructions it can do per second

### Congruency

How the CPU does more than one thing at once

-   Each hardware piece can do one thing at once
-   Duplicate the hardware pieces
-   Multicore CPUs
-   Pipelining
-   Time Sharing - switching back and fourth between tasks very quickly

### System Bus

How data is passed between system components

-   **Address Buss:** carries the address of the value in RAM were interested in or the ID of the peripheral were interested in
-   **Data Buss:** carries data to be transmited to or from ram or peripherals
-   **Control Buss:** controls weather or not the CUP is communicating with RAM or peripherals
-   The size or width of a buss is measured in bits. A 64b processor will have a 64b buss

### Caching

A cache is a group of registers on the CUP meant for holding extra data that the CUP might need. It will check the cache before going all the way to RAM for the data it is looking for. If the data the CPU needs is in the cache, it's considered a `cache hit` and if the data is not there, it's a `cache miss`.

-   RAM is slow
-   Register is fast
-   middle ground? Cache
-   Closer to the CPU
-   Usually arranged in a level hierarchy

## Number Bases and conversions

_There are 10 kinds of people in the world: those who understand binary and those who don’t._

The 3 main value representations we are working with are `decimal`, `hexadecimal`, and `binary`

### Number bases

-   Decimal is a base 10 system. i.e. there are ten digits to cylce through before we add another column:(0, 1, 2, 3. 4, 5, 6, 7, 8, 9)
-   Binary has is base 2: (0, 1)
-   Hexadecimal is base 16: (0,1, 2,3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)
-   Octal is base 8:(0, 1, 2, 3, 4, 5, 6, 7) - not often used
-   Hexadecimal is called _hex_ for short

Here are some of these bases are recorded in JS

```javascript
// All of these represent the number of apples on the table:

let numA = 12; // decimal
let numB = 0xc; // hexadecimal, leading 0x
let numC = 0b1100; // binary, leading 0b

(numA === numB) === numC; // TRUE!
```

### Base 2

Computers find it convenient to represent numbers in base 2 for a variety of reasons. One is that it’s easy to represent as a voltage on a wire: `0` volts is a 0 and `5` volts (or whatever) is a 1. Another is that you can do boolean logic with `0` being `FALSE` and `1` being `TRUE`.

### Some Terminology

`Byte` - 8 Bits
`Nibble` - 4 bits: highest dec value - 15
`Octet` - Synonym for byte

### Octal Trap

Octals numbers are rarely used. You can specify octal numbers in most programming languages with a leading zero:

```python
x = 12 # decimal
y = 012 # octal, decimal number 10
```

Don't pad decimal numbers with a leading 0

### Conversions

#### Converting binary to decimal

##### By hand

```
+--------128s place
|+-------64s place
||+------32s place
|||+-----16s place
||||+----8s place
|||||+---4s place
||||||+--2s place
|||||||+-1s place
||||||||
00110101
dec value: 53
```

##### In JavaScript

```javascript
// Binary constants:

let myBinary = 0b101; // 101 binary is 5 decimal

// Converting a binary string to a Number

let myValue1 = Number("0b101");

// or

let myValue2 = parseInt("101", 2); // base 2

// All these print 5:
console.log(myBinary); // 5
console.log(myValue1); // 5
console.log(myValue2); // 5
```

#### Converting a decimal to binary

##### In Javascript

```JavaScript
// Decimal constants (just like normal)

const val = 123;

// Converting a decimal to a binary string

const binVal = val.toString(2); // convert to base 2 number string

console.log(`${val} decimal is ${binVal} in binary`);
```

##### By hand

Converting a bin number to hex starts with separating the byte into nibbles. Then replace each nibble with its hex equivalent.

```
10010011
    |
1011 0011
  |   |
  B   3
   \ /
   B3
```
