import beluga
import logging
import numpy as np

re = 6.3781e6
h_0 = 50e3
h_f = 0
theta_f = 2250e3/re
v_0 = 4e3
gam_0 = -0.25/180*3.14159

ocp = beluga.Problem()

ocp.independent('t', 's')

ocp.state('h', 'v*sin(gam)', 'm')
ocp.state('theta', 'v*cos(gam)/r', 'rad')
ocp.state('v', '-D/mass - mu*sin(gam)/r**2', 'm/s')
ocp.state('gam', 'L/(mass*v) - mu/(v*r**2)*cos(gam) + v/r*cos(gam)', 'rad')

ocp.quantity('rho', 'rho0*exp(-h/H)')
ocp.quantity('Cl', 'cl1 * alpha')
ocp.quantity('Cd', 'cd2 * alpha**2 + cd0')
ocp.quantity('D', '0.5*rho*v**2*Cd*aref')
ocp.quantity('L', '0.5*rho*v**2*Cl*aref')
ocp.quantity('r', 're+h')

ocp.control('alpha', 'rad')

ocp.constant('mu', 3.986e14, 'm**3/s**2')  # Gravitational parameter, m**3/s**2
ocp.constant('rho0', 1.2, 'kg/m**3')  # Sea-level atmospheric density, kg/m**3
ocp.constant('H', 7500, 'm')  # Scale height for atmosphere of Earth, m
ocp.constant('mass', 750/2.2046226, 'kg')  # Mass of vehicle, kg
ocp.constant('re', re, 'm')  # Radius of planet, m
ocp.constant('aref', np.pi*(24*0.0254/2)**2, 'm**2')  # Reference area of vehicle, m**2

ocp.constant('cl0', 0, '1')
ocp.constant('cl1', 1.5658, '1')
ocp.constant('cd0', 0.0612, '1')
ocp.constant('cd2', 1.6537, '1')

ocp.constant('h_0', h_0, 'm')
ocp.constant('v_0', v_0, 'm/s')
ocp.constant('gam_0', gam_0, 'rad')

ocp.constant('h_f', h_f, 'm')
ocp.constant('theta_f', theta_f, 'rad')

# Define costs
ocp.terminal_cost('-v**2', 'm**2/s**2')

# Define constraints
ocp.initial_constraint('h-h_0', 'm')
ocp.initial_constraint('theta', 'rad')
ocp.initial_constraint('v-v_0', 'm/s')
ocp.initial_constraint('gam-gam_0', 'rad')
ocp.initial_constraint('t', 's')

ocp.terminal_constraint('h-h_f', 'm')
ocp.terminal_constraint('theta-theta_f', 'rad')

ocp.scale(m='h', s='h/v', kg='mass', rad=1)

bvp_solver = beluga.bvp_algorithm('spbvp')

guess_maker = beluga.guess_generator(
    'auto',
    start=[h_0, 0., v_0, -45/180*np.pi],
    direction='forward',
    costate_guess=[-1e5, -0.01, -0.01, -0.01],
    control_guess=[5/180*np.pi],
    time_integrate=1
)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(21) \
    .const('h_f', 0) \
    .const('theta_f', 50e3/re)

continuation_steps.add_step('bisection') \
    .num_cases(81) \
    .const('theta_f', 300e3/re)

continuation_steps.add_step('bisection') \
    .num_cases(41) \
    .const('gam_0', gam_0)

continuation_steps.add_step('bisection') \
    .num_cases(151) \
    .const('theta_f', theta_f)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    optim_options={'control_method': 'differential'},
    initial_helper=True,
    save_sols='hyper_example.beluga',
    autoscale=True
)
