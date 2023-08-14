from typing import List
from typing import Set
from functools import cache


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
            for coinval in coins:
                if (root.value - coinval) >= 0:
                    root.add_neighbor(GraphNode(root.value - coinval))

            updatedPath = []
            if prevNodeVal - root.value > 0:
                updatedPath = currentPath + [prevNodeVal - root.value]
            if len(root.neighbors) == 0 and (root.value == 0):
                updatedPath.sort()
                allPaths.add(tuple(updatedPath))

            for neighbor in root.neighbors:
                buildGraph(neighbor, coins, root.value, updatedPath, allPaths)

        @cache
        def obtainPath(amount: int, coins: List[int]) -> int:
            if amount == 0:
                return 0
            elif amount < 0:
                return -1

            else:
                validPaths = set()
                for coin in coins:
                    ob



        allpaths = set()
        buildGraph(graphRoot, coins, graphRoot.value, [], allpaths)

        graphRoot.visualizeGraph()
        return(len(allpaths))


coinList = [1, 2, 5]
targetTotal = 5

print(f"{Solution().change(targetTotal, coinList)} possible ways to make {targetTotal} cents with {coinList}")



#gg = GraphNode(5)
#gg.add_neighbor(GraphNode(1))
#gg.add_neighbor(GraphNode(2))
#gg.add_neighbor(GraphNode(5))
#gg.neighbors[0].add_neighbor(GraphNode(40))
#
#gg.visualizeGraph()
