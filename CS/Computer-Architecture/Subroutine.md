# Subroutines

-   Think of them like function calls
-   In assembly we use `CALL` at a particular address
-   We use `RET` to return to where we left off

## Limitations

-   can not pass arguments
-   no return values
-   these can be implemented in a few way

## Use of the stack

-   when we hit the `CALL` command, we need to store the return address somewhere
-   CPU's tend to use the stack for this.
-   Call will push the address of the instruction onto the stack after it and move to the sub routine address

Subroutines are used to escape writing the same code twice. Any place you would find a function call in a higher level language, a subroutine is a good idea.
