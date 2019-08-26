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
        
        stack = list()
        maxcount = count = nextcount = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack):
                    stack.pop()
                    count += 2
                else:
                    
            else:
                break
        
        maxcount = self.__maxcount(count, )

    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
                
        if len(s) == 2:
            return 2 if s=='()' else 0
                
        maxcount = count = nextindex = 0
        for i in range(0, len(s), 2):
            nextindex = i
            if s[i:i+2] == '()':
                count += 2
            else:
                break

        print('nextindex:{} count:{}'.format(i, count))
        if nextindex+1 >= len(s):
            return count
        else: 
            maxcount = self.__maxcount(count, self.longestValidParentheses(s[nextindex+1:]))
        return maxcount


def main():
    testcases = list()
    testcases.append("(()")
    testcases.append(")()())")
    testcases.append("()()")
    testcases.append("()(())")
    testcases.append("()(())(()")
    testcases.append("()(())(()((((()()")

    sol = Solution()
    for case in testcases:
        print(case)
        ans = sol.longestValidParentheses(case)
        print(ans)

if __name__ == '__main__':
    main()