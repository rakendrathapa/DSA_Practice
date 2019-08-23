"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution:
    def __convertutil(self, stringlist, numRows):
        skipnum = 2 * (numRows - 1)
        result = stringlist[0::skipnum]
        return result

    def convert(self, s: str, numRows: int) -> str:
        stringlist=list(s)
        result = self.__convertutil(stringlist, numRows)
        print(result)
        # result += stringlist[1::skipnum]
        # for i in range(numRows):
        #    result += s[i:, numRows]
        return result

def main():
    testcases=[]
    testcases.append(("PAYPALISHIRING", 3))
    testcases.append(("PAYPALISHIRING", 4))
    sol = Solution()
    for case in testcases:
        s, numRows = case
        print("s:{} numRows:{}".format(s, numRows))
        ans = sol.convert(s, numRows)
        print('s:{} result:{}'.format(s, ans)) 

if __name__ == '__main__':
    main()