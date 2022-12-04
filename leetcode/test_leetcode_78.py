from typing import List
import unittest


class Solution:
    # 使用递归解法: time: O(2^n), space: O(2^n)
    def subsets_recursion(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        previous_subset = self.subsets_recursion(nums[:-1])
        return previous_subset + [subset + [nums[-1]] for subset in previous_subset]

    # 迭代算法: time: O(2^n), space: O(2^n)
    def subset_iteration(self, nums: List[int]) -> List[List[int]]:
        all_subset = [[]]
        for num in nums:
            all_subset += [ele + [num] for ele in all_subset]
        return all_subset


class Test78(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.solution_funcs = {
            "recursion": self.s.subsets_recursion,
            "iteration": self.s.subset_iteration,
        }

    def _solution(self, func):
        self.assertEqual(self.solution_funcs[func]([]), [[]])
        self.assertEqual(self.solution_funcs[func]([2]), [[], [2]])
        self.assertEqual(self.solution_funcs[func]([2, 3]), [[], [2], [3], [2, 3]])

    def test_recursion_solution(self):
        self._solution("recursion")

    def test_subset_iteration(self):
        self._solution("iteration")


if __name__ == "__main__":
    unittest.main()
