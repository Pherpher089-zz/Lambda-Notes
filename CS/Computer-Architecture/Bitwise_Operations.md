# Bitwise operations

`NOT` or an inversion will output the opposite of what is input

| A   | NOT A |
| --- | ----- |
| `0` | `1`   |
| `1` | `0`   |

`AND` requires two inputs and produces an output that is `true` if the inputs are the same and `false` otherwise

| A   | B   | A AND B |
| --- | --- | ------- |
| `0` | `0` | `0`     |
| `0` | `1` | `0`     |
| `1` | `0` | `0`     |
| `1` | `1` | `1`     |

`OR` or takes two inputs and output `true` if either one of the inputs is `true`.

| A   | B   | A OR B |
| --- | --- | ------ |
| `0` | `0` | `0`    |
| `0` | `1` | `1`    |
| `1` | `0` | `1`    |
| `1` | `1` | `1`    |

`NAND` takes in two inputs and outputs `true` if either of the inputs is not `true`. This is an inverted `AND`

| A   | B   | A NAND B |
| --- | --- | -------- |
| `0` | `0` | `1`      |
| `0` | `1` | `1`      |
| `1` | `0` | `1`      |
| `1` | `1` | `0`      |

`NOR` takes in two inputs and returns false if either one of the inputs is true. This is an inverted `OR`

| A   | B   | A NOR B |
| --- | --- | ------- |
| `0` | `0` | `1`     |
| `0` | `1` | `0`     |
| `1` | `0` | `0`     |
| `1` | `1` | `0`     |

`XOR` takes in two inputs and returns `true` if the inputs are different

| A   | B   | A XOR B |
| --- | --- | ------- |
| `0` | `0` | `0`     |
| `0` | `1` | `1`     |
| `1` | `0` | `1`     |
| `1` | `1` | `0`     |

# Multi bit numbers

### AND

      11101011
    & 10011101
    |---------|
      10001001

The `AND` bitwise operator can also be used as a mask. Any place there is a `1` in the mask, the the corresponding bit will be preserved in the result. For instance:

      11101011
    & 11110000
    |---------|
      11100000

The first 4 bits of this byte are as they were in the masked byte before the mask. The remaining 4 bytes are just zeros

### XOR

      11101011
    ^ 10011101
    |---------|
      01110110

### Shifting

Shifting the bits in a number left or right. There is a minor difference in the outcome of each operation.

#### Left shift

```python
0b11001011 << 2 = 0b1100101100
0b1 << 3 = 0b1000

```

the left shift operation, followed by the amount of shifts to perform will place that many `0`s to the beginning of the number.

#### Right shift

```python
0b11001011 >> 4 = 0b1100
0b1101 >> 2 = 0b11
```

shifting right will simply truncate the leading bit.

### Python bitwise operators

-   AND = `&`
-   OR = `|`
-   NOT = `~`
    -   Also known as the unary operator. This returns the opposite of the givin bit.
-   LEFT SHIFT = `>>`
-   RIGHT SHIFT = `<<`

### Finding you pc_count

```python
IR = 0b10100000
IR >> 4
pc += (IR & 0b0001) + 1
```
