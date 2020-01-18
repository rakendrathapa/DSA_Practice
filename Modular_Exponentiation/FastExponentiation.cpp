/**
 * ALGORITHM NAME: Modular Exponentiation (Power in Modular Arithmetic)
 *
 * Given three numbers x, y and p, compute (xy) % p.
 **/

#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

extern int GetModulo(int n, int exp, int mod);
int main()
{
    cout << "TEST PROGRAM" << endl;
    int t=0;
    int n=0, exp=0, mod=0;
    int modulo=0;
    cin >> t;
    while(t--)
    {
        cin >> n >> exp >> mod;
        modulo = GetModulo(n, exp, mod);
        cout << "Ans: Modulo: " << modulo << endl;
    }

    return EXIT_SUCCESS;
}

int GetModulo(int n, int exp, int mod)
{
    if(mod==0){
        throw runtime_error("Math Error: Division by Zero");
    }

    if(n==0){
        return 0;
    }

    if (exp==0){
        return mod;
    }

    bool isNeg = false;
    if(n<0){
        isNeg = true;
    }

    vector<long long> mod_iter;
    long long t_e=1, t_m=(n % mod);
    int count = 0;
    mod_iter.push_back(t_m);

    cout << count++ << ". Exp:" << t_e << " Mod:" << t_m << endl;
    while((t_e = t_e*2) <= exp){
        // t_e = t_e * 2;
        t_m = t_m * t_m;
        t_m = t_m % mod;
        cout << count++ <<". Exp:" << t_e << " Mod:" << t_m << endl;
        mod_iter.push_back(t_m);
    }

    int i=0;
    long long total_mod = 1;
    while (exp)
    {
        if(exp & 0x1){
            total_mod = (total_mod * mod_iter[i]) % mod;
            cout << "i:" << i << " Mod:" << mod_iter[i] << " Cumulative Mod:" << total_mod << endl;
        }
        exp = exp >> 1;
        i++;
    }

    return total_mod;
}
