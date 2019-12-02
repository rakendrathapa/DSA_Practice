"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.



Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4.
Example 2:

Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73

"""
from collections import defaultdict

class Solution:
    def calculateTime(self, keyboard, word):
        strdict = defaultdict(int)
        for i in range(len(keyboard)):
            strdict[keyboard[i]] = i

        time = 0
        prev = 0
        for j in range(len(word)):
            time += abs(strdict[word[j]] - prev)
            prev = strdict[word[j]]

        return time

def main():
    testcases = list()
    testcases.append(("abcdefghijklmnopqrstuvwxyz", "cba"))
    testcases.append(("pqrstuvwxyzabcdefghijklmno", "leetcode"))
    testcases.append(("abcdefghijklmnopqrstuvwxyz", ""))

    sol = Solution()
    for case in testcases:
        keyboard, word = case
        ans = sol.calculateTime(keyboard, word)
        print(ans)


if __name__ == '__main__':
    main()
