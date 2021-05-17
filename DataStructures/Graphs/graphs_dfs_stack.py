class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


def dfs_search(root_node, search_value):
    visited = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        print('Visited: [', end=" ")
        for i in range(0, len(visited)):
            print(visited[i].value, end=',')
        print(']')

        if current_node.value == search_value:
            return current_node
        for child in current_node.children:
            if child not in visited and child not in stack:
                stack.append(child)

        print('Stack:   [', end=" ")
        for i in range(0, len(stack)):
            print(stack[i].value, end=",")
        print(']')

if __name__ == '__main__':
    nodeG = GraphNode('G')
    nodeR = GraphNode('R')
    nodeA = GraphNode('A')
    nodeP = GraphNode('P')
    nodeH = GraphNode('H')
    nodeS = GraphNode('S')

    graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
    graph1.add_edge(nodeG, nodeR)
    graph1.add_edge(nodeA, nodeR)
    graph1.add_edge(nodeA, nodeG)
    graph1.add_edge(nodeR, nodeP)
    graph1.add_edge(nodeH, nodeG)
    graph1.add_edge(nodeH, nodeP)
    graph1.add_edge(nodeS, nodeR)

    print('G: {} -> {} -> {}'.format(nodeG.children[0].value, nodeG.children[1].value, nodeG.children[2].value))
    print('R: {} -> {} -> {} -> {}'.format(nodeR.children[0].value, nodeR.children[1].value, nodeR.children[2].value,
                                           nodeR.children[3].value))
    print('A: {} -> {}'.format(nodeA.children[0].value, nodeA.children[1].value))
    print('P: {} -> {}'.format(nodeP.children[0].value, nodeP.children[1].value))
    print('H: {} -> {}'.format(nodeH.children[0].value, nodeH.children[1].value))
    print('S: {}'.format(nodeS.children[0].value))

    assert nodeA == dfs_search(nodeS, 'A')
    print('STOP')
    assert nodeS == dfs_search(nodeP, 'S')
    print('STOP')
    assert nodeR == dfs_search(nodeH, 'R')


