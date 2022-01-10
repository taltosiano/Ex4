# Ex4


## final project - our pokemon game!

![ppkemonnn](https://user-images.githubusercontent.com/94299489/148839230-246413c2-f5b0-4d7a-92f5-df1452c42756.png)

        
## our project classes:
we use the previous graph implementation on Ex3. and we add some other classes to based the game.

### pokemon
represents the set of operations applicable on a  node (vertex) in a (directional)     
 weighted graph.
Every node has data (id,pos) that helps us to representing the graph in the most accurate way. 

### agent
represents the set of operations applicable on a directional  edge(src,dest,weight)  in a (directional) weighted graph.

### MyGame
represents a Directional Weighted Graph with all his elements(Nodes,Edeges)and   including many functions that updates his elements.

### student code

### client

|function  |  Description |  output |
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

## HOW TO RUN THE GAME:
the user should download the project to your own computer. In the terminal command line you should write: 
java -jar Ex4_Server_v0.0.jar 0  ( “0” represents the case between [0-15])


### link to wiki 
 WIKI ----> https://github.com/taltosiano/Ex3.wiki.git

### Computer specifications:
Computer operating system is macOS, 256 SSD Apple M1 Chip with 8‑Core CPU and 7‑Core GPU and 16‑core Neural Engine 8GB unified memory, 16 GB

## example of check1 print Graph:

## example of check3 print Graph:


## Authors
**Tal tosiano-208846600**  
**Moran shalev-316220938**
