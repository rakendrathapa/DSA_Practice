# cook your dish here
def testfunction(cardstr):
    if cardstr is None:
        raise ValueError('Passed NULL cardstring')

    cards = list(cardstr)
    # print(cards)
    count = 0
    for i in cards:
        if int(i)==1:
            count += 1

    if (count%2 != 0):
        print("WIN")
    else:
        print("LOSE")

def main():
    # testcases = int(input())
    testcases = 1
    if testcases < 1 or testcases > 10 ** 2:
        raise ValueError('Invalid testcases')

    for i in range(testcases):
        # cardstr = input()
        cardstr = '00110000'
        testfunction(cardstr)

if __name__ == "__main__":
    main()
