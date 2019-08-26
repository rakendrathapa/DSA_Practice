"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
class Solution:
    def __maxcount(self, leftval, rightval):
        return leftval if leftval > rightval else rightval


    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0

        if len(s) == 2:
            return 2 if s=='()' else 0

        maxcount = left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1

            elif s[i] == ')':
                right += 1

            if left == right:
                maxcount = self.__maxcount(maxcount, 2*right)

            if right > left:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1

            elif s[i] == ')':
                right += 1

            if left == right:
                maxcount = self.__maxcount(maxcount, 2 * right)

            if left > right:
                left = right = 0

        return maxcount


def main():
    testcases = list()
    testcases.append("(()")
    testcases.append(")()())")
    testcases.append("()()")
    testcases.append("()(())")
    testcases.append("()(())(()")
    testcases.append(")()())()()(")
    testcases.append("")

    sol = Solution()
    for case in testcases:
        print(case)
        ans = sol.longestValidParentheses(case)
        print(ans)

if __name__ == '__main__':
    main()
