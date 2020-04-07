# Training Kit: Graphs

## Video

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
