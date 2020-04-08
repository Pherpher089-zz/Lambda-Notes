# Training Kit: Graphs

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
