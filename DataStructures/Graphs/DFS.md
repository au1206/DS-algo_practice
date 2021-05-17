The Depth First Search (DFS) is the most
fundamental search algorithm used to explore
nodes and edges of a graph. It runs with a
time complexity of O(V+E) and is often used as
a building block in other algorithms.

By itself the DFS isn’t all that useful, but
when augmented to perform other tasks such as
count connected components, determine
connectivity, or find bridges/articulation
points then DFS really shines.

a DFS plunges depth first
into a graph without regard for which edge it
takes next until it cannot go any further at
which point it backtracks and continues.'


PSEUDO CODE
```
# Global or class scope variables
n = number of nodes in the graph
g = adjacency list representing graph
visited = [false, …, false] # size n
function dfs(at):
    if visited[at]: 
        return
    visited[at] = true

    neighbours = graph[at]
    for next in neighbours:
        dfs(next)
        
# Start DFS at node zero
start_node = 0
dfs(start_node)
```


Connected Components
Sometimes a graph is split into multiple
components. It’s useful to be able to
identify and count these components.

Assign an integer value to each group to
be able to tell them apart.

We can use a DFS to identify components.
First, make sure all the nodes are labeled
from [0, n) where n is the number of nodes.

Algorithm: Start a DFS at every node (except if
it’s already been visited) and mark all reachable
nodes as being part of the same component.

```
# Global or class scope variables
n = number of nodes in the graph
g = adjacency list representing graph
count = 0
components = empty integer array # size n
visited = [false, …, false] # size n
function findComponents():

for (i = 0; i < n; i++):
    if !visited[i]:
        count++
        dfs(i)
    return (count, components)

function dfs(at):
    visited[at] = true
    components[at] = count
    for (next : g[at]):
        if !visited[next]:
            dfs(next)
```