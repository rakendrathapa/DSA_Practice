'''
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:
Input: "42"
Output: 42
Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''
class Solution:
    def myAtoi(self, int_str):
        intlst = list(int_str)
        val = 0
        sign = False
        signset = False
        intmax = 2**31

        for char in intlst:
            if char == ' ': # whitespace
                if signset is True:
                    break
                continue

            if char == '-' or char == '+':
                if signset is True: # sign
                    break
                else:
                    sign = True if char == '-' else False
                    signset = True
                    continue

            charintval = ord(char) - ord('0')
            if charintval < 0 or charintval > 9:
                break
            if intmax < (val * 10 + charintval):
                val = intmax
                break
            val = val * 10 + charintval
            signset = True

        if sign is True:
            val = -val
        else:
            if val == intmax:
                val = val - 1

        return val

def main ():
    testvalues = []
    testvalues.append('42')
    testvalues.append('   -42')
    testvalues.append('+-2')
    testvalues.append('   +1 123')
    testvalues.append('   0+123')
    testvalues.append('4193 with words')
    testvalues.append('-4193 with words')
    testvalues.append('words and 987')
    testvalues.append('-91283472332')
    testvalues.append('2147483648')
    testvalues.append('-2147483647')
    testvalues.append('-9223372036854775810')
    testvalues.append('9223372036854775810')
    testvalues.append('-5-')

    sol = Solution()
    for vals in testvalues:
        print(sol.myAtoi(vals))

if __name__ == '__main__':
    main()




