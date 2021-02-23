import numpy as np
from math import sin, cos, pi
from scipy import integrate, optimize
import matplotlib.pyplot as plt

v_0 = 150.
m = 10
g = 32.17
rho = 0.00235
c_d = 0.5
a_ref = 15


# Define drag equation
def drag(v):
    return 0.5 * rho * v**2 * c_d * a_ref


# Define dynamics of projectile
def dynamics(_, states):
    x, y, v, gam = states
    return np.array([
        v * cos(gam),
        v * sin(gam),
        -drag(v) / m - g * sin(gam),
        -g / v * cos(gam)
    ])


# Define terminal event (note the addition of attributes to the function)
def hit_ground(_, states):
    return states[1]


hit_ground.terminal = True
hit_ground.direction = -1


# Define cost function
def cost(gam_0):
    # Propagate trajectory
    prop_sol = integrate.solve_ivp(
        dynamics, [0., 50.], np.array([0., 0., v_0, gam_0]), events=hit_ground)

    # Extract and return flight range
    x_f = prop_sol.y[0, -1]

    # Invert range for minimization
    return -x_f


# Solve optimization problem (Guess 45 deg which is no drag solution)
opt_sol = optimize.minimize(cost, np.array([pi/4]))
opt_gam_0 = opt_sol.x[0]

print('Optimal release angle is {0:.4f} degrees'.format(opt_gam_0 * 180 / pi))

############################################
# Create plots for illustration (not needed)
fig = plt.figure(0, figsize=(6.5, 3.5))

gam_0_range = np.linspace(0, pi/2, 15)
cost_range = np.array([cost(_gam_0) for _gam_0 in gam_0_range])

ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(gam_0_range * 180 / pi, -cost_range, label='range')
ax1.plot(opt_gam_0 * 180 / pi, -opt_sol.fun, 'x', label='optimal')
ax1.legend()
ax1.set_xlabel(r'launch angle, $\gamma_0$ [deg]')
ax1.set_ylabel('range, $x_f$ [ft]')

ax2 = fig.add_subplot(1, 2, 2)
for _gam_0 in gam_0_range:
    _prop_sol = integrate.solve_ivp(dynamics, [0., 50.], np.array([0., 0., v_0, _gam_0]),
                                    max_step=0.1, events=hit_ground)
    ax2.plot(_prop_sol.y[0, :], _prop_sol.y[1, :], color='C0')

_prop_sol = integrate.solve_ivp(dynamics, [0., 50.], np.array([0., 0.01, v_0, opt_gam_0]),
                                max_step=0.1, events=hit_ground)
ax2.plot(_prop_sol.y[0, :], _prop_sol.y[1, :], color='C1')

ax2.set_xlabel(r'$y$ [deg]')
ax2.set_ylabel('$x$ [ft]')

fig.subplots_adjust(wspace=0.33, bottom=0.15)

plt.show()
