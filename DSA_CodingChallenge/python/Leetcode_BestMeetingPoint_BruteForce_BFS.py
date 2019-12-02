"""
 A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.

"""
import sys
from collections import deque


class Solution:
    class __Point:
        __slots__ = 'row', 'col', 'dist'

        def __init__(self, row, col, distance):
            self.row = row
            self.col = col
            self.dist = distance

    def __search(self, grid, row, col):
        q = deque()
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]
        q.appendleft(self.__Point(row, col, 0))
        totalDistance = 0
        while len(q) != 0:
            point = q.pop()
            r = point.row
            c = point.col
            d = point.dist
            if r < 0 or c < 0 or r >= m or c >= n or visited[r][c]:
                continue
            if grid[r][c] == 1:
                totalDistance += d
            visited[r][c] = True
            q.appendleft(self.__Point(r + 1, c, d + 1))
            q.appendleft(self.__Point(r - 1, c, d + 1))
            q.appendleft(self.__Point(r, c + 1, d + 1))
            q.appendleft(self.__Point(r, c - 1, d + 1))
        return totalDistance

    def minTotalDistance(self, grid):
        minDistance = sys.maxsize

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                distance = self.__search(grid, row, col)
                minDistance = min(distance, minDistance)
        return minDistance


def testmain():
    testcases = list()
    testcases.append([[1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0]])

    testcases.append([[0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0],
                      [1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1],
                      [1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0],
                      [1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,1],
                      [0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
                      [0,1,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1],
                      [0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0],
                      [0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0],
                      [1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0],
                      [0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1],
                      [0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0],
                      [0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
                      [1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1],
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
                      [0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0],
                      [0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0],
                      [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
                      [1,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0],
                      [0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0],
                      [0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                      [0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0],
                      [0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0],
                      [0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1],
                      [0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0],
                      [0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0],
                      [0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0]])
    sol = Solution()
    for cases in testcases:
        ans = sol.minTotalDistance(cases)
        print(ans)


if __name__ == '__main__':
    testmain()
