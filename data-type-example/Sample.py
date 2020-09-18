from random import randint, sample

"""
使用 sample 抽样，如下例子从 100 个样本中随机抽样 10 个
"""

arr = [randint(0, 50) for _ in range(100)]
print(arr[:5])
arr_sample = sample(arr, 10)
print(arr_sample)
