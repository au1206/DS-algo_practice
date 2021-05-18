"""
Given an array and a sum S, find 3 distinct numbers in the array to form the target sum.
the numbers in each triplet should be ordered in ascending order and the triplets should be ordered as well
Return empty array if no triplet exists

array = [1,2,3,4,5,6,7,8,9,15]
sum = 18
Output:
[[1,2,15],[3,7,8],[4,6,8],[5,6,7]]
"""
# brute force: O(n^3)
# element + pair sum : O(n^2), space : O(n)
# element + sorted_array (pair sum with 2 pointers): O(n) + O(nlogn)(for sorting), constant space


def triplet(arr:list, s:int):
    # Approach: pick one element then for the rest of the array use double pointers to find the pairs
    # step 1: sort the array
    # step 2: iterate over each element and call pairsum with 2 pointers
    res = []
    arr = sorted(arr)
    for i in range(0, len(arr)-2):
        x = s-arr[i]
        p1 = i+1
        p2 = len(arr)-1
        while p1 < p2:
            if arr[p1]+arr[p2] == x:
                res.append([arr[i], arr[p1], arr[p2]])
                p1 += 1
                p2 -= 1

            elif arr[p1] + arr[p2] > x:
                p2 -= 1

            else:
                p1 += 1
    return res


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    sum = 18
    res = triplet(array, sum)
    print(res)
