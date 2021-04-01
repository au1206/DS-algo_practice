"""
Leet code 41: First Missing Positive
https://leetcode.com/problems/first-missing-positive/


Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:
Input: nums = [1,2,0]
Output: 3


Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
0 <= nums.length <= 300
-2^31 <= nums[i] <= 2^31 - 1


Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

"""


# Solution1: complexity O(n^2)
class Solution1:

    def firstMissingPositive(self, nums) -> int:
        for elem in range(1, len(nums)+2):
            if elem not in nums:
                return elem


# Solution2: complexity O(n) space: O(n)
"""
create a counter array, since we only care about numbers between 1 to len(nums)+1
"""


class Solution2:

    def firstMissingPositive(self, nums) -> int:
        arr = [True] + [False]*300
        for elem in nums:
            if 0 < elem <= 300:
                arr[elem] = True

        for i, _ in enumerate(arr):
            if not _:
                return i

        else:
            return len(nums)+1


# Solution3: complexity O(n), space complexity: O(1)
class Solution3:

    def firstMissingPositive(self, nums) -> int:
        n, i = len(nums), 0
        while i < n:
            while 1 <= nums[i] <= n:
                pos = nums[i] - 1
                if nums[i] == nums[pos]:
                    break
                nums[i], nums[pos] = nums[pos], nums[i]
            i = i + 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':

    inp = [7,8,9,11,12]

    obj1 = Solution1()
    obj2 = Solution2()
    obj3 = Solution3()

    assert(obj3.firstMissingPositive([7,8,9,11,12]) == 1), "Wrong results"
    assert (obj3.firstMissingPositive([1,2,0]) == 3), "Wrong results"
    assert (obj3.firstMissingPositive([3,4,-1,1]) == 2), "Wrong results"
    print("All Testcases Passed")
    # print(result)

