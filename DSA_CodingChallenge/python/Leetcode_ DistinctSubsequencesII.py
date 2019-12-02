"""
Given a string S, count the number of distinct, non-empty subsequences of S .
Since the result may be large, return the answer modulo 10^9 + 7.
�
Example 1:
Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:
Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
Example 3:
Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

"""

class Solution(object):
    def distinctSubseqII(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i
        return (dp[-1] - 1) % (10**9 + 7)


def testmain():
    testcases = list()
    testcases.append("abc")
    testcases.append("aba")
    testcases.append("aaa")
    sol = Solution()
    for cases in testcases:
        print(cases, sol.distinctSubseqII(cases))


if __name__ == '__main__':
    testmain()
