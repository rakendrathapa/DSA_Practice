class Solution:
    class __LinkedStack:
        class __Node:
            __slots__ = '_element', '_next'

            def __init__(self, element, next):
                self._element = element
                self._next = next

        def __init__(self):
            """ Empty stack """
            self._head = None
            self._size = 0

        def __len__(self):
            return self._size

        def is_empty(self):
            return self._size == 0

        def push(self, e):
            self._head = self.__Node(e, self._head)
            self._size += 1

        def top(self):
            if self.is_empty():
                raise ValueError('Stack is empty')
            return self._head._element

        def pop(self):
            if self.is_empty():
                raise ValueError('Stack is empty')
            value = self._head._element
            self._head = self._head._next
            self._size -= 1
            return value


    def licenseKeyFormatting(self, S , K):
        tempStrLst = S.upper().split('-')
        stack = self.__LinkedStack()

        for tempStr in tempStrLst:
            stack.push(tempStr)

        tempK = K
        ansStack = self.__LinkedStack()

        while stack.is_empty() is False:
            tempStr = stack.pop()
            # print("stack:{} tempK:{}".format(stack.pop(), tempK))
            if len(tempStr) <= tempK:
                ansStack.push(tempStr)
                tempK -= len(tempStr)
                if tempK == 0:
                    ansStack.push('-')
                    tempK = K
            else:
                stack.push(tempStr[0:(len(tempStr) - tempK)])
                # print("To: push back:{}".format(tempStr[0:len(tempStr) - tempK]))
                ansStack.push(tempStr[(len(tempStr) - tempK):])
                # print("To: push ans:{}".format(tempStr[len(tempStr) - tempK:]))
                ansStack.push('-')
                tempK = K

        ans = ""
        while ansStack.is_empty() is False:
            ans += ansStack.pop()
            # print(ansStack.pop())

        # print(ans)
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
