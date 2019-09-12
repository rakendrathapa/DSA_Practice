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
import sys
def testmain2():
    t = 1
    for case in range(t):
        k = 3
        a = [1, 2, 3, 4, 5]
        if k == 0:
            return 0
        if len(a) <= k:
            return 1

        weighted_a = [sum(a[:i]) for i in range(len(a))]
        print(weighted_a)


        weighted_a = [a[i] for i in range(k-1)]
        weighted_a.extend([sum(a[i-k+1:i]) for i in range(k, len(a))])
        print(a)
        print(weighted_a)


def testmain():
    # t = int(input())
    t = 1
    for case in range(t):
        k = 2
        a = [1, 2, 3, 4, 5]
        a.sort()
        minimum = sum(a[:k])
        count = 1
        for i in range(len(a) + 1 - k):
            total = a[i]
            length = 0
            for j in range(i+1, range(len(a))):
                total += a[j]
                length += 1
                if length+1 >= k-1:
                    if minimum > total:
                        minimum = total
                        count = 1
                    elif minimum == total:
                        count += 1
                    total -= a[j - k]
                    length -= 1
        return count


if __name__ == '__main__':
    testmain2()


