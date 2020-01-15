/**
 * PROBLEM NAME: Radhesh and Hashing
 * In a far away Galaxy of Tilky Way, there was a planet Tarth where the sport of Tompetitive Toding was very popular.
 * According to legends, there lived a setter known for his complex cryptography problems.
 *
 * Radhesh is learning Hashing!! He has a string S consisting only of lowercase English alphabets.
 * To each alphabet, he assigns a value, i.e. a is assigned 0, b is assigned 1, …, and z is assigned 25.
 * Now, hash of a string S is sum of values of all of its characters.
 *
 * Now Ms Geethakoomaree, his Cryptography teacher, says that the hash function is poor because there can be multiple strings with same hash value.
 * Hence, given a string S, you need to find its hash and another string P of same length (which is not same as S) with same hash.
 * In case multiple P exists, print the lexicographically smallest one. If no such string exists, print −1.
 *
 * Input:
 * The first line has a single integer T, denoting number of test cases per file.
 * The only line of each testcase contains the string S.
 *
 * Output:
 * For each test case, in a new line, print the hash value of the string S and another string P (with same hash value and same length as S )
 * separated by a space. If no such P exists, print -1 instead of P. If multiple P exists, print just the lexicographically smallest one.
 *
 *
 * Constraints
 * 1≤T≤10^5
 * 1≤|S|≤10^5
 * Sum of |S| over the entire test file does not exceed 10^6
 * S consists of only lowercase english alphabets.
 *
 * Subtasks
 * Subtask 1 (10% points): |S|≤5.
 * Subtask 2 (20% points): Input string is lexicographically largest string of that hash value and that length.
 * Subtask 2 (70% points): Original Constraints.
 *
 * Sample Input:
 * 2
 * abz
 * yzz
 *
 * Sample Output:
 * 26 acy
 * 74 zyz
 *
 * EXPLANATION:
 * For first case, the hash value is 0+1+25=26. We can confirm that out of all possible strings, acy is lexicographically smallest.
 * For second test case, we have only 3 possible strings with same hash, yzz, zyz and zzy.
 * Out of these, yzz is same as S and hence rejected, zyz is hence printed as its lexicographically smaller than zzy.
 **/

#include <iostream>
#include <string>

using namespace std;

extern void GetSolution(string& s);
int main()
{
    int t=0;
    string s;
    cin >> t;
    while(t--){
        cin >> s;
        GetSolution(s);
    }
    return EXIT_SUCCESS;
}

void GetSolution(string& s)
{
    if(s.empty()){
        return;
    }

    int sum=0;

    for(size_t i=0; i<s.size(); i++)
    {
        sum += (s[i]-'a');
    }

    cout << sum << " " << "-1" << endl;

}
