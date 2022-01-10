# Ex4


## final project - our pokemon game!

![ppkemonnn](https://user-images.githubusercontent.com/94299489/148839230-246413c2-f5b0-4d7a-92f5-df1452c42756.png)


        
## The process of creating the project:
We built a system that builds a weighted graph by the classes:

### Node
represents the set of operations applicable on a  node (vertex) in a (directional)     
 weighted graph.
Every node has data (id,pos) that helps us to representing the graph in the most accurate way. 

### Edge
represents the set of operations applicable on a directional  edge(src,dest,weight)  in a (directional) weighted graph.

### DiGraph
represents a Directional Weighted Graph with all his elements(Nodes,Edeges)and   including many functions that updates his elements.

|function in DiGraph |  Description |  output |
| ------------ | ------------ | ------------ | 
|  def v_size() |  returns the number of nodes in the graph |  int |
|  def e_size() |  returns the number of edges in the graph |   int |
| def get_all_v() | return a dictionary of all the nodes in the Graph | dict  |
| def all_in_edges_of_node(id1: int) | return a dictionary of all the nodes connected to (into) id1 |  dict |
| def all_out_edges_of_node(id1: int) | return a dictionary of all the nodes connected from id1 |   dict |
| def get_mc() | returns the current version of this graph, Mode Count - for testing changes in the graph |   int |
| def add_edge(self, id1: int, id2: int, weight: float) | Adds an edge to the graph  | bool |
| def add_node(self, node_id: int, pos: tuple = None)  |   Adds a node to the graph  |  bool |
| def remove_node(self, node_id: int) |   Removes a node from the graph  | bool  |
| def remove_edge(self, node_id1: int, node_id2: int)|  Removes an edge from the graph   |  bool  | 


### GraphAlgo
represents a Directed (positive) Weighted Graph Theory Algorithms and including many algorithms.
for the tsp function (Travelling salesman problem) we use the "tarjan" algoritem to solve  this problem.
for the shortestPathDist function we use the dijkstra's algorithm to solve this problem.

|function in GraphAlgo |  Description |  output |
| ------------ | ------------ | ------------ | 
|  def get_graph() |  return the directed graph on which the algorithm works on. | GraphInterface |
|  def shortest_path(self, id1: int, id2: int) |  check the shortest path from node id1 to node id2 using Dijkstra's Algorithm |   Float, List |
| def load_from_json(self, file_name: str) | Loads a graph from a Json file | bool  |
| def save_to_json(self, file_name: str) | Saves the graph in Json format to a file |  bool |
| (self, node_lst: List[int]) | Finds the shortest path that visits all the nodes in the list |   dict |
| centerPoint() | Finds the node that has the shortest distance to it's farthest node |   int |
| plot_graph() | plots the graph. | None |

### Performance analysis of our algorithms and comparing to our code in Ex2: 
 in WIKI ----> https://github.com/taltosiano/Ex3.wiki.git

### Computer specifications:
Computer operating system is macOS, 256 SSD Apple M1 Chip with 8‑Core CPU and 7‑Core GPU and 16‑core Neural Engine 8GB unified memory, 16 GB

## example of check1 print Graph:

## example of check3 print Graph:


## Authors
**Tal tosiano-208846600**  
**Moran shalev-316220938**
