"""
Validate if a given string can be interpreted as a decimal number.
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."

Of course, the context of these characters also matters in the input.

"""
from enum import Enum
class Solution:
    def isNumber(self, s):
        teststring=list(s)
        checkcase = {'checkwhitespace':0,
        'checkExponent': 1,
        'checkSign':2,
        'checkDecimal':3,
        'checkInteger':4 }
        case = None
        setSign = False
        setInteger = False
        setlastwhitespace = False
        setSign = False
        setExponent = False
        setDecimal = False
        setLastChar = True
        for char in teststring:
            val = ord(char) - ord('0')
            # print('char:{} ord(char):{}'.format(char, ord(char)))

            if ord(char) == 32 or ord(char)==160:
                # print('val:{}'.format(val))
                case = 'checkwhitespace'
                # print('case:{}'.format(case))
                if setInteger is False:
                    continue
                if setlastwhitespace is True:
                    continue
                setlastwhitespace = True
                setLastChar = False

            elif char == 'e':
                case = 'checkExponent'      # valid - Between Decimal.
                # print('case:{}'.format(case))
                if setInteger is False:
                    return False            # cannot be the first digit, sign or after the whitesign
                if setExponent is True:
                    return False
                setExponent = True
                setLastChar = True

            elif char == '+' or char == '-':
                # can only be before the the integer and no twice
                case = 'checkSign'
                # print('case:{}'.format(case))
                if setlastwhitespace is True:
                    return False
                if setSign is True:
                    return False
                if setExponent is True:
                    continue
                if setInteger is True:
                    return False
                setSign = True
                setLastChar = True

            elif char == '.':
                case = 'checkDecimal'
                # if setInteger is False:
                #    return False
                if setExponent is True:
                    return False
                if setlastwhitespace is True:
                    return False
                if setDecimal is True:
                    return False
                setDecimal = True
                # setLastChar = True

            elif val < 0 or val > 9:
                # print('case: Negative')
                # print('val:{}'.format(val))
                return False
            else:
                case = 'checkInteger'
                # print('case:{}'.format(case))
                if setlastwhitespace is True:
                    return False
                setInteger = True
                setLastChar = False
        if setLastChar is False:
            return True
        return False

def main():
    testcases = []
    testcases.append("0")
    testcases.append("0.1")
    testcases.append("abc")
    testcases.append("1 a")
    testcases.append("2e10")
    testcases.append(" -90e3   ")
    testcases.append(" 1e")
    testcases.append("e3")
    testcases.append(" 6e-1")
    testcases.append(" 99e2.5 ")
    testcases.append("53.5e93")
    testcases.append(" --6 ")
    testcases.append("-+3")
    testcases.append("95a54e53")

    sol = Solution()
    for teststring in testcases:
        ans = sol.isNumber(teststring)
        print("{} => {}".format(teststring, ans))

if __name__ == '__main__':
    main()
