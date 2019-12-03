def __getsubseq(arr, index, k, finalarr, sub, temp):
    print(temp)
    if index == len(arr):
        if len(temp) == k:
            finalarr.append(temp)
    else:

        if len(sub):
            if abs(arr[index] - sub[len(sub) - 1]) <= 5:
                temp = sub
                __getsubseq(arr, index + 1, k, finalarr, sub, temp)
                temp = [arr[index]]
                __getsubseq(arr, index + 1, k, finalarr, sub + [arr[index]], temp)
                return

        __getsubseq(arr, index + 1, k, finalarr, sub, temp)
        __getsubseq(arr, index + 1, k, finalarr, sub + [arr[index]], temp)


def __goodsubsequence(arr, p):
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] - arr[i - 1] > p:
            return 0
    return 1


def main():
    arr = [9, 8, 7, 1, 5, 6]
    k = 3
    val = 5

    arrlist = list()
    __getsubseq(arr, 0, k, arrlist, [], [])
    count = 0
    for a in arrlist:
        temp = count + __goodsubsequence(a, val)
        if temp <= 10**9 + 7:
            count = temp
        else:
            count = (count + __goodsubsequence(a, val)) % 10**9 + 7
    print(count)

if __name__ == '__main__':
    main()
