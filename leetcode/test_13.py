import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_DICT = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = ROMAN_DICT.get(s[-1])
        for i in range(len(s) - 1):
            if ROMAN_DICT.get(s[i]) < ROMAN_DICT.get(s[i + 1]):
                sum -= ROMAN_DICT.get(s[i])
            else:
                sum += ROMAN_DICT.get(s[i])
        return sum


class Test13(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        result = s.romanToInt("III")
        self.assertEqual(result, 3)
        result = s.romanToInt("LVIII")
        self.assertEqual(result, 58)
        result = s.romanToInt("MCMXCIV")
        self.assertEqual(result, 1994)


if __name__ == "__main__":
    unittest.main()
