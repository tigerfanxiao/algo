import unittest
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# practice 1
# Write a function that can reverse a string using stack data structure with Stack
def reverse_string_with_stack(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ""

    while not stack.is_empty():
        rstr += stack.pop()

    return rstr


# practice 2
# Write a function that checks if paranthesis in the string are balanced or not
def check_balanced_string(s):
    left_paranthesis = "{(["
    right_paranthesis = "})]"
    paranthesis_dict = dict(zip(left_paranthesis, right_paranthesis))
    stack = Stack()

    for ch in s:
        if ch in left_paranthesis:
            stack.push(ch)
        if ch in right_paranthesis:
            if stack.is_empty():
                return False
            if paranthesis_dict.get(stack.peek()) == ch:
                stack.pop()
            else:
                return False
    return stack.is_empty()


class StackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_stack(self):
        self.stack.push("A")
        self.stack.push("B")
        self.assertEqual(self.stack.size(), 2)
        self.assertEqual(self.stack.peek(), "B")
        self.assertEqual(self.stack.pop(), "B")
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), "A")
        self.assertEqual(self.stack.pop(), "A")
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(self.stack.is_empty(), True)


class PractiseTests(unittest.TestCase):
    def test_reverse_string_with_stack(self):
        self.assertEqual(reverse_string_with_stack("fanxiao"), "oaixnaf")

    def test_check_balanced_string(self):
        self.assertEqual(check_balanced_string("({a+b})"), True)
        self.assertEqual(check_balanced_string("))((a+b}{"), False)
        self.assertEqual(check_balanced_string("((a+b))"), True)
        self.assertEqual(check_balanced_string("))"), False)
        self.assertEqual(check_balanced_string("[a+b]*(x+2y)*{gg+kk}"), True)


if __name__ == "__main__":
    unittest.main()
