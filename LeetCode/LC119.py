"""
Leet Code 119: Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33

"""


class Solution:
    def getRow(self, rowIndex):

        row = [1]*(rowIndex+1)
        if rowIndex == 0:
            return row

        prevRow = self.getRow(rowIndex-1)
        for i in range(1, len(row)-1):
            row[i] = prevRow[i-1] + prevRow[i]

        return row

if __name__ == '__main__':

    obj = Solution()
    for elem in range(10):
        print(obj.getRow(elem))
