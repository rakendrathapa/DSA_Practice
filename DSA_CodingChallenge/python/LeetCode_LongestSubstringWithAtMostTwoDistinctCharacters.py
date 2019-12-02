"""
Given a string s, find the length of the longest substring t  that contains at most 2 distinct characters.
Example 1:
Input: "ecebbbbba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""
from collections import defaultdict
class Solution:
    def __getstartindex(self, charsdict, max_len):
        if charsdict is None or len(charsdict) == 0:
            return None
        minimum = max_len
        for item in charsdict.values():
            if item < minimum:
                minimum = item
        return minimum

    def lengthOfLongestSubstringTwoDistinct(self, s):
        N = len(s)
        if N < 3:
            return N
        start = end = 0
        max_len = 2
        charsdict = defaultdict(int)
        while end < N:
            print(s[end], end)
            charsdict[s[end]] = end
            if len(charsdict.keys()) < 3:
                end += 1
            else:
                if max_len < end - start:
                    max_len = end - start
                start = self.__getstartindex(charsdict, N)
                print('end:', end, 'start:',start, 'max_len:', max_len)
                charsdict.pop(s[start], None)
                print(len(charsdict))
                start += 1

        print('end:', end, 'start:',start, 'max_len:', max_len)
        if max_len < end - start:
            max_len = end - start
        return max_len

def testmain():
    testcases = list()
    testcases.append("eceba")
    testcases.append("ecebbbba")
    testcases.append("eceeebbbbbba")
    testcases.append("ccaabbb")

    sol = Solution()
    for cases in testcases:
        print('cases:{} substrlen"{}'.format(cases, sol.lengthOfLongestSubstringTwoDistinct(cases)))

if __name__ == '__main__':
    testmain()
