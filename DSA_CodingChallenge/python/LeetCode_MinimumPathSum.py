"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""


class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        print('rows:{} cols:{}'.format(rows, cols))
        minPath = [[0 for i in range(cols)] for j in range(rows)]

        minPath[0][0] = grid[0][0]
        for i in range(1, rows):
            minPath[i][0] = minPath[i - 1][0] + grid[i][0]

        for j in range(1, cols):
            minPath[0][j] = minPath[0][j - 1] + grid[0][j]

        print(minPath)
        for i in range(1, rows):
            for j in range(1, cols):
                minimum = minPath[i - 1][j] if minPath[i - 1][j] < minPath[i][j - 1] else minPath[i][j - 1]
                minPath[i][j] = minimum + grid[i][j]

        print(minPath)
        return minPath[-1][-1]


def main():
    testcases = list()
    testcases.append([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]])

    testcases.append([
        [5, 3, 2, 1, -2, 7],
        [1, 7, -3, 3, 5, 4],
        [4, 4, -2, 8, 1, -3],
        [8, -1, 7, 0, 5, 2],
        [4, 6, -3, 3, -4, 7],
        [-5, 3, -2, 6, 9, 2]])

    sol = Solution()
    for case in testcases:
        ans = sol.minPathSum(case)
        print(ans)


if __name__ == '__main__':
    main()
