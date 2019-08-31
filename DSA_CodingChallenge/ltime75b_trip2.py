# cook your dish here
def trip(k, a):
    if k == 1 and len(a) > 0:
        return False
    elif k == 1 and a[0] == -1:
        a[0] = 1
        return True
    elif len(a) == 1:
        a[0] = -1
        return True

    k_lst = [i for i in range(1, k + 1)]
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            if i == 0:  # first and last element
                if k_lst[0] == a[i + 1]:
                    a[i] = k_lst[1]
                else:
                    a[i] = k_lst[0]
            elif i == len(a) - 1:  # last element. Check the second last
                if k_lst[0] == a[i - 1]:
                    a[i] = k_lst[1]
                else:
                    a[i] = k_lst[0]
            else:
                for k in range(len(k_lst)):
                    if k_lst[k] != a[i + 1] and k_lst[k] != a[i - 1]:
                        a[i] = k_lst[k]
                        break

    prev = 0
    for i in range(len(a)):
        if a[i] == -1:
            return False
        if a[i] == prev:
            return False
        prev = a[i]

    return True


def testmain():
    t = int(input())
    for case in range(t):
        n_k = input().split()
        n = int(n_k[0])
        k = int(n_k[1])
        a = list(map(int, input().split()))

        if True == trip(k, a):
            print('YES')
            print(" ".join(map(str, a)))
        else:
            print('NO')


if __name__ == '__main__':
    testmain()
