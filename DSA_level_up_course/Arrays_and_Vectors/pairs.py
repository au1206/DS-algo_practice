"""
Given an array and a sum S, find two distinct numbers in the array to form the target sum

"""
# brute force : O(n^2)
# sort + binary search: O(nlogn)
# sets : O(n)


def pairs(arr: list, sum: int):
    set1 = set()

    for elem in arr:
        x = sum-elem
        if x in set1:
            return [x, elem]
        else:
            set1.add(elem)

    return None


if __name__ == '__main__':
    arr = [10, 5, 2, 3, -6, 9, 11]
    s = 4
    print(pairs(arr, s))
