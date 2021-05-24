"""
Gievn an array os size at-least two, dins the smallest subarray that needs to be sorted in place so that the entire
input array becomes sorted

if the input array is alreayd sorted, the function should return [-1,-1], otherwise return the start and end index of
smallest subarray.

input:
a1 = [1,2,3,4,5,8,6,7,9,10,11]
Output:
[s,7]
"""
# approach 1 : sort the array then compare with original to check the difference return first index witch change and
# last index with change.  time complexity = O(nlogn)+ O(n) -> O(nlogn)


def sort_subarray1(a):
    arr = sorted(a)
    left = -1
    right = -1
    for i in range(len(a)):
        if arr[i] == a[i]:
            continue
        else:
            left = i
            break

    for i in range(len(a)-1, -1, -1):
        if arr[i] == a[i]:
            continue
        else:
            right = i
            break

    return [left, right]


# Approach 2: find the smallest and the largest out of place elements in the array, then find the correct positions of
# these elements to find the left and right. Time Complexity: O(n)
def sort_subarray2(a):
    left = -1
    right = -1
    smallest = 100000000
    largest = -100000000
    for i in range(1, len(a)-1):
        if a[i-1] < a[i] <= a[i+1]:
            continue

        else:
            smallest = min(smallest, a[i])
            largest = max(largest, a[i])

    if a[0] > a[1]:
        smallest = min(smallest, a[0])
        largest = max(largest, a[0])
        left = 0

    if a[-1] < a[-2]:
        smallest = min(smallest, a[-1])
        largest = max(largest, a[i-1])
        right = len(a)

    if smallest == 100000000:
        return [-1, -1]

    i = 0
    while smallest >= a[i]:
        i += 1
        left = i

    j = len(a)-1
    while largest <= a[j]:
        j -= 1
        right = j

    if smallest == 100000000:
        left = -1
    if largest == -100000000:
        right = -1

    return [left, right]


if __name__ == '__main__':
    a1 = [1,2,3,4,5,8,6,7,9,10,11]
    a2 = [1,2,3,4,5]
    print(sort_subarray2(a2))
