import math


def func(x):
    return (2*x)/(x**2-9)
    
def newList():
    x=list()
    for cl in range(20):
        x.append(0)
    return x


def Adaptive(a,b,intTol,N,TOL,A,H,FA,FC,FB,S,L):
    APP=0
    i=1
    TOL[i]=10*intTol
    A[i]=a
    H[i]=(b-a)/2
    FA[i]=func(a)
    FC[i]=func(a+H[i])
    FB[i]=func(b)
    S[i]=(H[i]*(FA[i]+4*FC[i]+FB[i]))/3
    L[i]=1
    #NEWLIST
    FD=newList();FE=newList()
    while (i>0):
        FD=func(A[i]+H[i]/2)
        FE=func(A[i]+(3*H[i])/2)
        s1=(H[i]*(FA[i]+4*FD+FC[i]))/6
        s2=(H[i]*(FC[i]+4*FE+FB[i]))/6
        V=[0,A[i],FA[i],FC[i],FB[i],H[i],TOL[i],S[i],L[i]]

        #Set
        i=i-1
        if abs(s1+s2-V[7])<V[6]:
            APP+=(s1+s2)
        else:
            if V[8] >= N:
                return "Level Exceeded"
            else:
                i+=1
                A[i]=V[1]+V[5]
                FA[i]=V[3]
                FC[i]=FE
                FB[i]=V[4]
                H[i]=V[5]/2
                TOL[i]=V[6]/2
                S[i]=s2
                L[i]=V[8]+1
                #Another Set
                i+=1
                A[i]=V[1]
                FA[i]=V[2]
                FC[i]=FD
                FB[i]=V[3]
                H[i]=H[i-1]
                TOL[i]=TOL[i-1]
                S[i]=s1
                L[i]=L[i-1]

    return APP
            


def main():
    a=2  #int(input("Enter a:"))
    b=2.8  #int(input("Enter b:"))
    intTol=0.001  #int(input("Enter Tol:"))
    N=6  #int(input("Enter N:"))
    TOL=newList();A=newList();H=newList();FA=newList();FC=newList()
    FB=newList();S=newList();L=newList()
    print("Final Value:")
    print(Adaptive(a,b,intTol,N,TOL,A,H,FA,FC,FB,S,L))


main()
