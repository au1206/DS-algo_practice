"""
LC1041. Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/

On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.

HINT: The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # the trajectory will be bounded if the original direction changes
        # or original position is same
        # unit distance in directions north, east, south, west
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0  # initial position
        idx = 0  # initial direction is north

        for i in instructions:
            if i == 'L':
                # idx to point to left(west) of present direction
                idx = (idx + 3) % 4

            elif i == 'R':
                # idk to point ot right(east) of present direction
                idx = (idx + 1) % 4

            else:
                # in case of 'G' we add the unit step in the present direction
                x += direc[idx][0]
                y += direc[idx][1]

        # will not be in same direction or same position
        return (x == 0 and y == 0) or idx != 0

