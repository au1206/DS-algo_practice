"""
Given the root of a Binary Tree and a data value representing a node, return the path from the root to that node in the
form of a list. You can assume that the binary tree has nodes with unique values.
"""

from queue import Queue


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


def path_from_root_to_node(root, data):
    path = []

    def traverse(node, data):
        if node is None:
            return None

        if node.data == data:
            return [data]

        left_answer = traverse(node.left, data)
        if left_answer is not None:
            left_answer.append(node.data)
            return left_answer

        right_answer = traverse(node.right, data)
        if right_answer is not None:
            right_answer.append(node.data)
            return right_answer

        return None

    out = traverse(root, data)
    return list(reversed(out))


def test_function(test_case):
    arr = test_case[0]
    data = test_case[1]
    solution = test_case[2]
    root = convert_arr_to_binary_tree(arr)
    output = path_from_root_to_node(root, data)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':

    # Manual Test
    tree = BinaryTreeNode("apple")
    tree.left = BinaryTreeNode("banana")
    tree.right = BinaryTreeNode("cherry")
    tree.left.left = BinaryTreeNode("dates")
    tree.left.right = BinaryTreeNode("Egg")

    path = path_from_root_to_node(tree, "Egg")
    print(path)


    # Test Case 1
    arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
    data = 5
    solution = [1, 2, 5]

    test_case = [arr, data, solution]
    test_function(test_case)

    # Test Case 2
    arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
    data = 5
    solution = [1, 3, 5]

    test_case = [arr, data, solution]
    test_function(test_case)

    # Test Case 3
    arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
    data = 11
    solution = [1, 3, 4, 6, 10, 11]

    test_case = [arr, data, solution]
    test_function(test_case)

    # Test Case 4
    arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
    data = 8
    solution = [1, 3, 5, 8]

    test_case = [arr, data, solution]
    test_function(test_case)
