/**
 * PROBLEM NAME: Lost Guy Radhu
 *
 * Far away in Lonely lands of Sahoo village there lived mathematically advanced guy. Let's call him the lost guy because he remains lost in his Mathematical courses.
 * One of the games he is playing is "Dab the Tab". This game is so addictive that he isn't doing anything else and played this game N times in a single day,
 * getting a score of Ai in the i-th game. After every game, the Maximum Score among all games played till now, is displayed.
 *
 * Next day, he was bored at work, and was thinking about the gaming session the previous day. In particular, he had Q thoughts,
 * where each thought involves wondering what Maximum Score was displayed after the i-th game. He wants you to help him resolve these thoughts.
 * That is, he has Q questions, where each question consists of a single integer qi. For this, you should tell him what the Maximum Score was, after the qi game.
 *
 * Input:
 * First line will contain T, number of testcases. Then the testcases follow.
 * Each testcase begins with two integers, N and Q, denoting the number of games played and the number of queries.
 * Next Line contains N integers: A1,A2,…,AN, the scores in the N games playes.
 * Next Line contains Q integers, q1q2…qQ, where qi denotes the i-th query.
 *
 * Output:
 * For each query, print the Maximum Score in a new line
 *
 * Constraints
 * 1≤T≤10
 * 1≤N,Q≤105
 * 0≤Ai≤MX
 * 1≤qi≤N
 *
 * Subtasks
 * Subtask 1 (15% points): N≤100,Q≤10^4 and MX=1000
 * Subtask 2 (20% points): N≤1000,Q≤10^5 and MX=10^9
 * Subtask 3 (65% points): N≤105,Q≤10^5 and MX=10^9.
 *
 * Sample Input:
 * 1
 * 5 3
 * 5 4 8 6 9
 * 2 3 5
 * Sample Output:
 * 5
 * 8
 * 9
 *
 * EXPLANATION:
 * For first thought, maximum score is max(5,4)=5.
 * For second thought, maximum score is max(5,4,8)=8.
 */
#include <iostream>
#include <cstddef>
#include <limits>
#include <vector>

using namespace std;

extern void GetSolution(const int* Ai, const int nAi, const int* queries, const int nqueries);

int main()
{
     std::cout << "short: " << std::dec << std::numeric_limits<short>::max()
              << " or " << std::hex << std::showbase << std::numeric_limits<short>::max() << '\n'
              << "int: " << std::dec << std::numeric_limits<int>::max()
              << " or " << std::hex << std::numeric_limits<int>::max() << '\n' << std::dec
              << "long: " << std::dec << std::numeric_limits<long>::max()
              << " or " << std::hex << std::numeric_limits<long>::max() << '\n' << std::dec
              << "long long: " << std::dec << std::numeric_limits<long long>::max()
              << " or " << std::hex << std::numeric_limits<long long>::max() << '\n' << std::dec
              << "streamsize: " << std::dec << std::numeric_limits<std::streamsize>::max()
              << " or " << std::hex << std::numeric_limits<std::streamsize>::max() << '\n'
              << "size_t: " << std::dec << std::numeric_limits<std::size_t>::max()
              << " or " << std::hex << std::numeric_limits<std::size_t>::max() << '\n'
              << "float: " << std::numeric_limits<float>::max()
              << "double: " << std::numeric_limits<double>::max()
              << std::endl;

    int t=0, n=0, q=0;
    int Ai[100000] = {0};
    int queries[100000] = {0};

    cin >> t;
    while(t--)
    {
        cin >> n >> q;
        for(int i=0; i<n; i++){
            cin >> Ai[i];
        }

        for(int i=0; i<q; i++){
            cin >> queries[i];
        }

        GetSolution(Ai, n, queries, q);
    }

    return 0;
}

void GetSolution(const int* Ai, const int nAi, const int* queries, const int nqueries)
{
    int* maxAi = new int[nAi]();
    int maxi = -1;
    for (int i=0; i< nAi; i++){
        if(maxi < Ai[i]){
            maxi = Ai[i];
        }
        maxAi[i] = maxi;
    }

    // cout << "\nRESULT:" << endl;
    for (int i=0; i<nqueries; i++){
        cout << maxAi[queries[i] - 1] << endl;
    }
    delete[] maxAi;
}

