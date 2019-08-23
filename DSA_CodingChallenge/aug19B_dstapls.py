# cook your dish here
def division(dividend, divisor):
    # this function divides large integer string integer with integer.
    mod = 0  # check at the end if this is 0 else throw ValueError in this case
    quo = 0  # to return
    for a in dividend:
        quo *= 10
        val = mod * 10 + int(a)
        quo += int(val / divisor)
        mod = val % divisor
        # print("quo:{} mod:{}".format(quo, mod))
    if mod: raise ValueError("Apples Does not divide baskets")
    return quo

def testfunction(apples, baskets):
    #print("apples:{} baskets:{}".format(apples, baskets))
    val = division(apples, baskets)
    if val % baskets: return("YES")
    return("NO")

def main():
    testcases = int(input())
    if testcases < 1 or testcases > 250: raise ValueError("Invalid testcases parameter")
    for a in range(testcases):
        n_k = input().split()
        apples = n_k[0]
        baskets = int(n_k[1])

        #if apples < 1: raise ValueError("Invalid number of apples")
        if baskets < 1: raise ValueError("Invalid number of baskets")
        #if(apples%baskets): raise ValueError("baskets cannot divide apples")

        value = testfunction(apples, baskets)
        print(value)

if __name__ == "__main__":
    main()
