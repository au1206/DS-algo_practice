"""
Given an array containing N integers, find the longest band
A band is defined as a subsequence which can be reordered such that all elements appear in a consecutive manner
"""

# naive way
# time complexity : O(nlogn) + O(n)
def longest_band(arr):
    arr = sorted(arr)
    res = 0
    count = 1
    print(arr)
    for i in range(len(arr)-1):

        if arr[i+1] - arr[i] == 1:
            count += 1

        else:
            count = 1

        res = max(res, count)
    # seq = [arr[0]]
    # out = []
    # i = 1
    # while i < len(arr):
    #     if arr[i] - arr[i-1] == 1:
    #         count += 1
    #         # seq.append(arr[i-1])
    #         seq.append(arr[i])
    #         i += 1
    #
    #     else:
    #         count = 1
    #         out.append(seq)
    #         seq = [arr[i]]
    #         i += 1
    #
    #     res = max(res, count)
    #
    # print(out)
    return res


# optimized way O(n)
def longest_band(arr):
    a = set(arr)
    print(a)
    res = 0
    for elem in a:
        if elem-1 in a:
            continue

        else:
            print("new band starting at", elem, end=' ')
            count = 1
            while elem+1 in a:
                count += 1
                elem += 1
            print("with band length", count)

        res = max(res,count)
    return res


if __name__ == '__main__':
   arr = [1, 9,3,0,18,5,2,10,7,12,6]
   print(longest_band(arr))


