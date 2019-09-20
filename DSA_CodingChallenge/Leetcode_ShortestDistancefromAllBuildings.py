"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""
import sys
from collections import deque, defaultdict


class Solution:
    def __collectCandidate(self, grid, visited):
        c_row, c_col =  -1, -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    c_row, c_col = row, col
                elif grid[row][col] == 2:
                    visited[row][col] = True
        return c_row, c_col

    class __Point:
        __slots__ = 'row', 'col', 'dist'

        def __init__(self, row, col, distance):
            self.row = row
            self.col = col
            self.dist = distance

    def __bfs(self, grid, visited, row, col):
        q = deque()
        m = len(grid)
        n = len(grid[0])

        buildings = defaultdict(list)
        pointdict = defaultdict(list)
        candidates = list()

        q.appendleft(self.__Point(row, col, 0))
        totalDistance = 0
        while len(q) != 0:
            point = q.pop()
            r = point.row
            c = point.col
            d = point.dist
            if r < 0 or c < 0 or r >= m or c >= n or visited[r][c]:
                continue


            print('\nr:{} c:{} d:{}'.format(r, c, d))

            visited[r][c] = True
            if grid[r][c] == 1:
                totalDistance = int((totalDistance + d)/2)
                candidates.append(d)


                buildings.append(d)
                print('buildings:{} totalDistance:{}'.format(buildings, totalDistance))
            else:
                pointdict[d].append((r,c))
                print('pointdict[{}]:{}'.format(d, pointdict[d]))

            q.appendleft(self.__Point(r + 1, c, d + 1))
            q.appendleft(self.__Point(r - 1, c, d + 1))
            q.appendleft(self.__Point(r, c + 1, d + 1))
            q.appendleft(self.__Point(r, c - 1, d + 1))

        return pointdict[int(totalDistance/2)]


    def minTotalDistance(self, grid):
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        row, col = self.__collectCandidate(grid, visited)
        if row == -1 or col == -1:
            return -1
        # row, col = 0, 0
        return self.__bfs(grid, visited, row, col)

def testmain():
    testcases = list()
    testcases.append([[1,0,2,0,1],
                      [0,0,0,0,0],
                      [0,0,1,0,0]])

    sol = Solution()
    for cases in testcases:
        ans = sol.minTotalDistance(cases)
        print(ans)


if __name__ == '__main__':
    testmain()
