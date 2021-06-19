"""
LeetCode 953: Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.


Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # creating hashmap to store char ranks
        # O(len(order))
        dict1 = {}
        for k, v in enumerate(order):
            dict1[v] = k
        # print(dict1)

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if dict1[words[i][j]] > dict1[words[i + 1][j]]:
                        return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break
        return True

