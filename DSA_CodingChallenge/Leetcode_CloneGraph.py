"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Example:

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.


Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


from collections import defaultdict


class Solution:
    def DFSUtil(self, node, new_node, visited):
        visited[node.val] = new_node
        # print('Node:', node.val)
        for c in node.neighbors:
            key = c.val
            # print('key:', key)
            if key in visited.keys():
                # print('Visited')
                new_node.neighbors.append(visited[key])
            else:
                # print('not Visited')
                new = Node(key, list())
                new_node.neighbors.append(new)
                self.DFSUtil(c, new, visited)

    def cloneGraph(self, node):
        if node is None:
            return None
        visited = defaultdict(Node)
        root = Node(node.val, list())
        self.DFSUtil(node, root, visited)
        '''
        queue = deque()
        queue.appendleft(node)
        root = new_node = Node(node.val, list())
        visited[node.val] = new_node
        while queue:
            n = queue.pop()
            for c in n.neighbors:
                key = c.val
                if key in visited.keys():
                    # print('Visited')
                    new_node.neighbors.append(visited[key])
                else:
                    # print('not Visited')
                    new = Node(key, list())
                    new_node.neighbors.append(new)
                    queue.appendleft(c)
                    visited[key] = new
        '''
        return root
