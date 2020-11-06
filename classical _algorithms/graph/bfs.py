from typing import List
import numpy as np

# 构造一个有向带权图的邻接矩阵
inf = float("inf")
graph_matrix = np.array([
    [0, 8, inf, 5, inf],
    [inf, 0, 3, inf, inf],
    [inf, inf, 0, inf, 6],
    [inf, 9, inf, 0, inf],
    [inf, inf, inf, inf, 0]
])

# 此处为邻接矩阵的行数与列数
row = len(graph_matrix)
column = len(graph_matrix[0])

print(row, column)


# 图的深度优先遍历算法
def dfs(graph: List[List], v: int):
    # visited 为全局数组，初始时所有元素均为0表示所有顶点都未被访问过
    visited = [0, 0, 0, 0, 0]

    print(visited)
    return


# 图的广度优先遍历算法

