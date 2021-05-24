"""
given an array, find the minimum number of swaps required to make the array sorted

Input:
a = [5,4,3,2,1]
Output:
2
"""

def min_swaps(arr):
    ans = 0
    visited = [False] * len(arr)
    paired_arr = [(x, i) for i, x in enumerate(arr)]
    print(paired_arr)
    print(sorted(paired_arr))
    corrected_arr = sorted(paired_arr)

    for i in range(len(arr)):
        old_pos = corrected_arr[i][1]
        if visited[i] or old_pos == i:
            continue

        cycle = 0
        node = i

        while not visited[node]:
            visited[node] = True
            next_node = corrected_arr[node][1]
            node = next_node
            cycle += 1

        ans += cycle - 1
    return ans



if __name__ == '__main__':
    a = [5, 4, 3, 2, 1]
    print(min_swaps(a))

    a = [2,4,5,1,3]
    print(min_swaps(a))
