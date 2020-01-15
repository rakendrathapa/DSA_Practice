/**
 * PROBLEM NAME: Is this FFT
 * In a far away Galaxy of Tilky Way, there was a planet Tarth where the sport of
 * Tompetitive Toding was very popular. According to legends, there lived a setter
 * known for his love for crispy mathematical and implementation problems.
 *
 * Radhesh was applying for a research project for polynomial multiplication under
 * the world renowed professor Ms Geehtakoomaree. However, she pefers to take the
 * top cream layer of applicants, and hence designs a test for him.
 *
 * Given 2 polynomials P(x) and Q(x), need to print their product.
 *
 * Input:
 * The first line has a single integer T, denoting number of test cases per file.
 *
 * Next line has 2 integers N and M, each denoting number of terms in the polynomials P and Q respectively.
 * Note that the highest degree of those polynomials will be N−1 and M−1 respectively.
 *
 * The next line has N space separated integers denoting coefficients of the polynomial P,
 * starting from lowest power to highest power (i.e. the first number corresponds to coefficient of x0, the Nth one corresponds to coefficient of x^N−1)
 *
 * The next line has M space separated integers denoting coefficients of the polynomial Q,
 * starting from lowest power to highest power (i.e. the first number corresponds to coefficient of x0, the Mth one corresponds to coefficient of x^M−1)
 *
 * Output
 * N+M−1 integers, denoting the product of polynomials.
 * The first number should correspond to coefficient of x0 and similarly the last number should correspond to coefficient of x^N+M−2
 * (Recall that N and M were number of terms and hence highest degree of P(x) and Q(x) was N−1 and M−1 respectively).
 *
 * Sample Input:
 * 3
 * 2 2
 * 1 -1
 * 1 1
 * 3 2
 * 1 2 1
 * 0 1
 * 3 3
 * 1 2 1
 * 1 -2 1
 *
 * Sample Output:
 * 1 0 -1
 * 0 1 2 1
 * 1 0 -2 0 1
 *
 * EXPLANATION:
 * The first case corresponds to multiplication of (1 − x) and (1 + x). The answer for this is (1 − x^2).
 * The coefficients, starting from x0 are 1, 0 and −1 and the same is printed.
 *
 * The second test case corresponds to multiplication of (1 + 2x+ x^2) and (x).
 * the result is (0 + x + 2x^2+ x^3)
 */
#include <iostream>

using namespace std;

extern void GetSolution(int* poly_n, const int n, int* poly_m, const int m);
int main()
{
    int t=0, n=0, m=0;
    int n_term=0, m_term=0;
    cin >> t;
    int poly_n[1000] = {0};
    int poly_m[1000] = {0};
    while(t--)
    {
        cin >> n >> m;
        for (int i=0; i<n; i++){
            cin >> n_term;
            poly_n[i] = n_term;
        }

        for (int i=0; i<m; i++){
            cin >> m_term;
            poly_m[i] = m_term;
        }
        GetSolution(poly_n, n, poly_m, m);
    }
}

void GetSolution(int* poly_n, const int n, int* poly_m, const int m)
{
    int* coeff = new int[n+m]();
    for (int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            coeff[i+j] += poly_n[i]*poly_m[j];
        }
    }

    for (int i=0; i< n+m-1; i++){
        cout << coeff[i] << " ";
    }
    delete[] coeff;
}
