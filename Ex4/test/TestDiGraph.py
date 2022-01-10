import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def init_graph1() -> DiGraph:
    g = GraphAlgo()
    g.load_from_json("../data/A1.json")
    return g.graph


def init_graph2() -> DiGraph:
    g = GraphAlgo()
    g.load_from_json("../data/A2.json")
    return g.graph


def init_graph3() -> DiGraph:
    g = GraphAlgo()
    g.load_from_json("../data/A3.json")
    return g.graph


class DiGraph(unittest.TestCase):

    def test_v_size(self):
        g = init_graph1()
        self.assertEqual(17, g.v_size())
        g.remove_node(1)
        self.assertEqual(16, g.v_size())
        g.add_node(17, tuple([1, 2, 3]))
        self.assertEqual(17, g.v_size())

    def test_e_size(self):
        g = init_graph2()
        self.assertEqual(80, g.e_size())
        g.remove_edge(7, 8)
        self.assertEqual(79, g.e_size())

    def test_get_all_v(self):
        g = init_graph1()
        keys = g.get_all_v().keys()
        self.assertEqual(17, len(keys))

    def test_all_in_edges_of_node(self):
        g = init_graph2()
        keys1 = g.all_in_edges_of_node(2).keys()
        self.assertEqual(3, len(keys1))
        g.remove_node(1)
        keys2 = g.all_in_edges_of_node(2).keys()
        self.assertEqual(2, len(keys2))

    def test_all_out_edges_of_node(self):
        g = init_graph1()
        keys1 = g.all_out_edges_of_node(3).keys()
        self.assertEqual(2, len(keys1))
        g.remove_node(1)
        keys2 = g.all_in_edges_of_node(2).keys()
        self.assertEqual(2, len(keys2))

    def test_get_mc(self):
        g = init_graph1()
        self.assertEqual(53, g.get_mc())
        g.remove_node(4)
        g.add_node(1, tuple([2, 3, 4]))
        g.remove_edge(1, 2)
        self.assertEqual(59, g.get_mc())

    def test_add_edge(self):
        g = init_graph1()
        self.assertEqual(False, g.add_edge(0, 1, 2))
        self.assertEqual(36, g.e_size())
        g.add_edge(6, 7, 8)
        g.add_edge(10, 7, 5)
        self.assertEqual(37, g.e_size())

    def test_add_node(self):
        g = init_graph1()
        self.assertEqual(17, g.v_size())
        g.add_node(0)
        g.add_node(1)
        g.add_node(18)
        self.assertEqual(18, g.v_size())
        g = init_graph3()
        self.assertEqual(49, g.v_size())
        g.add_node(50)
        g.add_node(51)
        g.add_node(52)
        self.assertEqual(52, g.v_size())

    def test_remove_node(self):
        g = init_graph2()
        self.assertEqual(31, g.v_size())
        self.assertEqual(80, g.e_size())
        g.remove_node(0)
        self.assertEqual(74, g.e_size())
        self.assertEqual(30, g.v_size())
        g.remove_node(34)
        self.assertEqual(30, g.v_size())

    def test_remove_edge(self):
        g = init_graph3()
        self.assertEqual(185, g.get_mc())
        self.assertEqual(136, g.e_size())
        g.remove_edge(0, 3)
        g.remove_edge(0, 1)
        self.assertEqual(186, g.get_mc())
        self.assertEqual(135, g.e_size())


if __name__ == '_main_':
    unittest.main()
