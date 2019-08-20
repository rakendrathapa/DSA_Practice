from LinkedList_Bags_Queues_Stacks import LinkedBag as LB
import math

def testmain():
    numbers = LB.LinkedBag()

    data = "10, 5, 6, 7, 2, 6, 78, 92"
    data = data.split(',')
    data = list(map(int, data))

    for value in data:
        numbers.add_element(float(value))

    N = numbers.size()
    print("N:{} numbers:{}".format(N, numbers))

    sum = 0.0
    # for value in numbers.get_element():
    for value in numbers:
        print(value)
        sum += value

    mean = sum / N
    sum = 0.0

    for value in numbers:
        sum += (value - mean) ** 2
    std_dev = math.sqrt(sum / N - 1)

    print('Mean: {}\n Standard Deviation: {}'.format(mean, std_dev))


if __name__ == '__main__':
    testmain()

