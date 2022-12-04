
# Do not use append / extend in comprehension expression

Notes: both append and extend method will not have return value, so you will have `[None]` in the first line

```python
# 错误代码
[subset.append(4) for subset in [[1], [2]] # return none

# 正确
[subset + [4] for subset in [[1], [2]] # return [1, 4], [2, 4]
```