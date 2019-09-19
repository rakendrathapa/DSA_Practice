"""
The Fibonacci sequence F0,F1,… is a special infinite sequence of non-negative integers, where F0=0, F1=1 and for each integer n≥2, Fn=Fn−1+Fn−2.

Consider the sequence D of the last decimal digits of the first N Fibonacci numbers, i.e. D=(F0%10,F1%10,…,FN−1%10). Now, you should perform the following process:

Let D=(D1,D2,…,Dl).
If l=1, the process ends.
Create a new sequence E=(D2,D4,…,D2⌊l/2⌋). In other words, E is the sequence created by removing all odd-indexed elements from D.
Change D to E.
When this process terminates, the sequence D contains only one number. You have to find this number.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.
Output
For each test case, print a single line containing one integer ― the last remaining number.


Example Input
1
9
Example Output
3
Explanation
Example case 1: The first N Fibonacci numbers are (0,1,1,2,3,5,8,13,21). The sequence D is (0,1,1,2,3,5,8,3,1)→(1,2,5,3)→(2,3)→(3)

"""
# cook your dish here
import math


# division of  large numbers
def l_Division(number, divisor):
    idx = 0;
    temp = int(number[idx])
    while temp < divisor:
        temp = temp * 10 + int(number[idx + 1])
        idx += 1
    idx += 1
    quo = 0
    while len(number) > idx:
        quo = quo * 10 + (temp // divisor)
        temp = (temp % divisor) * 10 + int(number[idx])
        idx += 1

    quo = quo * 10 + temp // divisor
    rem = temp % divisor
    return quo, rem


def isGreater(str1, str2):
    if len(str2) > len(str1):
        return False
    elif len(str1) > len(str2):
        return True

    for i in range(len(str1)):
        if int(str1[i]) == int(str2[i]):
            continue
        elif int(str1[i]) > int(str2[i]):
            return True
        else:
            return False
    return False


def fibonnaci():
    n = [0] * 60
    n[1] = n[2] = 1
    for i in range(3, 60):
        n[i] = (n[i - 1] + n[i - 2]) % 10
    return n


def testmain():
    t = int(input())
    fibArr = fibonnaci()
    intmax = 2 ** 31 - 1
    checkmax = str(intmax)

    for i in range(t):
        n = input()
        d = 0
        if False == isGreater(n, checkmax):
            num = int(n)
            exp = int(math.log2(num))
            d = (2 ** exp) % 60
        else:
            quo, rem = l_Division(n, 2 ** 31)
            exp = 31
            exp += int(math.log2(quo))
            d = (2 ** exp) % 60
        print(fibArr[d - 1])


if __name__ == '__main__':
    testmain()
