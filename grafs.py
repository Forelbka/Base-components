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
    
    def adj_matrix_to_adj_list(matrix):
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
    
    def dfs(self, start: str, target: str) -> dict:
        """
        Depth-first search algorithm to find a path from a start node to a target node.

        Parameters:
            start (str): The start node.
            target (str): The target node.

        Returns:
            dict: A dictionary representing the path from the start node to the target node.
                  The keys are the nodes in the path, and the values are the previous nodes in the path.
                  If no path is found, returns None.
        """
        adj_list = self.adj_list
        def dfs_helper(node, target, visited):
            visited.append(node)
            if node == target:
                return [node]
            else:
                for cur_node in adj_list[node].keys() - visited:
                    ret = dfs_helper(cur_node, target, visited)
                    if ret:
                        return ret + [node]
                return None
        visited = []
        return dfs_helper(start, target, visited)
    
    def bfs(self, start: str, target: str) -> dict:
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

g = Graf(
    {
        'A': {'B': 1, 'C': 2},
        'B': {"A": 1, 'D': 3, 'E': 4},
        'C': {'A': 2, 'D': 1, 'J': 3},
        'D': {'B': 3, 'C': 1, 'F': 7},
        'E': {'B': 4, 'F': 1, 'I': 2},
        'F': {'D': 7, 'E': 1, 'J': 3, 'I': 8},
        'J': {'C': 3, 'F': 3, 'I': 1},
        'I': {'E': 2, 'F': 8, 'J': 1},
    }
)

# g = Graf.adj_matrix_to_adj_list(
#     [
#         ['*', 'A', 'B', 'C'],
#         ['A', '*', '1', '2'],
#         ['B', '1', '*', '3'],
#         ['C', '2', '3', '*'],

#     ]
# )

# print('\n'.join(map(lambda x: ' '.join(map(str, x)), g.adj_matrix())))
print(g.bfs('A', 'I'))