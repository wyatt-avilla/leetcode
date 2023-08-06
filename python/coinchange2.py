from typing import List
from typing import Set
from collections import Counter


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def visualizeGraph(self):
        print(self)
        for connection in self.neighbors:
            connection.visualizeGraph()

    def __str__(self):
        return f"{self.value} -> ({', '.join(str(neighbor.value) for neighbor in self.neighbors)})"

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        graphRoot = GraphNode(amount)
        def buildGraph(root: GraphNode, coins: List[int], prevNodeVal: int, currentPath: List[int], allPaths: Set):
            updatedPath = []
            if prevNodeVal - root.value > 0:
                updatedPath = currentPath + [prevNodeVal - root.value]
            for coinval in coins:
                if (root.value - coinval) >= 0:
                    root.add_neighbor(GraphNode(root.value - coinval))
                if len(root.neighbors) == 0 and (root.value == 0):
                    allPaths.add(tuple(Counter(updatedPath)))
            for neighbor in root.neighbors:
                buildGraph(neighbor, coins, root.value, updatedPath, allPaths)

        allpaths = set()
        buildGraph(graphRoot, coins, graphRoot.value, [], allpaths)
        graphRoot.visualizeGraph()
        return(len(allpaths))




Solution().change(100, [1, 2, 5])



#gg = GraphNode(5)
#gg.add_neighbor(GraphNode(1))
#gg.add_neighbor(GraphNode(2))
#gg.add_neighbor(GraphNode(5))
#gg.neighbors[0].add_neighbor(GraphNode(40))
#
#gg.visualizeGraph()
