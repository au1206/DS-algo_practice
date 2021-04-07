"""
Maximum Subarray

"""


def max_crossing_subarray(arr1, low1, mid1, high1):
    left_sum = -10000000
    right_sum = -10000000
    sum = 0
    max_right = high1
    max_left = low1

    for i in range(mid1, low1-1, -1):
        sum += arr1[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for j in range(mid1+1, high1):
        sum += arr1[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum+right_sum


def max_subarray(arr, low, high):
    if high == low:
        return low, high, arr[0]

    else:
        mid = (low + high)//2
        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid+1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum

        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    low, high, value = max_subarray(arr, 0, len(arr))
    print(low+1, high+1, value)
