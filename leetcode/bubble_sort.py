import unittest


def bubble_sort(arr):
    pass


class BubbleTests(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
