# Graphs I

## Training Kit:

_aka: Network_

When a graph has a lot of edges we call it `dense` otherwise we call it
`sparse`. Naturally, dense graphs require more resources to search.

`Undirected` graph only has two way connections. `Directed` only have one way connections.

`Weighted` graphs have a weight per edge that represents the cost to traverse between the nodes.

`Strongly connected components` appear to be sub graphs connected together.

`Cyclic Graphs` have nodes that loop back around to themselves. In a circle.

**What is a graph?**

-   Collections of data represented by nodes and connections between those nodes

### parts of a graph

-   Node/Vertices - Represents objects in data set.
-   Edges - Connections between nodes; Can be bidirectional.
-   Weight - Cost to travel across an edge. This is in regard to what ever resources are used to travel across. (Optional Element)

### Types of graphs

-   Directed graph: can only move in one direction across edges
-   Undirected graph: Allows movement in both directions across edges
-   Cyclic graph: Edges allow you to revisit at least one node
-   Acyclic graph: Vertices can only be visited once.

## Written

### What is a graph??

-   Graphs can represent any kind of multi-way relational data.

### Directed and Undirected Graphs

**Directed and Undirected Graphs**
The nature of the relationship that is being represented is what determines if a directed or undirected graph should be used. If the relationship could be described as “one way”, then a directed graph makes the most sense. For example, representing the owing of money to others (debt) with a directed graph would make sense.

### Weighted graphs

`Weighted graphs` have values associated with the edges. We call the specific values assigned to each edge weights.

road. The higher the total weight of a route on the graph, the longer the trip is. The weights can help decide which particular route we should choose when comparing all routes.

We can further modify weights. For example, if you were building a graph to represent a map for bicycle routes, we could give roads with bad car traffic or very steep inclines unnaturally large weights. That way a routing algorithm would be unlikely to take them. (This is how Google Maps avoids freeways when you ask it for walking directions.)

_Note: [Djikstra’s Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) is a graph search variant that accounts for edge weights._

Directed Acyclic Graphs (DAGs)
A directed acyclic graph (DAG) is a directed graph with no cycles. In other words, we can order a DAG’s vertices linearly in such a way that every edge is directed from earlier to later in the sequence.

### Directed Acyclic Graphs (DAGs)

A **directed acyclic graph** (DAG) is a directed graph with no cycles. In other words, we can order a DAG’s vertices linearly in such a way that every edge is directed from earlier to later in the sequence.

It's also worth noting that git hub uses this kind of graph to track it's commit history and flow.

### Adjacency List

An object where keys are vertices and the values are all the connected nodes. These are not actually lists however, they are dictionaries. This makes retrieval and adding of a node constant time.

```python
class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},
                            "B": {"C", "D"},
                            "C": {"E"},
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }
```

This type of adjacency representation is ideal for any graph that will add and remove nodes more often.

### Adjacency Matrix

A two dimensional array where each row represents a vert and every element in that row confirms a connection of each other node.

```
   A B C D E F G
   _ _ _ _ _ _ _
A |0 1 0 0 0 0 1
B |0 0 0 1 0 1 0
C |1 0 0 1 0 0 0
D |1 1 1 0 0 0 0
E |0 1 0 1 0 1 0
F |0 1 0 1 0 1 0
G |0 0 0 0 1 1 1
```

One of the biggest advantages of matrix is they can show weight very easily. Weights can replace the 1's in the matrix.

## Trade offs between these two adjacency representations.

**Shorthand Property**

---

    V - Total number of Vertices
    E - Total number of Edges
    e - Average number of connections per vertex

### Space Complexity

**Adjacency Matrix**
_complexity:_ `O(V^2)` space

Consider a graph in which every vertex points to every other vertex. Her the number of edges will approach `V^2`. This means that weather you use a list or matrix, both will have comparable space complexity. That being said, sets and dictionaries are less space efficient than lists and so a matrix would be an optimal choice.
**Adjacency List**
_Complexity_: `O(V+E)` space

Consider a graph with 100 vertices and 1 connection. A matrix would still need to store a value for every null connection. This would be completely inefficient.

_Takeaway: The worst case storage of an adjacency list occurs when the graph is dense. In this case, a matrix and a list representation have the same complexity (`O(v^2)`). However for the general case,the list representation is usually more desirable. ALso, since finding a vertex's neighbors is a common task, and adjacency lists make this opperation easier, adjacency lists are most often used to represent graphs._

## Add Vertex

**Adjacency Matrix**
complexity: O(v) time

For an adjacency matrix, we would need to add a new value to the end of each existing row, then add a new row at the end.

```python
for v in self.edges:
  self.edges[v].append(0)
v.append([0] * len(self.edges + 1))
```

This is, of course, when there is allcated space left in the lists. If not, the time complexity becomes `O(V^2)`

**Adjacency List**
_complexity: `O(1)` time_

Adding a vertex is as simple as adding a new set to the dict of edges.

```python
self.vertices["H"] = set()
```

_Takeaway: Adding vertices is very inefficient for adjacency matrices but very efficient for adjacency lists._

## Removing Vertex

**Adjacency Matrix**
_complexity: `O(V^2)`_

Removing vertices is inefficient in both representations. In an matrix, we need to remove the removed vert's row, then remove that column from each other row. Removing an element from a list requires moving everything after that element over by one slot which takes an average of V/2 operations. Since we need to do that for every single row in our matrix, that results in a V^2 time complexity. We need to reduce the index of each vertex after our removed index by 1 as well which doesn't add to our quadratic complexity.

**Adjacency List**
_complexity: `O(V)`_

This simply requires us to look through each vertex an remove the vertex we are removing.

## Add Edge

**Adjacency Matrix**
_complexity: `O(1)`_

Pretty simple

```python
self.vertices[v1][v2] = 1
```

**Adjacency List**
_complexity: `O(1)`_

Pretty simple

```python
self.vertices[v1].add(v2)
```

Both are constant time operations

## Removing Edges

_complexity: `O(1)`_

Pretty simple

```python
self.vertices[v1][v2] = 0
```

**Adjacency List**
_complexity: `O(1)`_

Pretty simple

```python
self.vertices[v1].remove(v2)
```

Both are constant time operations

## Finding an Edge

_complexity: `O(1)`_

```python
return self.edges[v1][v2] > 0
```

**Adjacency List**
_complexity: `O(1)`_

Pretty simple

```python
return v2 in self.vertices[v1]
```

Both are constant time operations

## Get All Edges from Vertex

**Adjacency Matrix**
_complexity: `O(V)`_

In an adjacency matrix, this is complicated. You would need to iterate through the entire row and populate a list based on the results:

```python
v_edges = []
for v2 in self.edges[v]:
    if self.edges[v][v2] > 0:
        v_edges.append(v2)
return v_edges
```

**Adjacency List**
_complexity: `O(1)`_

With an adjacency list, this is as simple as returning the value from the vertex dictionary:

```python
return self.vertex[v]
```

_Takeaway: Fetching all edges is less efficient in an adjacency matrix than an adjacency list._

|            | space    | Add Vert | Remove Vert | Add Edge | Remove Edge | Find Edge | Get All Edges |
| ---------- | -------- | -------- | ----------- | -------- | ----------- | --------- | ------------- |
| **Matrix** | `O(V^2)` | `O(V)`   | `O(v^2)`    | `O(1)`   | `O(1)`      | `O(1)`    | `O(V)`        |
| **List**   | `O(V+E)` | `O(1)`   | `O(V)`      | `O(1)`   | `O(1)`      | `O(1)`    | `O(1)`        |

`Breadth First Traversal` and `Depth First Traversal` are the two main methods of traversing to every separate node.

## Graph Traversal

### BFS (Breadth first search)

This sorting algorithm explores the graph outward in rings of increasing distance from the starting vertex.

The algorithm never attempts to explore a vert it has already explored or is currently exploring.

The biggest difference in this algorithm from the next is the use of the `queue` rather than a `stack`

_Note: it’s important to know the distincition between a breadth-first search and a breadth-first traversal. A breadth-first traversal is when you visit each vertex in breadth-first order and do something during the traversal. A breadth-first search is when you search through vertexes in breadth-first order until you find the target vertex. A breadth-first search usually returns the shortest path from the starting vertex to the target vertex once the target is found._

### Aplications of BFS

-   Path-finding, Routing
-   Find neighbor node in a p2p network like BitTorrent
-   Web crawlers
-   Finding people n connections away on a social network
-   Find neighboring locations on a graph
-   Broadcasting in a network
-   Cycle detection in a graph
-   Finding Connected Components
-   Solving serval theoretical graph problems

### Coloring Vertexes

As we explore the graph, it is useful to color verts as we arrive at them and as we leave them behind as "already searched"

Unvisited verts are white, verts whose neighbors are being explored are gray, and verts with no unexplored neighbors are black.

## Keeping Track of What We Need to Explore

In a BFS, it's useful to track which nodes we need to follow up on. for example, in the diagram above, wehn we get to node 2, we know that we also need to explore nodes 3 and 4.

We can track that by adding neighbors to a queue.

### Pseudo-code for BFS

```python
BFS(graph, startVert):
    for v of graph.vertexes:
        v.color = white

    startVert.color = gray
        queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]  // Peek at head of the queue, but do not dequeue!

        for v of u.neighbors:
            if v.color == white:
                v.color = gray
                queue.enqueue(v)

        queue.dequeue()
        u.color = black
```

### DFS (Depth First Search)

Another method we can use when searching a graph is a depth first search (DFS). This searching algorithm “dives” “down” the graph as far as it can before backtracking and exploring another branch.

The algorithm never attempts to explore a vert it has already explored or is in the process of exploring.

### Applications of DFS

DFS is often the preferred method or exploring a graph if we want to ensure we visit every node in the graph. As an example, let’s say that we have a graph that represents all the friendships in the entire world. We want to find a path between two known people Andy and Sarah. If we used a depth-first search in this scenario we could end up extremely far away from Andy while still not finding a path to Sarah. Using a DFS, we will eventually find the path, but it won’t find the shortest path and it will also likely take a long time.

What `DFS` is **NOT** good at:

-   Finding Minimum Spanning Trees of weighted graphs
-   Path finding
-   Detecting cycles in graphs
-   Topological sorting, useful for scheduling sequences of dependent jobs
-   Solving and generating mazes

### Coloring Vertexes

Again, as we explore the graph, it is useful to color verts as we arrive at them and as we leave them behind as “already searched”.

Unvisited verts are white, verts whose neighbors are being explored are gray, and verts with no unexplored neighbors are black.

### Recursion

Due to the nature of the search, recursion is a good application for a search. Recursion is a good approach to help "remember" where we left off.

```python
explore(graph) {
    visit(this_vert);
    explore(remaining_graph);
}
```

### Pseudo-code for DFS

Let’s explore some pseudo-code that shows a basic implementation of a depth-first-search of a graph. Make sure you can read the pseudo-code and understand what each line is doing before moving on.

```python
DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black
```

# Graphs II

## Lecture

## TK

There are appropriate applications for both breadth first and depth first searching. For instance if your node is at the bottom of the graph, a depth first search is what is needed.

### Applications of a DFS

-   Finding [Minimum Spanning Trees](https://en.wikipedia.org/wiki/Minimum_spanning_tree) of weighted graphs
-   Path finding
-   Detection cycles in graphs
-   [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
-   Solving and generating mazes

# Graphs III

## Lecture

So many things can be represented in a graph

## Earliest Ancestor problem

Here are the three steps to almost all graph problems

1. Describe in terms of graphs
    1. Nodes: Parents, children
    2. Edges: if they are parent child
2. Build our graph
    1. Build a graph class
    2. Don't use an adjacency list or matrix, just a `get_neighbors()`
3. Choose a graph algorithm
    1. Traversal or search?
    2. Breadth or depth?

_Note: if passing in a list of tuples, you can use two variables in the for loop definition and use them in logic_

```python
for i, j in list_of_tuples:
    print(f"i:{i}, j:{j}")
```

## Objectives

### Connected components

Groups of connected nodes. There can be several groups of nodes that aren't actually connected to each other in the same graph. These are connected components.

When a graph has groups of disconnected components it's know as `disjointed`
**Uses**

-   finding related data
-   social networks and their group of friends

Another way to search a graph for connected components is by coloring all nodes that are connected to one node, grey. Once a node has been searched, mark it black. If the next node is grey, we know its already been accounted for in a component and can now be marked black.

### Randomness

#### What is randomness

```
Randomness is the lack of pattern or predictability in events. A random sequence of events, symbols or steps has no order and does not follow an intelligible pattern or combination.
```

Coinflips are inharently random. If you flip a coin 9 times and get all heads, the chances of you getting heads a 10th time is 50%. Rock, paper, scissors is not random at all how ever. Humans are very bad at creating random sequences. These are due to personal bias and make the choices more predictable.

Turns out, computers are very good at this form of randomness.

Here are lists of 10 random numbers between 1 and 10, generated by a computer:

```python
>>> import random
>>> [random.randint(1,10) for i in range(0,10)]
[6, 2, 2, 6, 6, 1, 7, 9, 9, 4]
>>> [random.randint(1,10) for i in range(0,10)]
[1, 3, 2, 8, 9, 3, 1, 9, 4, 8]
>>> [random.randint(1,10) for i in range(0,10)]
[6, 4, 9, 4, 5, 5, 4, 7, 3, 7]
>>> [random.randint(1,10) for i in range(0,10)]
[6, 6, 1, 1, 2, 8, 9, 2, 3, 10]
>>> [random.randint(1,10) for i in range(0,10)]
[8, 1, 9, 5, 10, 4, 6, 2, 10, 7]
>>> [random.randint(1,10) for i in range(0,10)]
[8, 4, 1, 1, 8, 6, 9, 4, 1, 9]
>>> [random.randint(1,10) for i in range(0,10)]
[2, 1, 2, 2, 2, 10, 1, 1, 1, 3]
>>> [random.randint(1,10) for i in range(0,10)]
[1, 6, 1, 6, 6, 4, 9, 9, 7, 5]
>>> [random.randint(1,10) for i in range(0,10)]
[4, 4, 7, 6, 6, 5, 2, 8, 3, 7]
>>> [random.randint(1,10) for i in range(0,10)]
[8, 1, 4, 3, 4, 3, 5, 4, 4, 9]
```

Looking at these results, you may think that the lists seem LESS random. After all, the first list contains three 6s, two 2s, two 9s, and no 3s, 5s, 8s or 10s. The seventh list is 80% 1s and 2s. Is this REALLY random?

The short answer is yes. Small random sample sizes will show statistical variation. The larger the sample size though, the closer the result will skew toward the expected values. This is known as the [Law of Large Numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers). Consider the following function:

```python
import random
def random_counts(n):
    """
    Generates n random numbers between 1-10 and counts how many of each there are.
    """
    counts = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    nums = [random.randint(1,10) for i in range(1,n)]
    for i in nums:
        counts[i] += 1
    return counts
```

This will generate a list of n random numbers then count how many of each there are. Let's try running it for different values of n.

```python
>>> random_counts(10)
{1: 0, 2: 2, 3: 0, 4: 1, 5: 2, 6: 2, 7: 2, 8: 0, 9: 0, 10: 0}
>>> random_counts(10)
{1: 2, 2: 0, 3: 3, 4: 0, 5: 2, 6: 1, 7: 0, 8: 0, 9: 1, 10: 0}
>>> random_counts(10)
{1: 1, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 2, 8: 1, 9: 2, 10: 1}
>>> random_counts(100)
{1: 9, 2: 6, 3: 10, 4: 14, 5: 14, 6: 8, 7: 7, 8: 11, 9: 10, 10: 10}
>>> random_counts(100)
{1: 6, 2: 7, 3: 13, 4: 11, 5: 16, 6: 9, 7: 5, 8: 13, 9: 8, 10: 11}
>>> random_counts(100)
{1: 11, 2: 11, 3: 8, 4: 10, 5: 12, 6: 7, 7: 8, 8: 13, 9: 10, 10: 9}
>>> random_counts(1000)
{1: 110, 2: 106, 3: 98, 4: 96, 5: 98, 6: 96, 7: 90, 8: 98, 9: 111, 10: 96}
>>> random_counts(1000)
{1: 102, 2: 87, 3: 103, 4: 101, 5: 95, 6: 100, 7: 107, 8: 94, 9: 94, 10: 116}
>>> random_counts(1000)
{1: 107, 2: 106, 3: 119, 4: 95, 5: 99, 6: 96, 7: 94, 8: 92, 9: 91, 10: 100}
>>> random_counts(10000)
{1: 971, 2: 1015, 3: 1024, 4: 1004, 5: 956, 6: 952, 7: 1054, 8: 978, 9: 1019, 10: 1026}
>>> random_counts(10000)
{1: 1024, 2: 996, 3: 970, 4: 1029, 5: 1014, 6: 997, 7: 977, 8: 936, 9: 1030, 10: 1026}
>>> random_counts(10000)
{1: 1086, 2: 968, 3: 1010, 4: 1019, 5: 973, 6: 966, 7: 1004, 8: 1006, 9: 996, 10: 971}
>>> random_counts(1000000)
{1: 100270, 2: 100035, 3: 100127, 4: 99814, 5: 99748, 6: 100162, 7: 99851, 8: 99706, 9: 100104, 10: 100182}
>>> random_counts(1000000)
{1: 100784, 2: 100029, 3: 100287, 4: 99821, 5: 99933, 6: 100350, 7: 100419, 8: 99304, 9: 99329, 10: 99743}
>>> random_counts(1000000)
{1: 100170, 2: 100205, 3: 99644, 4: 99702, 5: 99874, 6: 100316, 7: 99996, 8: 99864, 9: 99968, 10: 100260}
```

Statistically, you would expect each number to show up exactly 10% of the time. As you can see, the larger the n, the closer the results get to that expected percentage. This is how casinos work: they may lose a large amount of money on a single roll of the roulette wheel but over thousands of spins, the house always comes out ahead in the long run.

Computers are quite good at producing statistical randomness like this. But is it actually random? Turns out, the answer is no.

### What is pseudorandomness?

Computers are machines that take in some input, run a set of operations on that input, then return an output. These operations are generally **deterministic**, which means it will always produce the same output from an identical set of inputs.

There is no way to produce a truly random numbers with a computer.

Psudorandom numbers will always produce the same output for any seed that is passed in.

### Shuffling an array

One good method is the [Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
