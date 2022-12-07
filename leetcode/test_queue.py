import unittest
from collections import deque

class Queue:
    def __init__(self) -> None:
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)
    

    def dequeue(self):
        return self.container.pop()


    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0



# queue practise
# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000
# 1001
# 1010

def solution():
    queue = Queue()
    queue.enqueue('1')
    result = []
    while len(result) < 10:
        cur = queue.dequeue()
        result.append(cur)
        queue.enqueue(cur + '0')
        queue.enqueue(cur + '1')
    return result



class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
    
    def test_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.is_empty(), True)
        
        
    def test_solution(self):
        self.assertEqual(solution(), ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010'])


if __name__ == '__main__':
    solution()
    unittest.main()
    