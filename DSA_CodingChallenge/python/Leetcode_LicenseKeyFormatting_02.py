class Solution:
    def licenseKeyFormatting(self, S , K):
        tempStr = S.replace("-", "").upper()
        remainder = len(tempStr) % K

        print(tempStr)
        grp1 = [tempStr[0:remainder]]
        others = [tempStr[i:i+K] for i in range(remainder, len(tempStr), K)]

        if remainder:
            return "-".join(grp1 + others)
        return "-".join(others)


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
