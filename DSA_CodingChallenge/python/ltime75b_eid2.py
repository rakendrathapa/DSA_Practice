# cook your dish here
# cook your dish here
def __checkFairness(valintlist):
    ageArr = [0] * 18
    age_cost = zip(valintlist[0:3], valintlist[3:])

    for i, j in age_cost:
        if ageArr[i] != 0:
            if j == ageArr[i]:
                continue
            else:
                return 'NOT FAIR'
        else:
            ageArr[i] = j

    count = 0
    for age in ageArr:
        if age == 0:
            continue
        if age <= count:
            return 'NOT FAIR'
        count = age
    return 'FAIR'


def testmain():
    t = int(input())
    for case in range(t):
        val = input()
        valintlist = list(map(int, val.split()))
        print(__checkFairness(valintlist))


if __name__ == '__main__':
    testmain()
