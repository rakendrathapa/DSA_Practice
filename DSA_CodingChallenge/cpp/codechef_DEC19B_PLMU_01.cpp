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


struct Input;
template<typename T, size_t N, size_t M> struct CoefficientBinomial;

template<typename T> T read();
template<typename T> void read(T& obj);
istream& operator>>(istream& is, vector<unsigned long>& v);
void readTestcases(unsigned long T);
unsigned long compute(const Input& in);
unsigned long compute(const vector<unsigned long>& a, unsigned long N);
unsigned long CB(unsigned long n, unsigned long k);

struct Input
{
    Input()
    {
        read<vector<unsigned long>>(a);
    }

    vector<unsigned long> a;
};

template<typename T, size_t N, size_t M> struct CoefficientBinomial
{
    constexpr CoefficientBinomial() : a()
    {
        a[0][0] = 1;
        for (auto i = 1u; i < N; ++i)
        {
            a[i][0] = 1;
            for (auto j = 1u; j < M; ++j)
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j];
        }
    }

    T a[N][M];
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    readTestcases(read<unsigned long>());

    return 0;
}

unsigned long CB(unsigned long n, unsigned long k)
{
    static CoefficientBinomial<unsigned long, 40001, 3> cb;

    return cb.a[n][k];
}

unsigned long compute(const vector<unsigned long>& a, unsigned long N)
{
    unsigned long cntZero(0);
    unsigned long cntTwo(0);
    unsigned long r(0);

    for (unsigned long i = 0; i < N; ++i)
    {
        switch (a[i])
        {
        case 0:
            ++cntZero;
            break;

        case 2:
            ++cntTwo;

        default:
            break;
        }

    }

    return CB(cntZero, 2) + CB(cntTwo, 2);
}


template<typename T> T read()
{
    T n;
    cin >> n;
    return n;
}

template<typename T> void read(T& obj)
{
    cin >> obj;
}

istream& operator>>(istream& is, vector<unsigned long>& v)
{
    v.clear();

    const unsigned long n(read<unsigned long>());
    v.resize(n);

    for (unsigned long i = 0; i < n; ++i)
        read<unsigned long>(v[i]);

    return is;
}

void readTestcases(unsigned long T)
{
    for (unsigned long i = 0; i < T; ++i)
        cout << compute(Input()) << endl;
}

unsigned long compute(const Input& in)
{
    return compute(in.a, in.a.size());
}
