def testfunction(cardstr):
    if cardstr is None:
        raise ValueError('Passed NULL cardstring')

    cards = list(map(int, cardstr))
    visited = [False] * len(cards)
    queue = []

    for i in range(len(cards)):
        if cards[i]:
            queue.append(i)
            print('card[{}]:{}'.format(i, cards[i]))

    if queue is None:
        return 0

    while queue:
        i = queue.pop(0)
        if cards[i] == 1:
            visited[i] = True
            print('Visited Node:{}: cards[{}]:{}'.format(i, i, cards[i]))

            if i + 1 < len(cards):
                print('Before: cards[{}]:{}'.format(i + 1, cards[i + 1]))
                cards[i + 1] = cards[i + 1] ^ 1
                print('After: cards[{}]:{}'.format(i + 1, cards[i + 1]))
                if visited[i + 1] is False and cards[i + 1] == 1:
                    queue.append(i + 1)

            if i - 1 > 0:
                print('Before: cards[{}]:{}'.format(i - 1, cards[i - 1]))
                cards[i - 1] = cards[i - 1] ^ 1
                print('After: cards[{}]:{}'.format(i - 1, cards[i - 1]))
                if visited[i - 1] is False and cards[i - 1] == 1:
                    queue.append(i - 1)
    count = 0
    for a in visited:
        print('Visited{}:{}', count, a)
        count += 1
        if a is False:
            return 0

    return 1


def main():
    # testcases = int(input())
    testcases = 1
    if testcases < 1 or testcases > 10 ** 2:
        raise ValueError('Invalid testcases')

    for i in range(testcases):
        # cardstr = input()
        cardcardstr = '00110000'
        val = testfunction(cardcardstr)
        if val:
            print('WIN')
        else:
            print('LOSE')


if __name__ == "__main__":
    main()
