"""
Given n non negative integers represeniting an elevation map where width of easch bart is 1, compute how much water can
it trap after raining

input:
height: [0,1,0,2,1,0,1,3,2,1,2,1]
output : 6
refer rains.png in assets for explanation
"""
# water trapped at a given position i would be min(left, right) - height at i


def water(height):
    # store max of left for each i in a new array
    # store max of right for each i in a new array
    # this would get the time complexity down from O(n^2) to O(n)

    left_max = [0] * len(height)
    right_max = [0] * len(height)
    max_left = height[0]
    max_right = height[-1]
    sum = 0

    for i in range(len(height)):
        max_left = max(max_left, height[i])
        left_max[i] = max_left

    for i in range(len(height)-1, -1, -1):
        max_right = max(max_right, height[i])
        right_max[i] = max_right

    for i in range(len(height)):
        sum += min(left_max[i], right_max[i]) - height[i]

    print(left_max)
    print(right_max)
    return sum


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(water(height))
