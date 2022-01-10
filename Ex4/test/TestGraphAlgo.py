import os
import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def init_graph1() -> GraphAlgo:
    g = GraphAlgo()
    g.load_from_json("../data/A1.json")
    return g


def init_graph2() -> GraphAlgo:
    g = GraphAlgo()
    g.load_from_json("../data/A2.json")
    return g


def init_graph3() -> GraphAlgo:
    g = GraphAlgo()
    g.load_from_json("../data/A3.json")
    return g


class TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        g = init_graph1()
        self.assertEqual(g.get_graph(), g.graph)
        self.assertEqual(17, g.get_graph().v_size())
        self.assertEqual(36, g.get_graph().e_size())

    def test_load_from_json(self):
        g = GraphAlgo()
        g.load_from_json("../data/T0.json")
        self.assertEqual(4, g.graph.v_size())

    def test_save_to_json(self):
        g = init_graph1()
        g.save_to_json("myGraphTest")
        self.assertTrue(True, os.path.isfile("myGraphTest.json"))

    def test_shortest_path(self):
        g = init_graph1()
        short1 = g.shortest_path(1, 5)
        self.assertEqual(5.091901160431474, short1[0])
        self.assertEqual([1, 2, 6, 5], short1[1])
        short2 = g.shortest_path(0, 4)
        self.assertEqual(5.350731924801653, short2[0])
        self.assertEqual([0, 1, 2, 3, 4], short2[1])

    def test_tsp(self):
        g = init_graph2()
        g.graph.add_edge(1, 2, 3)
        g.graph.add_edge(1, 3, 4)
        g.graph.add_edge(2, 3, 2)

        tsp1 = [1, 2, 3]
        self.assertEqual([1, 2, 3], g.TSP(tsp1)[0])
        tsp2 = [1, 2, 3]
        self.assertEqual(2.8647559158521916, g.TSP(tsp2)[1])

    def test_center_point(self):
        g = init_graph3()
        self.assertEqual(8.858254086057299, g.centerPoint()[1])
        self.assertEqual(0, g.centerPoint()[0])

    def test_plot_graph(self):
        g = init_graph1()
        g.plot_graph()
        # g = init_graph2()
        # g.plot_graph()
