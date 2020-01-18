/**
 * PROBLEM NAME: Count Substring
 * Given a string S consisting of only 1s and 0s, find the number of substrings which start and end both in 1.
 *
 * In this problem, a substring is defined as a sequence of continuous characters Si, Si+1, ..., Sj where 1 ≤ i ≤ j ≤ N.
 *
 * Input
 * First line contains T, the number of testcases. Each testcase consists of N(the length of string) in one line and string in second line.
 *
 * Output
 * For each testcase, print the required answer in one line.
 *
 * Constraints
 * 1 ≤ T ≤ 10^5
 * 1 ≤ N ≤ 10^5
 * Sum of N over all testcases ≤ 10^5
 *
 * Example
 * Input:
 * 2
 * 4
 * 1111
 * 5
 * 10001
 *
 * Output:
 * 10
 * 3
 *
 * Explanation
 * #test1: All substrings satisfy.
 * #test2: Three substrings S[1,1], S[5,5] and S[1,5] satisfy.
 */

#include <iostream>

using namespace std;

extern int GetSolution(string& s, int len);
int main()
{
    int t=0, n=0;
    string s;

    cin >> t;
    while(t--){
        cin >> n;
        cin >> s;
        cout << GetSolution(s, n) << endl;
    }
    return 0;
}

int GetSolution(string& s, int len)
{
    int count=0;
    for(int i=0; i<len; i++){
        // cout << "s[" << i << "]: " << s[i] << " ";
        if(s[i] == '1'){
            count++;
        }
    }
    return count + count * (count - 1) / 2;
}
