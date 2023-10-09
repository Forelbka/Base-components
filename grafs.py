class Graf():
    def __init__(self, adj_list:dict):
        self.adj_list = adj_list

    def adj_matrix(self) -> list:
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
        adj_list = {}
        keys = matrix[0][1:]
        for i in range(1, len(matrix)):
            adj_list[keys[i - 1]] = {}
            for j in range(1, len(matrix)):
                if matrix[i][j] != '*':
                    adj_list[keys[i - 1]][keys[j - 1]] = matrix[i][j]
        return Graf(adj_list)

    def dijkstras(self, start: str) -> dict:
        adj_list = self.adj_list
        ret_dict = {start: 0, **{key: float('inf') for key in adj_list}}
        ret_dict[start] = 0
        visited = [start]
        cur_node = start
        while len(visited) < len(adj_list):
            next_node = min(adj_list[cur_node].keys(), key=lambda x: ret_dict[x])
            ret_dict[next_node] = ret_dict[cur_node] + adj_list[cur_node][next_node]
            visited.append(next_node)
            cur_node = next_node
        return ret_dict
        

    def __repr__(self) -> str:
        return self.adj_list
    
    def __str__(self) -> str:
        return str(self.adj_list)

g = Graf(
    {
        'A': {'B': 1, 'C': 2},
        'B': {'A': 1, 'C': 3},
        'C': {'A': 2, 'B': 3},
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
print(g.dijkstras('A'))