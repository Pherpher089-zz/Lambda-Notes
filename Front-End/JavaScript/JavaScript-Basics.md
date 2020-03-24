# JavaScript

## Variables and scope
### Difference between let and var
 ```javascript
 function exapmple() {
    // Can only be accessed within the scope of the block it was defigned in - block scope
    // Mutable - can be changed after definition/declaration
    let localScopeVar = 0
    //Can be accessed outised this function - global scope
    // Mutable - can be changed after definition/declaration

    var globalScopeVar = 1
    // Can only be accessed within the scope of the block it was defigned in - block scope
    // Immutable - can not be changed after declaration
    const localScopeConstantVar = 2

    //Allowed
    localScopeVar += 1
    //Allowed
    globalScopeVar += 1
    //Not allowed
    localScopeConstantVar += 1

 }
    //Not allowed
    localScopeVar += 1
    //Allowed
    globalScopeVar += 1
    //Not allowed
    localScopeConstantVar += 1
 ```

