/**
 * Problem Name: Plus Multiply
 *
 * Chef has a sequence A1,A2,…,AN.
 * He needs to find the number of pairs (i,j) (1≤i<j≤N) such that Ai+Aj=Ai⋅Aj.
 *
 * Input
 * The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
 * The first line of each test case contains a single integer N.
 * The second line contains N space-separated integers A1,A2,…,AN.
 *
 * Output
 * For each test case, print a single line containing one integer ― the desired number of pairs.
 *
 * Constraints
 * 1≤T≤20
 * 1≤N≤40,000
 * 0≤Ai≤10^9 for each valid i
 *
 * Subtasks
 * Subtask #1 (30 points): 1≤N≤500
 * Subtask #2 (70 points): original constraints
 *
 * Example Input
 * 2
 * 3
 * 2 4 2
 * 3
 * 0 2 3
 *
 * Example Output
 * 1
 * 0
 *
 * Explanation
 * Example case 1: The only valid pair is (1,3).
 * Example case 2: We can see that no valid pair exists.
 *
**/
#include <iostream>
#include <vector>
using namespace std;

extern int GetPairs(const vector<int>& A);

int main()
{
    int t=0, n=0;
    cin >> t;

    for (int i=0; i<t; i++){
        cin >> n;
        int nums=0;
        vector<int> A;

        for (int j=0; j<n; j++){
            cin >> nums;
            A.push_back(nums);
        }
        int numPairs = GetPairs(A);
        cout << numPairs <<endl;
    }
}

int GetPairs(const vector<int>& A)
{
    int count = 0;
    vector<int>::const_iterator it = A.begin();
    while(it != A.end())
    {
        int num = *it;
        // cout << "num: " << num << endl;
        if(num == 1){
            // cout << "num == 1 " << endl;
            it++;
            continue;
        }
        if(num % (num-1)){
            // cout << "num % (num-1)" << endl;
            it++;
            continue;
        }
        int B = int(num / (num - 1));
        // cout << "B: " << B << endl;
        vector<int>::const_iterator it2 = ++it;
        while(it2 != A.end()){
            if(*it2 == B){
                count++;
            }
            // cout << "num:"<< *it2 << " count:" << count << endl;
            it2++;
        }
    }
    return count;
}
