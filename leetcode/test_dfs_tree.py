import unittest


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, node):
        self.children.append(node)

    def depthFirstSearch(self, array=[]):
        array.append(self.name)
        if len(self.children) > 0:
            for child in self.children:
                child.depthFirstSearch(array)
        return array


class GrapthTests(unittest.TestCase):
    def _generate_graph(self):
        nodeA = Node("A")
        nodeB = Node("B")
        nodeC = Node("C")
        nodeD = Node("D")
        nodeE = Node("E")
        nodeF = Node("F")
        nodeG = Node("G")

        nodeA.addChild(nodeB)
        nodeA.addChild(nodeC)
        nodeB.addChild(nodeD)
        nodeB.addChild(nodeE)
        nodeC.addChild(nodeF)
        nodeF.addChild(nodeG)
        return nodeA

    def setUp(self):
        self.node = self._generate_graph()

    def test_depth_first_search(self):
        result = self.node.depthFirstSearch()
        self.assertEqual(result, ["A", "B", "D", "E", "C", "F", "G"])


if __name__ == "__main__":
    unittest.main()
