# LongestPalindromeSubstring
class Solution:
    def longestPalindrome(self, s):
        # A O(n^2) time and O(1) space program to find the
        #longest palindromic substring

        # This function prints the longest palindrome substring (LPS)
        # of str[].
        # print(len(s))
        maxLength = 1
        length = len(s)
        low = 0
        high = 0
        table = [[0 for x in range(length)] for x in range(length)]
        print("Init table: {}".format(table))

        # One by one consider every character as center point of
        # even and length palindromes
        for i in range(length):
            table[i][i] = 1

        print("table 1: {}".format(table))

        # Palindromes of length 2
        for i in range(1, length):
            if s[i-1] == s[i]:
                table[i-1][i] = 1
                if maxLength < 2:
                    maxLength = 2
                    low=i-1
                    high=i
        print("table 2: {}".format(table))
        print("low: {} high:{} maxlength: {}".format(low, high, maxLength))
        for k in range(2, length):
            for i in range(k, length):
                if s[i-k] == s[i] and table[i-k+1][i-1] == 1:
                    table[i-k][i] = 1
                    if maxLength < k+1:
                        maxLength = k+1
                        low = i - k
                        high = i
                    print("table {}: {}".format(k, table))
                    print("low: {} high:{} maxlength: {}".format(low, high, maxLength))

        print("Final: low: {} high:{} maxlength: {}".format(low, high, maxLength))
        palindrome = s[low:high+1]
        print("Palindrome substring is: {}".format(palindrome))
        return palindrome

def main():
    s = 'babad'
    sol = Solution()
    ans = sol.longestPalindrome(s)
    print(ans)

if __name__ == "__main__":
    main()
