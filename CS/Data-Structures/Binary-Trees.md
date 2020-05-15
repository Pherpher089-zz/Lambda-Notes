# Binary Trees
### finding the middle of a linked list without the length of the list
using two pointers to move through the list. One that moves one node at a time and one that moves two nodes at a time. Once the faster pointer reaches the end, the slower node will be in the middle.

## Graph
consists of a finite set of verticies and edges that connect the verticies

They may or may not change or go in both directions

they may have weight and may be mutable

### Trees  
- graph were each vertex has one parent
- all parts are connected
  
#### Binary trees 
- every vertex has 0 - 2 children
- values are greater to or equal to the value stored in the right branch.
- values that or less than the parent node are stored in the left branch.
- Values less than the root node must be stored in the right most sub tree 

**depth first** - Uses a stack. Adds root node to stack and, while the length of the stack is greater than zero, pop the top node, operate on it. Then push it's left and right node onto the stack. 

**breadth first** - Uses a queue. Enqueue the root node. While the length of the que is greater than 0, dequeue the last node in the queue. Operate on it. Then enqueue it's left and right node. 