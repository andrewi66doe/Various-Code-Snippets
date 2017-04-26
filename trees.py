import random


class Node:
    left_node = None
    right_node = None
    value = None
    parent = None

    def __init__(self, val):
        self.value = val

    def is_leaf(self):
        return self.left_node is None and self.right_node is None


def insert(val, root):
    if val < root.value:
        if root.left_node is None:
            root.left_node = Node(val)
            root.left_node.parent = root
        else:
            insert(val, root.left_node)
    elif val > root.value:
        if root.right_node is None:
            root.right_node = Node(val)
            root.right_node.parent = root
        else:
            insert(val, root.right_node)


def preorder_traversal(root):
    if root is None:
        return

    print(root.value)
    preorder_traversal(root.left_node)
    preorder_traversal(root.right_node)


def postorder_traversal(root):
    if root is None:
        return

    preorder_traversal(root.left_node)
    preorder_traversal(root.right_node)
    print(root.value)


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left_node)
    print(root.value)
    inorder_traversal(root.right_node)


def number_of_nodes(root):
    if root.is_leaf():
        return 1


def count_le(root, k):
    if root is None:
        return 0

    left = count_le(root.left_node, k)

    print(root.value)
    if root.value >= k and root.parent.value <= root.value:
        return left + 1
    elif root.value >= k and root.parent.value <= root.value:
        return left


    right = count_le(root.right_node, k)

    return left + right + 1


def nodes(node):
    if node is None:
        return 0

    left = nodes(node.left_node)
    right = nodes(node.right_node)

    return 1 + left + right


def imbalance(node):
    if node is None:
        return 0, 0

    if node.is_leaf():
        return 0, 1

    bl, ml = imbalance(node.left_node)
    br, mr = imbalance(node.right_node)

    b = max(bl, br, abs(ml - mr))
    m = ml + mr

    return b, m


def heapify(node):
    if node.is_leaf():
        return node
    if node.left_node is not None:
        l = heapify(node.left_node)
        if l.value < node.value:
            t = l.value
            l.value = node.value
            node.value = t
    if node.right_node is not None:
        r = heapify(node.right_node)

        if r.value < node.value and r.value < l.value:
            t = r.value
            r.value = node.value
            node.value = t

    return node


if __name__ == "__main__":
    root = Node(1)
    values = [4, 5, 3, 10, 2, 7]
    for i, _ in enumerate(values):
        insert(values[i], root)

    #inorder_traversal(root)
    print(count_le(root, 7))
