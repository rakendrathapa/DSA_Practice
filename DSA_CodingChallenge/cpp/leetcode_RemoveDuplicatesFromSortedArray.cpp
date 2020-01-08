/**
 * PROBLEM NAME: Remove Duplicates from Sorted Array
 *
 * Given a sorted array nums, remove the duplicates in-place such that each element
 * appear only once and return the new length.
 *
 * Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
 *
 * Example 1:
 * Given nums = [1,1,2],
 *
 * Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
 *
 * It doesn't matter what you leave beyond the returned length.
 *
 * Example 2:
 * Given nums = [0,0,1,1,1,2,2,3,3,4],
 * Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
 *
 * It doesn't matter what values are set beyond the returned length.
 *
 * Clarification:
 * Confused why the returned value is an integer but your answer is an array?
 * Note that the input array is passed in by reference, which means modification
 * to the input array will be known to the caller as well.
 *
 * Internally you can think of this:
 *
 * // nums is passed in by reference. (i.e., without making a copy)
 * int len = removeDuplicates(nums);
 * // any modification to nums in your function would be known by the caller.
 * // using the length returned by your function, it prints the first len elements.
 * for (int i = 0; i < len; i++) {
 *  print(nums[i]);
 * }
 */
#include <map>
#include <vector>
#include <iostream>

using namespace std;
int removeDuplicates(vector<int>& nums)
{
    if((nums.size()==1) || (nums.size()==0)){
        return nums.size();
    }
    int len=0;

    std::map<int, int> arrMap;
    vector<int> stack;
    vector<int>::iterator it = nums.begin();
    while(it != nums.end()){
        if(arrMap.count(*it) == 0){
            stack.push_back(*it);
            arrMap[*it]++;
            len++;
        }
        it++;
    }
    for(size_t i=0; i<len; i++){
        nums[i] = stack[i];
        cout << nums[i] << " ";
    }

    return len;
}

int removeDuplicates2(vector<int>& nums)
{
    if(nums.size()< 2){
        return nums.size();
    }
    int j = 0;
	int i = 1;

	while (i < nums.size()) {
		if (nums[i] != nums[j]) {
			j++;
			nums[j] = nums[i];
		}
        i++;
	}

    for(size_t i=0; i<(j + 1); i++){
        cout << nums[i] << " ";
    }
	return j + 1;
}

int main()
{
    vector<int> t1{0,0,1,1,1,2,2,3,3,4,0,1};
    vector<int> t2{0,0,1,1,1,2,2,3,3,4,0,1};
    int len = removeDuplicates(t1);
    cout << "\nlen:" << len << endl;
    len = removeDuplicates2(t2);
    cout << "\nlen:" << len << endl;
    return EXIT_SUCCESS;
}
