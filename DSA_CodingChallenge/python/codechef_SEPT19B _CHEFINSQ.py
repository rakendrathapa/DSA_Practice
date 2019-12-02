"""
Chef has a sequence A1, A2, …,AN. This sequence has exactly 2^N subsequence. Chef considers a subsequence of A interesting if its size is exactly K and the sum of all its elements is minimum possible, i.e. there is no subsequence with size K which has a smaller sum.
Help Chef find the number of interesting subsequence of the sequence A.
Input
• The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
• The first line of each test case contains two space-separated integers N and K.
• The second line contains N space-separated integers A1, A2,…,AN

Output
For each test case, print a single line containing one integer ― the number of interesting subsequence.

Constraints
• 1≤T≤10
• 1≤K≤N≤50
• 1≤Ai≤100 for each valid I

Subtasks
Subtask #1 (30 points): 1≤N≤20
Subtask #2 (70 points): original constraints
Example Input
1
4 2
1 2 3 4

Example Output
1

Explanation
Example case 1: There are six subsequence with length 2: (1,2), (1,3), (1,4), (2,3), (2,4 and (3,4). The minimum sum is 3 and the only subsequence with this sum is (1,2).

"""
from math import factorial as fact
from collections import defaultdict

def testmain(A, k):
    # n, k = map(int, input().split())
    # l = list(map(int, input().split()))
    n = len(A)
    hash_arr = defaultdict(int)
    for i in A:
        hash_arr[i]+=1
    r = 1
    for j in hash_arr:
        if j<=k:
            k-=j
        else:
            r*=fact(j)/(fact(k)*fact(j-k))
            k-=j
        if k<0:
            break
    print(int(r))

if __name__ == '__main__':
    k = 3
    a = [1, 2, 3, 4, 5, 6, 7]
    testmain(a, k)


