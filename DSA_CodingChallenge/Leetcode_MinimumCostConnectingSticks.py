"""
Minimum Cost to Connect Sticks
User Accepted: 661
User Tried: 825
Total Accepted: 669
Total Submissions: 1352
Difficulty: Medium
You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.



Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30
"""

import heapq

class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        # print(sticks)
        cost = 0
        while len(sticks) != 1:
            min_stick = heapq.heappop(sticks)
            # print(min_stick)
            min_stick2 = heapq.heappop(sticks)
            # print(min_stick2)

            cost += (min_stick + min_stick2)  # Update the total cost
            heapq.heappush(sticks, (min_stick + min_stick2))

        return cost

def main():
    testcases = list()
    testcases.append([2,4,3])
    testcases.append([1,8,3,5])
    sol = Solution()

    for case in testcases:
        ans = sol.connectSticks(case)
        print(ans)

if __name__ == '__main__':
    main()
