"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.
Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
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

    def lengthOfLongestSubstringKDistinct(self, s, k):
        N = len(s)
        if k == 0:
            return 0
        if N <= k+1:
            return N

        start = end = 0
        max_len = k
        charsdict = defaultdict(int)
        while end < N:
            # print(s[end], end)
            charsdict[s[end]] = end
            if len(charsdict.keys()) < k+1:
                end += 1
            else:
                if max_len < end - start:
                    max_len = end - start
                start = self.__getstartindex(charsdict, N)
                # print('end:', end, 'start:',start, 'max_len:', max_len)
                charsdict.pop(s[start], None)
                # print(len(charsdict))
                start += 1

        # print('end:', end, 'start:',start, 'max_len:', max_len)
        if max_len < end - start:
            max_len = end - start
        return max_len

def testmain():
    testcases = list()
    testcases.append(("a", 0))
    testcases.append(("eceba", 2))
    testcases.append(("aa",1))
    testcases.append(("ecebbbba", 3))
    testcases.append(("eceeebbbbbba", 2))
    testcases.append(("ccaabbb", 1))

    sol = Solution()
    for cases in testcases:
        val, k = cases
        print('cases:{} k:{} substrlen"{}'.format(val, k, sol.lengthOfLongestSubstringKDistinct(val, k)))

if __name__ == '__main__':
    testmain()
