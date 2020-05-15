# System Stack

Most CPUs have a built-in stack that’s useful for keeping temporary data, making subroutine calls, and handling interrupts. We’ll learn how the stack operates

## Overview

Since the number of registers is limited on a CPU, the stack is a useful place to store data temporarily. We’ll examine a sample scenario where this is the case.

Stack at this low of a level still have a `PUSH` and a `POP`. They also have a `sp` or a stack pointer which points to the last element of the stack. This pointer is kept in a special purpose register or a general purpose register.

Another thing to note, is that the stack starts at a high memory address and decrements downward. This memory will typically exist above the program in memory. If too much info is stacked and it collides with the program in memory its

# STACK OVERFLOW!!!!!!!!!!!!!

### How is the stack used commonly

-   temorary variables
-   store the return address of a sub routine
-   storage of registers and CPU state while handling an interupt
-   alocating local variables of a sub routine

### Challenge

1. What happens if you PUSH too many items on the stack?
    - Stack overflow!
2. What happens if you POP from an empty stack?
    - Underflow
3. How can you detect if the stack is empty?
    - A stack base and stack limit are stored in registers to keep track, preventing stack overflow or underflow _<< Im not sure if this is correct_
4. What information must be saved on the stack when the CPU is servicing an interrupt? Why?
    - The current registers and the current CPU state must be saved to the stack

## Interrupts

-   these are commonly triggered by a peripheral device with a complete process ready for the CPU. This will send a signal to the CPU to stop what it's doing currently and focus on this new task.
-   The CPU state is saved to memory and the CPU continues to the address of the _interrupt handler_
-   A the handler completes, the processor state is popped of the stack and it resumes like nothing happened

## Interrupt vector table

-   Most CPU's have a look up table: _interrupt vector table_
-   When say interrupt #2 occurs, the address of the handler is looked up on the table
-   its an array of pointers to interrupt handlers, one per interrupt
-   Different CPUs keep them in different parts of ram
-
