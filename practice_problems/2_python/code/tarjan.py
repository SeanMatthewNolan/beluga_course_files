import numpy as np


class Node:
    def __init__(self, identifier):
        self.identifier = identifier

        self.in_nodes = []
        self.out_nodes = []

        self.index = None
        self.low = None

    def __repr__(self):
        return 'Node_{}'.format(self.identifier)


# Function to create graph from adjacency matrix
def create_graph(adj_mat):
    # Initialize nodes
    num_nodes = adj_mat.shape[0]
    node_list = [Node(_k) for _k in range(num_nodes)]

    # Set in and out nodes (edges)
    for i, node in enumerate(node_list):
        node.in_nodes = [node_j for node_j, cond in zip(node_list, adj_mat[:, i]) if cond]
        node.out_nodes = [node_j for node_j, cond in zip(node_list, adj_mat[i, :]) if cond]

    return node_list


# Create class to encapsulate index and stack of Trajan algorithm
class TarjanClass:
    def __init__(self):
        self.index = 0
        self.stack = []
        self.strongly_connected_components = []

    def tarjan(self, node_set):
        self.index = 0
        self.stack = []

        for node in node_set:
            if node.index is None:
                self.strong_connect(node)

        return self.strongly_connected_components

    def strong_connect(self, node):
        node.index = self.index
        node.low = self.index
        self.index += 1

        self.stack.append(node)

        # Consider out nodes of current node
        for out_node in node.out_nodes:
            if out_node.index is None:
                self.strong_connect(out_node)
                node.low = min(node.low, out_node.low)

            # Check if out_node is already on stack. Bypasses need for onStack
            # flag used in psuedo-code
            # If out_node not on stack, current edge points to already identified
            # strongly connected components
            elif out_node in self.stack:
                node.low = min(node.low, out_node.index)

        # If root node returned to, pop the node from stack and generate
        # strongly connected components
        if node.low == node.index:
            end_node = self.stack.pop()
            scc = [end_node]

            while end_node is not node:
                end_node = self.stack.pop()
                scc.append(end_node)

            self.strongly_connected_components.append(scc)


# Define tarjan as a single function
tarjan = TarjanClass().tarjan

if __name__ == '__main__':
    test_adj_mat = np.array([
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1]
    ])

    graph = create_graph(test_adj_mat)
    sccs = tarjan(graph)
