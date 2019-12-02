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
        result = []
        for i in range(numRows):
            flagUp = 1
            flagDown = 0
            skipnum = i
            result.append(stringlist[skipnum])
            while skipnum < len(stringlist):
                # print('flagDown:{} flagUp:{} char:{}'.format(flagDown, flagUp, stringlist[skipnum]))
                val = (flagUp * 2 * (numRows - i - 1)) + (flagDown * 2 * i)
                if val != 0:
                    skipnum += val
                    if skipnum >= len(stringlist):
                        break
                    result.append(stringlist[skipnum])
                temp = flagUp
                flagUp = flagDown
                flagDown = temp
        return result

    def convert(self, s: str, numRows: int) -> str:
        stringlist=list(s)
        if stringlist is None:
            return ""
        if numRows == 1:
            return s
        if numRows >= len(stringlist):
            return s
        result = self.__convertutil(stringlist, numRows)
        return "".join(result)

def main():
    testcases=[]
    testcases.append(("", 1))
    testcases.append(("A", 3))
    testcases.append(("AB", 1))
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
