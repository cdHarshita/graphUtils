import unittest
from graphUtils.algorithms import dijkstra, bellman_ford, floyd_warshall, topo_sort


class TestGraphAlgorithms(unittest.TestCase):
    def setUp(self):
        # Example graph used for most tests
        self.graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }

    def test_dijkstra_shortest_path(self):
        # Testing Dijkstra's algorithm
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
        self.assertEqual(dijkstra(self.graph, 'A'), expected)

    def test_bellman_ford_shortest_path(self):
        # Testing Bellman-Ford algorithm
        expected = {'A': 0, 'B': 1, 'C': 3, 'D': 4}
        self.assertEqual(bellman_ford(self.graph, 'A'), expected)

    def test_bellman_ford_negative_cycle(self):
        # Graph with a negative weight cycle
        graph_with_cycle = {
            'A': {'B': 1},
            'B': {'C': 2},
            'C': {'A': -4}
        }
        with self.assertRaises(ValueError, msg="Graph contains a negative-weight cycle"):
            bellman_ford(graph_with_cycle, 'A')

    def test_floyd_warshall_shortest_paths(self):
        # Testing Floyd-Warshall algorithm
        result = floyd_warshall(self.graph)
        expected = {
            'A': {'A': 0, 'B': 1, 'C': 3, 'D': 4},
            'B': {'A': float('inf'), 'B': 0, 'C': 2, 'D': 3},
            'C': {'A': float('inf'), 'B': float('inf'), 'C': 0, 'D': 1},
            'D': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0},
        }
        self.assertEqual(result, expected)

    def test_topo_sort_valid_order(self):
        # Testing Topological Sorting
        graph = {
            'A': ['C'],
            'B': ['C', 'D'],
            'C': ['E'],
            'D': ['F'],
            'E': ['H'],
            'F': ['G'],
            'G': [],
            'H': []
        }
        sorted_order = topo_sort(graph)

        # Ensure the order is valid
        visited = set()
        for node in sorted_order:
            visited.add(node)
            for neighbor in graph.get(node, []):
                self.assertNotIn(neighbor, visited)

    def test_topo_sort_cycle_detection(self):
        # Graph with a cycle
        cyclic_graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        with self.assertRaises(ValueError, msg="Graph has at least one cycle"):
            topo_sort(cyclic_graph)


if __name__ == "__main__":
    unittest.main()
