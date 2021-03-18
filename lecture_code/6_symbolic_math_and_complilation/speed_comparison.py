import numba
import sympy
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
from math import sin
import time

# Implement ODE for pendulum different ways to compare speed

num_iter = 10
y0 = np.array([np.pi/4, 0])
t_span = [0, 10]
g, r, k = 32, 1, 1


def integrate_func(func):
    return scipy.integrate.solve_ivp(func, t_span, y0, args=[g, r, k], max_step=0.01)


def plot_test(func):
    sol = integrate_func(func)
    plt.plot(sol.t, sol.y[0, :])
    plt.xlabel(r'Time, $t$')
    plt.ylabel(r'Angle, $\theta$')
    plt.show()


def pendulum_speed_test(func):
    t0 = time.time()
    # for _ in range(num_iter):
    #     __ = integrate_func(func)

    for _ in range(10000):
        __ = func(0, y0, g, r, k)

    tf = time.time()
    print(tf - t0)
    return tf - t0


# Python
def python_func(_, _y, _g, _r, _k):
    return np.array([_y[1], -_g/_r * sin(_y[0]) - _k * _y[1]])


# plot_test(python_func)
pendulum_speed_test(python_func)

# SymPy
sym_dyn = sympy.sympify(np.array(['theta_dot', '-g/r * sin(theta) - k*theta_dot']))
sympy_func = lambda _, _y, _g, _r, _k: sym_dyn.subs({'theta': _y[0], 'theta_dot': _y[1], 'g': _g, 'r': _r, 'k': _k})
# plot_test(sympy_func)
# pendulum_speed_test(sympy_func)

# Lambdify
lambdify_func = sympy.lambdify(['t', np.array(['theta', 'theta_dot']), 'g', 'r', 'k'], sym_dyn)
# plot_test(lambdify_func)
# pendulum_speed_test(lambdify_func)

# Numba JIT
jit_func = numba.njit((numba.float64, numba.float64[:], numba.float64, numba.float64, numba.float64))(python_func)
# plot_test(jit_func)
pendulum_speed_test(jit_func)

# Numba JIT w/ lambdify
jit_lambdify_func = \
    numba.njit((numba.float64, numba.float64[:], numba.float64, numba.float64, numba.float64))(lambdify_func)
# plot_test(jit_lambdify_func)
pendulum_speed_test(jit_lambdify_func)
