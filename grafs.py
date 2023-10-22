class Graf():
    def __init__(self, adj_list:dict):
        self.adj_list = adj_list

    def adj_matrix(self) -> list:
        """
        Generates an adjacency matrix based on the adjacency list.

        Returns:
            list: The adjacency matrix.
        """
        adj_list = self.adj_list

        ret_matrix = [['*' for i in range(len(adj_list) + 1)] for _ in range(len(adj_list) + 1)]

        for i, key in enumerate(adj_list.keys()):
            ret_matrix[0][i + 1] = key
            ret_matrix[i + 1][0] = key
        for i in range(1, len(adj_list) + 1):
            for j in range(1, len(adj_list) + 1):
                try:
                    ret_matrix[i][j] = adj_list[ret_matrix[j][0]][ret_matrix[0][i]]
                except:
                    ret_matrix[i][j] = '*'
        return ret_matrix
    
    def adj_matrix_to_adj_list(matrix: list):
        """
        Generates a dictionary representation of an adjacency list from an adjacency matrix.

        Args:
            matrix (list): A 2D list representing an adjacency matrix.

        Returns:
            Graf: An instance of the Graf class representing the generated adjacency list.

        """
        adj_list = {}
        keys = matrix[0][1:]
        for i in range(1, len(matrix)):
            adj_list[keys[i - 1]] = {}
            for j in range(1, len(matrix)):
                if matrix[i][j] != '*':
                    adj_list[keys[i - 1]][keys[j - 1]] = matrix[i][j]
        return Graf(adj_list)

    def dijkstras(self, start: str) -> dict:
        """
        Calculates the shortest path from a given start node to all other nodes using Dijkstra's algorithm.

        Parameters:
            start (str): The start node.

        Returns:
            dict: A dictionary mapping each node to its shortest distance from the start node.
        """
        adj_list = self.adj_list
        ret_dict = {start: 0, **{key: float('inf') for key in adj_list}}
        ret_dict[start] = 0
        visited = []
        cur_node = start
        while len(visited) < len(adj_list):
            for next_node in adj_list[cur_node]:
                if ret_dict[next_node] > ret_dict[cur_node] + adj_list[cur_node][next_node]:
                    ret_dict[next_node] = ret_dict[cur_node] + adj_list[cur_node][next_node]
            visited.append(cur_node)
            if len(visited) == len(adj_list):
                break
            cur_node = min(adj_list[cur_node].keys() - set(visited), key=lambda x: ret_dict[x])
        return ret_dict
    
    def dfs(self, start: str, target: str) -> list:
        """
        Performs a depth-first search (DFS) on the graph starting from the given `start` node and searching for the `target` node.
        
        Parameters:
            start (str): The starting node for the DFS traversal.
            target (str): The target node that we are searching for.
        
        Returns:
            list: The path from the `start` node to the `target` node, if it exists. Otherwise, an empty list is returned.
        """
        
        adj_list = self.adj_list
        def dfs_helper(node: str, target: str, visited: list) -> list:
            """
            Perform a depth-first search (DFS) starting from the given node to find a path to the target node.

            Args:
                node (str): The starting node for the DFS.
                target (str): The target node to find a path to.
                visited (list): A list of nodes that have already been visited during the DFS.

            Returns:
                list: A list of nodes representing the path from the starting node to the target node. If no path is found, an empty list is returned.
            """
            visited.append(node)
            if node == target:
                return [node]
            else:
                for cur_node in adj_list[node].keys() - visited:
                    ret = dfs_helper(cur_node, target, visited)
                    if ret:
                        return ret + [node]
                return []
        visited = []
        return dfs_helper(start, target, visited)
    
    def bfs(self, start: str, target: str) -> bool:
        """
        Performs a breadth-first search (BFS) on a graph starting from a given node and checks if a target node is reachable.

        Parameters:
            start (str): The starting node for the BFS.
            target (str): The target node to be reached.

        Returns:
            bool: True if the target node is reachable from the starting node, False otherwise.
        """
        queue = [start]
        visited = []
        while queue:
            cur_node = queue.pop(0)
            visited.append(cur_node)
            if cur_node == target:
                return True
            for next_node in self.adj_list[cur_node].keys() - visited:
                queue.append(next_node)
        return False

    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        :return: The string representation of the object.
        :rtype: str
        """
        return repr(self.adj_list)
    
    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: The string representation of the adjacency list.
        """
        return str(self.adj_list)

# g = Graf(
#     {
#         'A': {'B': 1, 'C': 2},
#         'B': {"A": 1, 'D': 3, 'E': 4},
#         'C': {'A': 2, 'D': 1, 'J': 3},
#         'D': {'B': 3, 'C': 1, 'F': 7},
#         'E': {'B': 4, 'F': 1, 'I': 2},
#         'F': {'D': 7, 'E': 1, 'J': 3, 'I': 8},
#         'J': {'C': 3, 'F': 3, 'I': 1},
#         'I': {'E': 2, 'F': 8, 'J': 1},
#     }
# )

# g = Graf.adj_matrix_to_adj_list(
#     [
#         ['*', 'A', 'B', 'C'],
#         ['A', '*', '1', '2'],
#         ['B', '1', '*', '3'],
#         ['C', '2', '3', '*'],

#     ]
# )

# print('\n'.join(map(lambda x: ' '.join(map(str, x)), g.adj_matrix())))
# print(g.bfs('A', 'I'))

import unittest

class TestDijkstras(unittest.TestCase):

    def setUp(self):
        # Initialize the graph
        self.graph = Graf({
            'A': {'B': 5, 'C': 3},
            'B': {'A': 5, 'C': 2, 'D': 6},
            'C': {'A': 3, 'B': 2, 'D': 7},
            'D': {'B': 6, 'C': 7}
        })
        # Define the adjacency list

    def test_shortest_path(self):
        # Test the shortest path from 'A' to all other nodes
        result = self.graph.dijkstras('A')
        self.assertEqual(result, {'A': 0, 'B': 5, 'C': 3, 'D': 10})

        # Test the shortest path from 'B' to all other nodes
        result = self.graph.dijkstras('B')
        self.assertEqual(result, {'A': 5, 'B': 0, 'C': 2, 'D': 6})

        # Test the shortest path from 'C' to all other nodes
        result = self.graph.dijkstras('C')
        self.assertEqual(result, {'A': 3, 'B': 2, 'C': 0, 'D': 7})

        # Test the shortest path from 'D' to all other nodes
        result = self.graph.dijkstras('D')
        self.assertEqual(result, {'A': float('inf'), 'B': 6, 'C': 7, 'D': 0})

if __name__ == '__main__':
    unittest.main()