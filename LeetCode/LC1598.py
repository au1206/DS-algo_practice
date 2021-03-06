"""
Leet code 1596: Crawler Log Folder
https://leetcode.com/problems/crawler-log-folder/


Share
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example 1:

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
"""


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        steps = 0
        for elem in logs:
            if elem == '../':
                if steps == 0:
                    continue
                stack.pop()
                steps -= 1

            elif elem == './':
                continue

            else:
                stack.append(elem)
                steps += 1

        print(stack)
        return steps
