import heapq


def testmain():
    arr = [2, 3]
    minhandshakes = 0
    heapq.heapify(arr)

    while (len(arr) > 1):
        print(arr)
        m = heapq.heappop(arr)
        n = heapq.heappop(arr)
        minhandshakes += m * n
        heapq.heappush(arr, m + n)
    print(minhandshakes)


if __name__ == '__main__':
    testmain()
