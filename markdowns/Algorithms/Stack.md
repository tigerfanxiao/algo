Last in First Out: LIFO

stack 用例
1. 在浏览器会保存用户的访问历史, 如果回退的话, 是从最近访问的网站开始回退
2. undo操作, 所有的操作会在stack中
3. 编程中的函数嵌套函数调用

实现Stack这种数据结构可以通过array和linked-lis来实现. 
array和linked-list的区别在于, linked-list动态扩充更容易

他有两种操作, push和pop
在python中, 可以用list和collection.deque来实现stack, 但是list的pop操作的时间复杂度`O(n)`
而collection.deque的pop操作的时间复杂度是`O(1)`

```python
from collections import deque
stack = deque()

stack.append('A')
stack.append('B')
stack.append('C')

stack.pop()  # C
stack.pop()  # B
stack.pop()  # A
```

