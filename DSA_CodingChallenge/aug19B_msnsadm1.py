# cook your dish here
def testfunction(As, Bs):
    maxVal=0
    for a,b in zip(As,Bs):
        if a<0 or a>50: return 0
        if b<0 or b>50: return 0
        if a or b:
            pt = a*20
            pt -= b*10
            if pt>maxVal: maxVal=pt
    return maxVal

def main():
    testcases=int(input())
    if testcases<1 or testcases>100: return 0
#        raise ValueError("Invalid value of testcases")
  
    for i in range(testcases):
        N = int(input())
        if N<1 or N>150: return 0
#            raise ValueError("Invalid value of N")
        As = input().split()
        As = list(map(int, As))
        Bs = input().split()
        Bs = list(map(int, Bs))
#        print("N:{}, size(As):{}, size(Bs):{}".format(N, len(As), len(Bs)))
        if N != len(As) and N != len(Bs): return 0
        maxVal=testfunction(As, Bs)
        print(maxVal)
  

if __name__ == "__main__":
    main()
