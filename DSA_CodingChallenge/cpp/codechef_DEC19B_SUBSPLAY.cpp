/**
 * PROBLEM NAME: Easy Subsequence Selection
 * You are given a string S with length N. Choose an integer K and two non-empty subsequences A and B
 * of characters of this string, each with length K, such that:
 * A=B, i.e. for each valid i, the i-th character in A is the same as the i-th character in B.
 * Let's denote the indices of characters used to construct A by a1,a2,…,aK, i.e. A=(Sa1,Sa2,…,SaK).
 * Similarly, let's denote the indices of characters used to construct B by b1,b2,…,bK.
 * If we denote the number of common indices in the sequences a and b by M, then M+1≤K.
 *
 * Input
 * The first line of the input contains a single integer T denoting the number of test cases.
 * The description of T test cases follows.
 * The first line of each test case contains a single integer N.
 * The second line contains a single string S with length N.
 *
 * Output
 * For each test case, print a single line containing one integer ― the maximum K,
 * or 0 if there is no solution.
 *
 * Constraints
 * 1≤T≤100
 * 1≤N≤105
 * S contains only lowercase English letters
 *
 * Example Input
 * 1
 * 4
 * anxa
 * Example Output
 * 1
 **/
#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

extern void PrintSubStrings(const string& input);
extern int GetMaxSubStringLen(const string&);
int main()
{
    int t=0, l=0;
    string input;

    cin >> t;
    for (int i=0; i<t; i++){
        cin >> l;
        cin >> input;
        // PrintSubStrings(input);
        int n = GetMaxSubStringLen(input);
        cout << n << endl;
    }

    return 0;
}

void PrintSubStrings(const string& input)
{
    cout << input.length() << " " << int(input.length()/2) << endl;
    for (int j=1; j<=int(input.length()/2); j++){
        for(int i=0; i <= int(input.length() - j); i+=j){
            cout << "Substr: " << input.substr(i, j) << endl;
        }
    }
}

/*
int GetMaxSubStringLen(const string& input)
{
    int maxVal=0;
    map<string, int> substrNums;

    for (int j=1; j<=int(input.length()/2); j++){
        for(int i=0; i <= int(input.length() - j); i+=j){
            string candidate = input.substr(i, j);
            map<string, int>::iterator it = substrNums.find(candidate);
            if(it == substrNums.end()){
                substrNums.insert({candidate, 0});
            }else{
                if (maxVal < j) maxVal = j;
                 (it->second)++;
            }
        }
    }
    return maxVal;
}
*/

int GetMaxSubStringLen(const string& input)
{
    // object from the class stringstream
    unsigned char arr[26]={0}, prev[26]={0};
    int dist=0, min=9999999;
    for (size_t count=0; count < input.size(); count++ ){
        // arr[(int)input[count] - 'a'] = count;
        arr[(int)input[count] - 'a']++;

        if(arr[(int)input[count] - 'a'] > 1){
            dist = count - prev[(int)input[count] - 'a'];
            if(dist < min){
                min = dist;
            }
            prev[(int)input[count] - 'a'] = count;
        }
    }
    if (min != 9999999){
        // cout << input.size() - min << endl;
        return input.size() - min;
    }
    return 0;
}
