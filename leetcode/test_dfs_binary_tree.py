import unittest


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def depth_first_search(node, ret=[]):
    ret.append(node.data)
    if node.leftChild is not None:
        depth_first_search(node.leftChild, ret)
    if node.rightChild is not None:
        depth_first_search(node.rightChild, ret)
    return ret


class TestBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.root = self._generate_tree()

    def _generate_tree(self):
        node1 = BinaryTreeNode(50)
        node2 = BinaryTreeNode(20)
        node3 = BinaryTreeNode(45)
        node4 = BinaryTreeNode(11)
        node5 = BinaryTreeNode(15)
        node6 = BinaryTreeNode(30)
        node7 = BinaryTreeNode(78)

        node1.leftChild = node2
        node1.rightChild = node3
        node2.leftChild = node4
        node2.rightChild = node5
        node3.leftChild = node6
        node3.rightChild = node7
        return node1

    def test_depth_first_search(self):
        self.assertEqual(
            depth_first_search(self.root),
            [50, 20, 11, 15, 45, 30, 78],
        )


if __name__ == "__main__":
    unittest.main()
