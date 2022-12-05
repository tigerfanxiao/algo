首先heap是一种Binary Tree [[Binary Tree]]

Heap分为两种Min Heap和Max Heap, 以下介绍Min Heap

* 根节点的元素是数值最小的元素
* 新增节点一定是从左边分支插入
* 插入新增节点后, 再挪动节点到恰当的位置
* 节点可以通过array来存储, 子节点在array中的位置, 可以通过index计算得到
* 