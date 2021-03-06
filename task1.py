import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    # Using the legendre function to obtain the nodes and weights with any n from 1 to 100
    # x is the nodes, w is the weights
    x, w = np.polynomial.legendre.leggauss(n)
    # Transforming the x value into the integral from the interval [-1,1] to [a,b]
    transformed_x = (b-a)*x/2 + ((b+a)/2)    
    # The answer is calculated out by using the Gauss-Legendre Quadrature formula
    # (b-a)/2 is the jacobian of the transformation
    ans = ((b-a)/2)*sum(w*f(transformed_x))


    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))
