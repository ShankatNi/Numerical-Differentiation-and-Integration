#Composite Simpson_Rule
import math

def function(tempValue):
    funcValue=1/(1+tempValue**5)
    #print(tempValue,math.log(tempValue+1),"=",funcValue)
    return funcValue

def main():
    print("Composite Simpson Rule")
    a=0      #float(input("Enter end point a:"))
    b=2      #float(input("Enter end point b:"))
    n=6     #int(input("Enter even positive integer n:"))
    h=(b-a)/n
    X_I0=function(a)+function(b)
    X_I1=0
    X_I2=0
    print("h",h)
    print("a",a,function(a))
    
    for i in range(1,n):
        X=a+i*h
        if i % 2 ==0:
            X_I2=X_I2+function(X)
            print("Other Even",i,X,X_I2,function(X))
        else:
            X_I1=X_I1+function(X)
            print("Other Odd",i,X,function(X))

    X_I=h*(X_I0+2*X_I2+4*X_I1)/3
    print("b",b,function(b))
    
    print("Final Answer:",X_I)



main()
