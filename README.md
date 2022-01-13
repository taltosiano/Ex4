# Ex4


## final project on OOP course - our pokemon game!

![ppkemonnn](https://user-images.githubusercontent.com/94299489/148839230-246413c2-f5b0-4d7a-92f5-df1452c42756.png)

### about the assignment
In this task we were asked to create a Pokemon game. The intention is to create Pokemons that will be scattered on a directed graph that we have 
already built in Ex3 , and to create agents that should catch as many Pokemon as possible at a minimum track length to perform this action.

## our project classes:
we use the previous graph implementation on Ex3. and we add some other classes to based the game.

| classe |  Description | 
| ------------ | ------------ | 
|  pokemon |  Represents the players | 
|  agent |  Represents the pokemon | 
| MyGame | return a dictionary of all the nodes in the Graph |
|  student code | Represents the GUI class |  
| client | Represents the server | 
| Node | represents the set of operations applicable on a node (vertex) in a (directional) weighted graph | 
| Edge | represents the set of operations applicable on a directional edge(src,dest,weight) in a (directional) weighted graph | 
| DiGraph  | represents a Directional Weighted Graph with all his elements(Nodes,Edeges)and including many functions that updates his elements|  
| GraphAlgo |  represents a Directed (positive) Weighted Graph Theory Algorithms and including many algorithms | 

## some main function in our classes

| function |  Description | 
| ------------ | ------------ | 
|  load_agents |  load list of agents from the Agant class | 
|  load_pokemons |  load list of pokemos from the Pokemon class | 
| theClosePokemon | looking for the closests pokemons to each agant |
|  theNextNode | find the next node to go to |  



## HOW TO RUN THE GAME:
the user should download the project to your own computer. In the terminal command line you should write: 
java -jar Ex4_Server_v0.0.jar 0  ( “0” represents the case between [0-15])

### Computer specifications:
Computer operating system is macOS, 256 SSD Apple M1 Chip with 8‑Core CPU and 7‑Core GPU and 16‑core Neural Engine 8GB unified memory, 16 GB

## uml diagram
![uml444](https://user-images.githubusercontent.com/94299489/149219967-479aaaa9-092f-4e6f-a095-1b8eb63acd2c.jpeg)



## Authors
**Tal tosiano-208846600**  
**Moran shalev-316220938**
