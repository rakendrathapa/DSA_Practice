/**
 * Problem Name: Easy Subsequence Selection
 *
 * You are given a string S with length N. Choose an integer K and two non-empty subsequences A and B of characters of this string, each with length K, such that:
 * A=B, i.e. for each valid i, the i-th character in A is the same as the i-th character in B.
 * Let's denote the indices of characters used to construct A by a1,a2,…,aK, i.e. A=(Sa1,Sa2,…,SaK).
 * Similarly, let's denote the indices of characters used to construct B by b1,b2,…,bK.
 * If we denote the number of common indices in the sequences a and b by M, then M+1≤K.
 *
 * Since Chef is busy right now, he asks you to find the maximum value of K such that it is possible to
 * find sequences A and B which satisfy the given conditions or determine that there is no such K.
 *
 * Input
 * The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
 * The first line of each test case contains a single integer N.
 * The second line contains a single string S with length N.
 *
 * Output
 * For each test case, print a single line containing one integer ― the maximum K, or 0 if there is no solution.
 *
 * Example Input
 * 1
 * 4
 * anxa
 *
 * Example Output
 * 1
 *
 **/

#include <iostream>
using namespace std;

extern int GetNumSubStrs(const string&);
int main()
{
    int n=0, s=0;
    string str;
    cin >> n;
    for (int i=0;i<s; i++)
    {
        cin >> s;
        cin >> str;
        int num = GetNumSubStrs(str);
        cout << num << endl;
    }
    return EXIT_SUCCESS;
}

int GetNumSubStrs(const string& str)
{

    return 0;
}
