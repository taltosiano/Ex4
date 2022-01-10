import asyncio
import heapq
import json
import math
import queue
import sys
from asyncio import PriorityQueue
import random
from typing import List

from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.Node import Node
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    def __init__(self):
        self.graph = DiGraph()

    # gets the Digraph of graphAlgo
    def get_graph(self) -> GraphInterface:
        return self.graph

    # load from json file
    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            with open(file_name, "r") as file:
                graphLoad = json.load(file)
                for n in graphLoad["Nodes"]:
                    if "pos" in n:
                        posList = n["pos"].split(',')
                        thisTuple = (posList[0], posList[1], posList[2])
                        graph.add_node(n["id"], thisTuple)
                    else:  # if this is "T0.json"-without pos
                        graph.add_node(n["id"])
                for e in graphLoad["Edges"]:
                    graph.add_edge(e["src"], e["dest"], e["w"])
            self.graph = graph
            return True
        except Exception as e:
            print(e)
            return False

    # save the json file
    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as f:  # Open a file for writing
                f.write(repr(self.graph))
                return True
        except:
            return False

    # calculate the shortest path from src=id1 to dest=id2
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return math.inf, []
        if id1 is id2:  # if src=dest
            return 0, [id1]
            # init all variables in node
        self.__init_all_vertexs()
        q = []
        srcNode = self.graph.get_node(id1)  # the src node
        srcNode.set_weight(0)
        heapq.heappush(q, (srcNode.get_weight(), srcNode))

        while q:
            (d, vertex) = heapq.heappop(q)
            for edge in self.graph.all_out_edges_of_node(vertex.get_id()).values():
                u = self.graph.get_node(edge.get_dst())
                dist = edge.get_weight() + d
                if dist < u.get_weight():
                    u.set_weight(dist)
                    u.set_info(str(vertex.get_id()))
                    heapq.heappush(q, (u.get_weight(), u))

        path = []
        destNode = self.graph.get_node(id2)
        if destNode.get_weight() is math.inf:
            return math.inf, []
        path.append(destNode.get_id())
        destInfo = destNode.get_info()
        while destInfo != "-1":
            node = self.graph.get_node(int(destInfo))
            path.insert(0, node.get_id())
            destInfo = node.get_info()
        return destNode.get_weight(), path

    # Initialize all the nodes as INFINITE
    def __init_all_vertexs(self):
        for node in self.graph.get_all_v().values():
            node.set_weight(math.inf)
            node.set_tag(0)
            node.set_info("-1")

    # Finds the shortest path that visits all the nodes in the list
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        nodes = []
        tsp = []
        dist = 0
        for i in node_lst:
            if self.graph.all_out_edges_of_node(i) is None or self.graph.get_node(i) is None:
                return None
            else:
                nodes.append(self.graph.get_node(i).get_id())
        for node1 in nodes:
            path = self.shortest_path(nodes[0], nodes[1])  # contain the path and the dist of every node in nodes
            tsp += path[1]  # add the path
            dist += path[0]  # add the dist
            tsp.pop()
            for node2 in nodes:
                if node2 in tsp:  # if node2 is already exist in tsp list
                    nodes.remove(node2)
        tsp.append(nodes.pop())
        return tsp, dist

    # return the center node of the graphAlgo-the node that has the shortest distance to it's farthest node
    def centerPoint(self) -> (int, float):
        curr = 0
        centerN = None
        minimalMaxDist = sys.maxsize
        if self.graph.v_size() == 1:
            return self.graph.get_node(self.graph.get_all_v().get(0)).get_id(), 0  # if there is only one node

        for i in range(self.graph.v_size()):
            for j in range(self.graph.v_size()):
                dist = self.shortest_path(i, j)[0]
                if dist == math.inf:
                    curr = float('inf')
                if curr < dist:
                    curr = dist  # the minimum dist

            if curr == float('inf'):
                return None, float('inf')
            if curr < minimalMaxDist:
                minimalMaxDist = curr
                centerN = self.graph.get_node(i)

        return centerN.get_id(), minimalMaxDist

    # plots the graphAlgo
    def plot_graph(self) -> None:
        plt.title("My Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        for key in self.graph.get_all_v().keys():
            if self.graph.get_node(key).get_pos() is None:  # if the Nodes in graphAlgo don't have pos
                x = random.uniform(0.0, 1000)
                y = random.uniform(0.0, 1000)
                self.graph.get_node(key).set_pos(tuple([x, y, 0.0]))
            plt.plot(self.graph.get_node(key).get_pos()[0], self.graph.get_node(key).get_pos()[1], ".", markersize=10,
                     color="blue")
            plt.text(self.graph.get_node(key).get_pos()[0], self.graph.get_node(key).get_pos()[1], str(key),
                     color="red", fontsize=10)

        for src in self.graph.get_all_v().keys():
            for dest in self.graph.all_out_edges_of_node(src).keys():
                xy = (self.graph.get_node(src).get_pos()[0], self.graph.get_node(src).get_pos()[1])
                xytext = (self.graph.get_node(dest).get_pos()[0], self.graph.get_node(dest).get_pos()[1])
                plt.annotate("", xy, xytext, arrowprops=dict(arrowstyle="<-"))
        plt.show()
