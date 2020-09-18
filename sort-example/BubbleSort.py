def bubble_sort(arr):
    # 获取数组的长度
    l = len(arr)
    for i in range(l):
        for j in range(l - i - 1):
            if (j + 1) > j:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


arr = [2, 1, 7, 9, 5, 8]
sort_arr = bubble_sort(arr)
print(sort_arr)
