from Sorting import Sorting

def testmain():
    arr = [38, 27, 43, 3, 9, 82, 10, 12]
    arr2 = [12, 11, 13, 5, 6, 7]
    sort = Sorting.Sorting()
    sort.mergesort(arr2)
    print(arr2)


if __name__ == '__main__':
    testmain()
