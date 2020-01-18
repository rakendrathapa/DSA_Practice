/**
 * PROBLEM NAME: Alternating subarray prefix
 * There's an array A consisting of N non-zero integers A1..N.
 * A subarray of A is called alternating if any two adjacent elements in it have different signs (i.e. one of them should be negative and the other should be positive).
 *
 * For each x from 1 to N, compute the length of the longest alternating subarray that starts at x - that is, a subarray Ax..y for the maximum possible y ≥ x.
 * The length of such a subarray is y-x+1.
 *
 * Input
 * The first line of the input contains an integer T - the number of test cases.
 * The first line of each test case contains N.
 * The following line contains N space-separated integers A1..N.
 *
 * Output
 * For each test case, output one line with N space-separated integers - the lengths of the longest alternating subarray starting at x, for each x from 1 to N.
 *
 * Constraints
 * 1 ≤ T ≤ 10
 * 1 ≤ N ≤ 10^5
 * -10^9 ≤ Ai ≤ 10^9
 *
 * Example
 * Input:
 * 3
 * 4
 * 1 2 3 4
 * 4
 * 1 -5 1 -5
 * 6
 * -5 -1 -1 2 -2 -3
 *
 * Output:
 * 1 1 1 1
 * 4 3 2 1
 * 1 1 3 2 1 1
 *
 * Explanation
 * Example case 1. No two elements have different signs, so any alternating subarray may only consist of a single number.
 * Example case 2. Every subarray is alternating.
 * Example case 3. The only alternating subarray of length 3 is A3..5.
 */

#include <iostream>

using namespace std;

extern bool GetSolution(const long long* A, const int n);

int main()
{
    int t=0, n=0;
    long long A[100000] = {0};
    long long Ai = 0;
    cin >> t;
    while(t--)
    {
        cin >> n;
        for(int i=0; i<n; i++){
            cin >> Ai;
            A[i] = Ai;
        }

        if(GetSolution(A, n)){
            cout << endl;
        }
        else{
            cerr << "Error in the Index" << endl;
        }
    }

    return EXIT_SUCCESS;
}


bool GetSolution(const long long* A, const int n)
{
    if((A == nullptr) || (n == 0)){
        return false;
    }

    if(n == 1){
        cout << 1 << endl;
        return true;
    }

    int *memElem = new int[n]();
    memElem[n - 1] = 1;
    bool isPos = false;

    if(A[n - 1] > 0){isPos = true;}

    for(int i=n-2; i>=0; i--){
        if(((A[i] > 0) && (isPos == false)) || ((A[i] < 0) && isPos))
        {
            memElem[i] = 1 + memElem[i+1];
            isPos = !isPos;
        }else{
            memElem[i] = 1;
        }
    }

    for(int i=0; i<n; i++){
        cout << memElem[i] << " ";
    }
    delete[] memElem;
    return true;
}
