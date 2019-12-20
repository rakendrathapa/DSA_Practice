/**
 * PROBLEM Name: Addition
 * Recently, Chef studied the binary numeral system and noticed that it is extremely
 * simple to perform bitwise operations like AND, XOR or bit shift on non-negative integers,
 * while it is much more complicated to perform arithmetic operations (e.g. addition, multiplication
 * or division).
 *
 * After playing with binary operations for a while, Chef invented an interesting algorithm for
 * addition of two non-negative integers A and B:
 *
 * function add(A, B):
 *  while B is greater than 0:
 *      U = A XOR B
 *      V = A AND B
 *      A = U
 *      B = V * 2
 *  return A
 *
 * Now Chef is wondering how fast this algorithm is.
 * Given the initial values of A and B (in binary representation),
 * he needs you to help him compute the number of times the while-loop of the algorithm is repeated.
 *
 * Input
 * The first line of the input contains a single integer T denoting the number of test cases.
 * The description of T test cases follows.
 * The first line of each test case contains a single string A.
 * The second line contains a single string B.
 *
 * Output
 * For each test case, print a single line containing one integer ― the number of iterations
 * the algorithm will perform during addition of the given numbers A and B.
 *
 * Constraints
 * 1≤T≤105
 * 1≤|A|,|B|≤105
 * A and B contain only characters '0' and '1'
 * the sum of |A|+|B| over all test cases does not exceed 106
 *
 * Subtasks
 * Subtask #1 (20 points): |A|,|B|≤30
 * Subtask #2 (30 points):
 * |A|,|B|≤500
 * the sum of |A|+|B| over all test cases does not exceed 10^5
 * Subtask #3 (50 points): original constraints
 *
 * Example Input
 * 3
 * 100010
 * 0
 * 0
 * 100010
 * 11100
 * 1010
 *
 * Example Output
 * 0
 * 1
 * 3
 *
 * Explanation
 * Example case 1: The initial value of B is 0, so while-loop is not performed at all.
 * Example case 2: The initial values of A and B are 0b0=0 and 0b100010=34 respectively.
 * When the while-loop is performed for the first time, we have:
 * U=34
 * V=0
 * A changes to 34
 * B changes to 2⋅0=0
 *
 * The while-loop terminates immediately afterwards, so it is executed only once.
 * Example case 3: The initial values of A and B are 0b11100=28 and 0b1010=10 respectively.
 * After the first iteration, their values change to 22 and 16 respectively.
 * After the second iteration, they change to 6 and 32, and finally, after the third iteration,
 * to 38 and 0.
 *
 **/

#include <iostream>
#include <string>

using namespace std;

extern int GetNumberOfLoops(string A, string B);

int main()
{
    int t=0;
    string A, B;

    cin >> t;
    for (int i=0; i<t; i++){
        cin >> A;
        cin >> B;
        int n = GetNumberOfLoops(A, B);
        cout << n << endl;
    }

    return 0;
}

int GetNumberOfLoops(string A, string B)
{
    int len_a = A.size();
    int len_b = B.size();
    int dist = 0, count = 0, maxi = 0;
    bool isLoop = false;

    if(len_a > len_b){
        dist = len_a - len_b;
        std::string zeros(dist, '0');
        B = zeros + B;
    }else{
        dist = len_b - len_a;
        std::string zeros(dist, '0');
        A = zeros + A;
    }

    // cout << "A:" << A << " B:" << B << endl;
    for(size_t i=0; i<B.size(); i++){
        if(B[i] ==  '1'){
            isLoop = true;
            break;
        }
    }
    if(isLoop == false){
        return 0;
    }

    for(size_t i=0; i<B.size(); i++){
        // cout << "A[" << i << "]=" << A[i] << " B[" << i << "]=" << B[i] << endl;
        // cout << "count=" << count << " maxi=" << maxi << endl;
        if((A[i]=='1') && (B[i]=='1')){
            count++;
            if(maxi < (count + 1)){
                maxi = count + 1;
            }
            count = 0;
        }
        else if ((A[i]=='1') || (B[i]=='1')){
            count++;
        }
        else{
            count = 0;
        }
    }
    if(maxi == 0){
        maxi = 1;
    }
    return maxi;
}
