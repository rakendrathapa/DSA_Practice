from collections import deque

class Solution:
    def licenseKeyFormatting(self, S , K):
        tempStrLst = S.upper().split('-')

        stack = list()
        ansstack = list()

        for tempStr in tempStrLst:
            stack.append(tempStr)

        # print(stack)

        tempK = K

        while len(stack) != 0:
            tempStr = stack.pop()
            if len(tempStr) <= tempK:
                ansstack.append(tempStr)
                tempK -= len(tempStr)
                if tempK == 0:
                    ansstack.append('-')
                    tempK = K
            else:
                stack.append(tempStr[0:(len(tempStr) - tempK)])
                ansstack.append(tempStr[(len(tempStr) - tempK):])
                ansstack.append('-')
                tempK = K

        ans = ""
        # print(queue)
        # print("".join(queue))
        while len(ansstack) != 0:
            ans += ansstack.pop()

        if ans == '':
            return ''
        elif ans[0] == '-':
            return ans[1:]
        else:
            return ans



def main():
    testcases = list()
    testcases.append(("5F3Z-2e-9-w", 4))
    testcases.append(("2-5g-3-J", 2))
    testcases.append(("---", 3))
    testcases.append(("2-4A0r7-4k", 4))

    sol = Solution()
    for cases in testcases:
        S, K = cases
        ans = sol.licenseKeyFormatting(S, K)
        print(ans)


if __name__ == '__main__':
    main()
