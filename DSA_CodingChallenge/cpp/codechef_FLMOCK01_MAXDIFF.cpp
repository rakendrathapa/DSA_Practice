/**
 * PROBLEM NAME: Maximum Weight Difference
 *
 * Chef has gone shopping with his 5-year old son. They have bought N items so far.
 *  The items are numbered from 1 to N, and the item i weighs Wi grams.
 * Chef's son insists on helping his father in carrying the items. He wants his dad
 * to give him a few items. Chef does not want to burden his son.
 * But he won't stop bothering him unless he is given a few items to carry.
 * So Chef decides to give him some items. Obviously, Chef wants to give the kid less weight to carry.
 *
 * However, his son is a smart kid. To avoid being given the bare minimum weight to carry,
 * he suggests that the items are split into two groups, and one group contains exactly K items.
 * Then Chef will carry the heavier group, and his son will carry the other group.
 *
 * Help the Chef in deciding which items should the son take. Your task will be simple.
 * Tell the Chef the maximum possible difference between the weight carried by him and the weight carried by the kid.
 *
 * Input:
 * The first line of input contains an integer T, denoting the number of test cases.
 * Then T test cases follow. The first line of each test contains two space-separated integers N and K.
 * The next line contains N space-separated integers W1, W2, ..., WN.
 *
 * Output:
 * For each test case, output the maximum possible difference between the weights carried by both in grams.
 *
 * Constraints:
 * 1 ≤ T ≤ 100
 * 1 ≤ K < N ≤ 100
 * 1 ≤ Wi ≤ 100000 (10^5)
 *
 * Example:
 * Input:
 * 2
 * 5 2
 * 8 4 5 2 10
 * 8 3
 * 1 1 1 1 1 1 1 1
 *
 * Output:
 * 17
 * 2
 *
 * Explanation:
 * Case #1: The optimal way is that Chef gives his son K=2 items with weights 2 and 4.
 * Chef carries the rest of the items himself. Thus the difference is: (8+5+10) − (4+2) = 23 − 6 = 17.
 *
 * Case #2: Chef gives his son 3 items and he carries 5 items himself.
 **/
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int t=0,n=0,k=0;
    int itm=0;

    std::cin >> t;
    while(t--)
    {
        std::vector<int> items;
        std::cin >> n;
        std::cin >> k;
        for(int i=0; i<n; i++){
            std::cin >> itm;
            items.push_back(itm);
        }

        std::sort(items.begin(), items.end());

        // Initializing the value to 0
        int sum = 0, sum1 = 0, sum2 = 0;

        // Getting the sum of the array
        for (int i = 0; i < n; i++) {
            sum += items[i];
        }
        // Getting the sum of first k elements
        for (int i = 0; i < k; i++) {
            sum1 += items[i];
        }
        // Getting the sum of (n-k) elements
        for (int i = k; i < n; i++) {
            sum2 += items[i];
        }
        std::cout << "sum1:" << sum1 << " sum2:" << sum2 << " total:" << sum << std::endl;

        // Returning the maximum possible difference.
        int diff = std::max(abs(sum1 - (sum - sum1)), abs(sum2 - (sum - sum2)));
        std::cout << diff << std::endl;
    }
    return EXIT_SUCCESS;
}
