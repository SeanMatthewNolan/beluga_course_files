import beluga
import logging

ocp = beluga.Problem()

ocp.independent('t', 's')

ocp.state('x', 'v*cos(theta)', 'ft')
ocp.state('y', 'v*sin(theta)', 'ft')
ocp.state('v', 'g*sin(theta)', 'ft/s')

ocp.control('theta', 'rad')

ocp.constant('g', -32.17, 'ft/s**2')

ocp.constant('x_f', 0, 'ft')
ocp.constant('y_f', 0, 'ft')

ocp.path_cost('1', '1')

ocp.initial_constraint('t', 's')
ocp.initial_constraint('x', 'ft')
ocp.initial_constraint('y', 'ft')
ocp.initial_constraint('v', 'ft/s')

ocp.terminal_constraint('x - x_f', 'ft')
ocp.terminal_constraint('y-y_f', 'ft')

ocp.scale(ft='y', s='y/v', rad=1)

bvp_solver = beluga.bvp_algorithm('Shooting')

guess_maker = beluga.guess_generator(
    'auto',
    start=[0, 0, 0],
    costate_guess=-0.1,
    control_guess=[-3.14159/2],
    use_control_guess=True,
    time_integrate=0.1
)

beluga.add_logger(display_level=logging.INFO)

continuation_steps = beluga.init_continuation()

continuation_steps.add_step('bisection') \
    .num_cases(21) \
    .const('x_f', 10) \
    .const('y_f', -10)

sol_set = beluga.solve(
    ocp=ocp,
    method='indirect',
    bvp_algorithm=bvp_solver,
    steps=continuation_steps,
    guess_generator=guess_maker,
    autoscale=True,
    initial_helper=True,
    save_sols='brachisto.beluga'
)
