import LinkedList_Bags_Queues_Stacks.LinkedBag as LB
import sys
import math

def testmain():
    numbers = LB()

    data = sys.stdin.readlines()
    for value in data:
        numbers.add_element(float(value))

    N = numbers.size()

    sum = 0.0
    for value in numbers:
        sum += value

    mean = sum / N

    sum = 0.0
    for value in numbers:
        sum += (value - mean) ** 2
    std_dev = math.sqrt(sum / N - 1)

    print('Mean: {}\n Standard Deviation: {}'.format(mean, std_dev))


if __name__ == '__main__':
    testmain()

