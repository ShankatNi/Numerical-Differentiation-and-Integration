#Composite Trapezoid_Rule
import math

def function(tempValue):
    funcValue=3/(1+tempValue**5)
    #funcValue=tempValue*math.log(tempValue)
    return funcValue

def main():
    a=0     #float(input("Enter end point a:"))
    b=2      #float(input("Enter end point b:"))
    n=225366     #int(input("Enter positive integer n:"))
    h=(b-a)/n
    
    X_I0=function(a)+function(b)
    X_I1=0
    for i in range(1,n):
        X_I1=X_I1+function(a+(i*h))
        
    X_I=h*(X_I0+2*X_I1)/2
    print("Final Answer:",X_I)

    


main()
