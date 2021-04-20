"""
Leet Code 682: Baseball Game
https://leetcode.com/problems/baseball-game/

You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.

"""


class Solution:
    def calPoints(self, ops: list[str]) -> int:
        list1 = []
        sum = 0
        for elem in ops:
            if elem == '+':
                op1 = int(list1[-1])
                op2 = int(list1[-2])
                list1.append(op1 + op2)

            elif elem == 'D':
                list1.append(2 * int(list1[-1]))

            elif elem == 'C':
                list1.pop()

            else:
                list1.append(int(elem))

        for x in list1:
            sum += x

        return sum
