'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return
        nums.sort()
        # print(nums)
        threeSumslist = []
        candidate = None
        for i in range(len(nums)-2):
            if nums[i] == candidate:
                continue
            candidate = nums[i]
            sum = -nums[i]
            front = i+1
            back = len(nums)-1
            i_candidate = None
            j_candidate = None
            # print('sum:{} current:{} \t nums[{}]:{} nums[{}]:{} '.format(sum, nums[front] + nums[back], front, nums[front], back, nums[back]))
            while front < back:
                if nums[front] == i_candidate and nums[back] == j_candidate:
                    front += 1
                    back -= 1
                    continue                
                
                if nums[front] + nums[back] > sum:
                    back -= 1
                elif nums[front] + nums[back] < sum:
                    front += 1
                else:
                    threeSumslist.append(sorted([nums[front], nums[i], nums[back]]))
                    # print(threeSumslist)
                    i_candidate = nums[front]
                    j_candidate = nums[back]
                    front += 1
                    back -= 1
                    
        
        print(threeSumslist)

def main():
    arrlist = []
    arr1 = [-1, 0, 1, 2, -1, -4]
    arr2 = [0, 0, 0, 0, 0]
    arr3 = [1,-1,-1,0]
    arr4 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    arrlist.append(arr1)
    arrlist.append(arr2)
    arrlist.append(arr3)
    arrlist.append(arr4)
    sol = Solution()
    # sol.threeSum(arr4)
    for arr in arrlist:
        sol.threeSum(arr)


if __name__ == '__main__':
    main()
