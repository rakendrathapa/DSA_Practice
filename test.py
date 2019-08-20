def testfunction(cardstr):
    if cardstr is None:
        raise ValueError('Passed NULL string')

    intStr = list(map(cardstr, int))

    visited = [False] * len(str)
    queue = []
    
    for i in range(len(str)):
        if int(str[i]):
            queue.append(i)
            print('str[{}]:{}'.format(i, str[i]))
    
    if queue is None:
        return 0

    while queue:
        i = queue.pop(0)
        if str[i] == '1':
            visited[i] = True
            print('Visited Node:{}: str[{}]:{}'.format(i, i, str[i]))
            if i+1 < len(str):
                print('Before: str[{}]:{}'.format(i+1, str[i+1]))
                if str[i+1] == '0':
                    str[i+1] = '1'
                else:
                    str[i+1] = '0'
                print('After: str[{}]:{}'.format(i + 1, str[i + 1]))

                if visited[i+1] is False and str[i+1] == '1':
                    queue.append(i+1)

            if i-1 > 0:
                print('Before: str[{}]:{}'.format(i - 1, str[i - 1]))
                # str[i-1] = str(int(str[i-1]) ^ 1)
                if str[i-1] == '0':
                    str[i-1] = '1'
                else:
                    str[i-1] = '0'
                print('After: str[{}]:{}'.format(i - 1, str[i - 1]))
                if visited[i - 1] is False and str[i-1] == '1':
                    queue.append(i-1)
    count = 0
    for a in visited:
        print('Visited{}:{}', count, a)
        count += 1
        if a is False:
            return 0
    
    return 1


def main():
    #testcases = int(input())
    testcases = 1
    if testcases < 1 or testcases > 10**2:
        raise ValueError('Invalid testcases')

    for i in range(testcases):
        #str = input()
        cardstr = '1100001100010'
        val = testfunction(cardstr)
        if val:
            print('WIN')
        else:
            print('LOSE')
        

if __name__ == "__main__":
    main()
