/**
 * PROBLEM NAME: LAPINDROMES
 *
 * Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character.
 * If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome,
 * since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes.
 * Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
 *
 * Your task is simple. Given a string, you need to tell if it is a lapindrome.
 *
 * Input:
 * First line of input contains a single integer T, the number of test cases.
 * Each test is a single line containing a string S composed of only lowercase English alphabet.
 *
 * Output:
 * For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
 *
 * Constraints:
 * 1 ≤ T ≤ 100
 * 2 ≤ |S| ≤ 1000, where |S| denotes the length of S
 *
 * Example:
 * Input:
 * 6
 * gaga
 * abcde
 * rotor
 * xyzxy
 * abbaab
 * ababc
 *
 * Output:
 * YES
 * NO
 * YES
 * YES
 * NO
 * NO
 **/
#include <iostream>

bool IsLapindrome(const std::string& str);
int main()
{
    int t=0;
    std::cin >> t;
    while(t--)
    {
        std::string str;
        std::cin >> str;
        if(IsLapindrome(str)){
            std::cout << "YES" << std::endl;
        }
        else{
            std::cout << "NO" << std::endl;
        }
    }
    return EXIT_SUCCESS;
}


bool IsLapindrome(const std::string& str)
{
    int i=0, j=0;
    int strLen = str.size();
    int hasharr[26] = {0};

    if(strLen % 2)
    {
        j = int(strLen / 2) + 1;
    }else{
        j = int(strLen / 2);
    }

    // std::cout << "j=" << j;
    while( j < strLen)
    {
        // std::cout << "i:" << i << " j:" << j << std::endl;
        // std::cout << "str[i]:" << str[i] << " int(str[i]):" << int(str[i] - 'a') << std::endl;
        // std::cout << "str[j]:" << str[j] << " int(str[j]):" << int(str[j] - 'a') << std::endl;

        hasharr[int(str[i] - 'a')]++;
        hasharr[int(str[j] - 'a')]--;
        j++;i++;
    }

    // std::cout << "hasharr[]:";
    for (i=0; i<26; i++){
        // std::cout << hasharr[i] << " ";
        if(hasharr[i]){
            return false;
        }
    }

    return true;
}
