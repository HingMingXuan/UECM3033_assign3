import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#ode function
def ode(y, t, a, b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1),b*(-y1+y0*y1)]
    return dydt
    
if __name__ == "__main__":
    
    #part 1
    # initial value for y0 and y1 and the value for a and b
    initial_y0 = 0.1
    initial_y1 = 1.0
    a = 1.0
    b = 0.2
    
    # initialize the arguments
    initial_y = [initial_y0, initial_y1]
    # partitioning the time from t = 0 to 5 into 200 uniform partition
    t = np.linspace(0, 5, 200)
    # solving the nonlinear ODE system
    sol = odeint(ode, initial_y, t, args=(a,b))
    
    # Graph of y0 and y1 against t
    # plotting the graph for both y0 and y1 against t
    plt.plot(t, sol[:, 0], 'r', label='Prey y0 against t', color="red")
    plt.plot(t, sol[:, 1], 'b', label='Predator y1 against t', color="green")
    plt.title('y against t with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'r', label='Predator y1 against Prey y0')
    plt.title('Predator y1 against Prey y0 with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.show()
    
    ############################################
    
    # part 2 (To observe the sevsitivity)
    # changing the initial value for y0 and y1 and the value for a and b
    initial_y0 = 0.11
    initial_y1 = 1.0
    a = 1.0
    b = 0.2
    
    # initialize the arguments
    initial_y = [initial_y0, initial_y1]
    # partitioning the time from t = 0 to 5 into 200
    t = np.linspace(0, 5, 200)
    # solving the nonlinear ODE system1    
    sol2 = odeint(ode, initial_y, t, args=(a,b))
    
    # Graph of y0=0.11 and y1 against t
    plt.plot(t, sol2[:, 0], 'r', label='Prey y0 against t',color="red")
    plt.plot(t, sol2[:, 1], 'b', label='Predator y1 against t',color="green")
    plt.title('y against t with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.show()


    # plotting the graph for y1 against y0=0.11
    plt.plot(sol[:, 0],sol[:,1], 'r', label='Predator y1 against Prey y0')
    plt.title('Predator y1 against Prey y0 with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.show()
    