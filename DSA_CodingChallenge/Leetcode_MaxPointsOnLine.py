'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o �
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

'''
from collections import defaultdict

class Solution:
    def __maxval(self, val1, val2):
        return val1 if val1 > val2 else val2

    def __gcd(self, x,y):
        while(y):
            x, y = y, x % y
        return x

    def maxPoints(self, points):        # points: List[List[int]]
        if len(points) <= 2:
            return len(points)

        maxPointsLength = 0

        for i in range(len(points)):
            currMax = overlapPoints = verticalPoints = 0
            slopes = defaultdict(int)

            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2, y2 = points[j]

                # If both point equal
                if points[j] == points[i]:
                    overlapPoints += 1
                # If x co-ordinate is same, then Perpendicular slope
                elif x1 == x2:
                    verticalPoints += 1

                else:
                    yDif = y2 - y1
                    xDif = x2 - x1
                    g = self.__gcd(xDif, yDif)

                    # Reducing the difference by their gcd
                    yDif /= g
                    xDif /= g
                    slope = (int(yDif), int(xDif))
                    # print('x1:{} y1:{} x2:{} y2:{} slope:{}'.format(x1, y1, x2, y2, slope))

                    slopes[slope] += 1
                    currMax = self.__maxval(currMax, slopes[slope])
                currMax = self.__maxval(currMax, verticalPoints)

            # updating global maximum
            maxPointsLength = self.__maxval(maxPointsLength, currMax + overlapPoints + 1)

        return maxPointsLength

def main():
    sol = Solution()
    points = []
    points.append([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
    points.append([[1,1],[2,2],[3,3]])

    for point in points:
        ans = sol.maxPoints(point)
        print(ans)

if __name__ == '__main__':
    main()
