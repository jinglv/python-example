"""
打印 99 乘法表

一共有 10 行，第 i 行的第 j 列等于：j*i，其中：
- i 取值范围：1<=i<=9
- j 取值范围：1<=j<=i
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (j, i, j * i), end="\t")
    print()
