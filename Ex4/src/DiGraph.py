# from plistlib import Dict

from src.GraphInterface import GraphInterface
from src.Edge import Edge
from src.Node import Node
from typing import Dict


class DiGraph(GraphInterface):
    def __init__(self):
        self.__nodes: Dict[int, Node] = dict()
        self.__edges: Dict[int, Dict[int, Edge]] = dict()
        self.__nodesCounter = 0
        self.__mc = 0
        self.__edgeCounter = 0

    # return the number of nodes in the graph
    def v_size(self) -> int:
        return len(self.__nodes)

    # return the number of edges in the graph
    def e_size(self) -> int:
        return self.__edgeCounter

    # returns a dict of all the vertexs in the graph
    def get_all_v(self) -> dict:
        return self.__nodes

    # returns a dict of all the edges in the graph
    def get_all_e(self) -> dict:
        return self.__edges

    # returns a dict of all in edges of the node-id1:that id1 is the dest of them
    def all_in_edges_of_node(self, id1: int) -> dict:
        edgesInGraph: Dict[int, Edge] = dict()
        for i in self.__nodes:
            if id1 in self.__edges.get(i):
                edgesInGraph.__setitem__(i, self.__edges.get(i)[id1])
                self.__nodes.get(id1).edges_in += 1
        return edgesInGraph

    # returns a dict of all in edges of the node-id1:that id1 is the src of them
    def all_out_edges_of_node(self, id1: int) -> dict:
        edgesOutGraph: Dict[int, Edge] = dict()
        if id1 in self.__nodes:
            for i in self.__edges.get(id1):
                edgesOutGraph.__setitem__(i, self.__edges.get(id1)[i])
                self.__nodes.get(id1).edges_out += 1
        return edgesOutGraph

    # Returns the current version of this graph-in every function -on every change in the graph state - the MC should
    # be increased
    def get_mc(self) -> int:
        return self.__mc

    # adding edge from id1 to-->id2 with weight of the edge
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (id1 not in self.__nodes) or (id2 not in self.__nodes) or (id2 in self.__edges.get(id1)) or (id1 == id2):
            return False
        else:
            e = Edge(id1, id2, weight)
            self.__edges.get(id1).__setitem__(id2, e)
            self.__edgeCounter += 1
            self.__mc += 1
            self.__nodes.get(id1).edges_out += 1
            self.__nodes.get(id2).edges_in += 1
            return True

    # adding node with id and pos
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.__nodes:
            return False
        else:
            n = Node(node_id, pos)
            self.__nodes.__setitem__(node_id, n)
            self.__edges.__setitem__(node_id, dict())
            self.__mc += 1
            return True

    # removes the node with 'node id' key
    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.__nodes:  # if the node doesn't exist
            return False
        else:
            sizeEdgeIn = self.all_in_edges_of_node(node_id)
            sizeEdgeOut = self.all_out_edges_of_node(node_id)
            self.__edgeCounter -= len(sizeEdgeIn)
            self.__edgeCounter -= len(sizeEdgeOut)
            self.__mc += len(sizeEdgeOut) + len(sizeEdgeIn)
            for x in sizeEdgeIn:
                self.__edges.get(x).pop(node_id)
            self.__mc += 1
            self.__nodes.pop(node_id)
            return True

    # removes the edge with 'node id1'src and 'node id2' dest
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 == node_id2) or (node_id1 not in self.__nodes) or (node_id2 not in self.__nodes) or (
                node_id2 not in self.__edges.get(node_id1)):
            return False
        else:
            self.__mc += 1
            self.__edgeCounter -= 1
            self.__edges.get(node_id1).pop(node_id2)
            self.__nodes.get(node_id1).edges_out -= 1
            self.__nodes.get(node_id2).edges_in -= 1
            return True

    # get the node with 'node' key
    def get_node(self, node: int) -> Node:
        if self.__nodes.__contains__(node):
            return self.__nodes.get(node)

    def __repr__(self) -> str:
        return "Graph: |V|=%s , |E|=%s" % (self.__nodes.__len__(), self.__edgeCounter)
