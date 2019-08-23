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
    def convert(self, s, numRows):
        if s == "":
            return s
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        step = 1
        pos = 1
        lines = {}
        for c in s:
            if pos not in lines:
                lines[pos] = c
            else:
                lines[pos] += c
            pos += step
            if pos == 1 or pos == numRows:
                step *= -1

        result = ""
        for i in range(1, numRows + 1):
            try:
                result += lines[i]
            except:
                return result
        return result

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
