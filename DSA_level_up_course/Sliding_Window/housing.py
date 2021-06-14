"""
Along one side of road there is a sequence of vacant plot of land. Each plot has a different area. You want to buy
K acres of land . you want to find all segments of contiguous plots whose sum is T
"""


def plots(a, target):
    i = 0
    k = 0
    sum = 0
    res = []
    while k < len(a):
        sum += a[k]
        k += 1

        while sum > target and i < k:
            sum -= a[i]
            i += 1

        if sum == target:
            res.append([i, k-1])

    return res


a1 = [1,2,3,4,5,6,7]
a2 = [7,6,5,4,3,2,1]
a3 = [1,3,2,1,4,1,3,2,1,1,2]
t = 8
print(plots(a3, t))
