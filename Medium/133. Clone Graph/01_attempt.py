#================================
# Working process:
#   1. Use a depth-first search (DFS) approach to traverse the graph and create a copy of each node.
#   2. Use a dictionary to keep track of the original nodes and their corresponding copies
#   3. If a node has already been copied, return the copy from the dictionary
#   4. If a node has not been copied, create a new copy and add it to the dictionary, then recursively copy its neighbors
# TakeAway: Understanding how to use DFS to traverse a graph and create a deep copy of it, as well as the importance of using a dictionary to keep track of the original nodes and their copies to avoid infinite loops and ensure that each node is only copied once.
#================================


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_map = {}
        
        def dfs(curr_node):
            if curr_node in cloned_map:
                return cloned_map[curr_node]

            else:
                copy_node = Node(curr_node.val)
                cloned_map[curr_node] = copy_node

                for i in curr_node.neighbors:

                    copy_node.neighbors.append(dfs(i))

            return copy_node

        return dfs(node)