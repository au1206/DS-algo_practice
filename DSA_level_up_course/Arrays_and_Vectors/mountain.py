"""
Write a function that take in an array of distinct integers, and returns the length of highest mountain.
A mountain is defined as adjacent integers that are strictly increasing until they reach a peak, at which becomes
strictly decreasing. At least 3 numbers are needed to for a mountain
"""
# identify peaks - a[]
# from the peak, move backwards till they decrease, similarly for positive side

# O(2n)
def peaks(arr):
    out = []
    for i in range(1, len(arr)-1):
        count_back, count_front = 0, 0

        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            # found a peak
            # count backwards
            j = i
            while j >= 1 and arr[j] > arr[j-1]:
                count_back += 1
                j -= 1

            # count forward
            # we can further optimize by using i directly instead of k as we want the counter to move down from the
            # peak in one pass
            # k = i
            # while k <= len(arr)-1 and arr[k] > arr[k+1]:
            #     count_front += 1
            #     k += 1
            # out.append((arr[i], count_back, count_front, count_back + count_front+1))

            while i <= len(arr)-1 and arr[i] > arr[i+1]:
                count_front += 1
                i += 1


    return out


if __name__ == '__main__':
    arr = [5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, 4]
    print(peaks(arr))
