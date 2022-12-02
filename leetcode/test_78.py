from typing import List
import unittest


class Solution:
    # 使用递归解法: time: O(2^n), space: O(2^n)
    def subsets_recursion(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        previous_subset = self.subsets_recursion(nums[:-1])
        return previous_subset + [subset + [nums[-1]] for subset in previous_subset]

    def subset_iteration(self, nums: List[int]) -> List[List[int]]:
        pass


class Test78(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.subsets_recursion([]), [[]])
        self.assertEqual(s.subsets_recursion([2]), [[], [2]])
        self.assertEqual(s.subsets_recursion([2, 3]), [[], [2], [3], [2, 3]])


if __name__ == "__main__":
    unittest.main()
