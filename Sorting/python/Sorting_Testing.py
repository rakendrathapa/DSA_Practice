from .Sorting import Sorting

def testmain():
    mergesorttestcases = list()
    mergesorttestcases.append([38, 27, 43, 3, 9, 82, 10, 12])
    mergesorttestcases.append([12, 11, 13, 5, 6, 7])
    mergesorttestcases.append([1, 5, 7, 9, 4, 2, 3, 6, 8])

    sort = Sorting()
    print('sorting: mergesort')
    for case in mergesorttestcases:
        # print('Array:{}'.format(case))
        sort.mergesort(case)
        # print('Sorted:{}'.format(case))

    quicksorttestcases = list()
    quicksorttestcases.append([0])
    quicksorttestcases.append([38, 27, 43, 3, 9, 82, 10, 12])
    quicksorttestcases.append([12, 11, 13, 5, 6, 7])
    quicksorttestcases.append([1, 5, 7, 9, 4, 2, 3, 6, 8])
    print('sorting: quicksort')
    for case in quicksorttestcases:
        # print('Array:{}'.format(case))
        ans = sort.quicksort(case)
        print('Sorted:{}'.format(ans))


if __name__ == '__main__':
    testmain()
