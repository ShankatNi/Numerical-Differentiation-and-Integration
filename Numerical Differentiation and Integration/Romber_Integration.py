import math

def func(numValue):
    #intAns=(numValue**2)*math.exp(numValue*(-1))
    intAns=3/(1+numValue**5)
    return intAns

def createList(n):  
    Q=list()
    for i in range(0,n+1):
        Q.append(list())
    length=n+1
    for i in Q:
        for cl in range(0,length):
            i.append(0)        
    return Q

def sigma(a,h,k):
    totValue=0
    for j in range(1,2**(k-2)+1):
        gap=a+(((2*j)-1)*h[k])
        totValue+=func(gap)
    return totValue
        


def main():
    a=0;b=2
    R=list()
    n=6
    R=createList(n)
    h=list()
    h.append(0)
    for k in range(1,n+1):
        h.append((b-a)/(2**(k-1)))

    R[1][1]=(h[1]/2)*(func(a)+func(b))
    
    for k in range(2,n+1):
        R[1][k]=0.5*(R[1][k-1]+h[k-1]*sigma(a,h,k))
        print()

        for j in range(2,k+1):
            R[j][k]=(4**(j-1)*R[j-1][k]-R[j-1][k-1])/(4**(j-1)-1)

    for cl in R:
        print(cl)



main()
