#Composite Trapezoid_Rule
import math

def function(tempValue):
    funcValue=tempValue*math.log(tempValue+1)
    return funcValue

def main():
    a=-0.5      #float(input("Enter end point a:"))
    b=0.5          #float(input("Enter end point b:"))
    n=6      #int(input("Enter positive integer n:"))
    h=(b-a)/(n+2)
    X_I0=function(a)+function(b)
    X_I2=0

    for i in range(0,n+1):
        X=a+(i+1)*h
        if i % 2 ==0:
            X_I2=X_I2+function(X)
            #print(X,X_I2)


    X_I=2*h*(X_I2)
    print("Final Answer",X_I)




main()
