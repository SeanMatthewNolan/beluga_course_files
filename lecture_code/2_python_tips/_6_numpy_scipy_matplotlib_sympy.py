#  NumPy gives array functionality like MATLAB (see: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
import numpy as np

# Initializing 1D array
arr1 = np.array([1., 2., 3., 4.])

# Initializaing 2D array
arr2 = np.array([[0., 1.], [2., 3.]])

# Mathematical operations on arrays

# Linear Spaced Array
arr3 = np.linspace(0, 10, 100)

# Scipy provides advance scientific computing algorithms
import scipy

# ODE solving
from scipy.integrate import solve_ivp


def deriv_func(_, _x):
    return np.array([-_x[1], _x[0]])


sol = solve_ivp(deriv_func, [0, 10], [0, 1])

# Matplotlib supplies plotting functionality
import matplotlib.pyplot as plt

plt.plot(sol.t, sol.y[0, :], label=r'$x_1$')
plt.plot(sol.t, sol.y[1, :], label=r'$x_2$')
plt.title('Example Plot')
plt.xlabel('Time, t')
plt.ylabel('State, x')
plt.show()
