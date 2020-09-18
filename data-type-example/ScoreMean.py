"""
去最求平均

去掉列表中的一个最小值和一个最大值后，计算剩余元素的平均值
"""


def score_mean(arr):
    arr.sort()  # 对数组进行排序
    arr2 = arr[1:-1]  # 去掉数组的第一位和最后一位（数组中最小的数和最大的数）
    return round((sum(arr2) / len(arr2)), 1)  # 求平均数


arr = [9.1, 9.0, 8.1, 9.7, 19, 8.2, 8.6, 9.8]
print(score_mean(arr))
