import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from beluga.utils import load
from matplotlib.colors import LinearSegmentedColormap

file = 'brachisto.beluga'

data = load(file)
sols = data['solutions'][-1]

fig1 = plt.figure()
fig1.suptitle('Brachistochrone Continuation')

gs = GridSpec(2, 2, figure=fig1)

ax1 = fig1.add_subplot(gs[0, 0])
ax2 = fig1.add_subplot(gs[0, 1])
ax3 = fig1.add_subplot(gs[1, 0])
ax4 = fig1.add_subplot(gs[1, 1])

colors = LinearSegmentedColormap.from_list('simple', ["C0", "C1"], N=len(sols))(list(range(len(sols))))


def plot_sol(_sol, _color='C0'):
    t = _sol.t

    x = _sol.y[:, 0]
    y = _sol.y[:, 1]
    v = _sol.y[:, 2]

    # lam_x = _sol.dual[:, 0]
    # lam_y = _sol.dual[:, 1]
    lam_v = _sol.dual[:, 2]

    theta = _sol.u[:, 0]

    ax1.plot(x, y, color=_color)
    ax2.plot(t, v, color=_color)
    ax3.plot(t, theta, color=_color)
    ax4.plot(t, lam_v, color=_color)


for sol, color in zip(sols, colors):
    plot_sol(sol, _color=color)


ax1.set_title('Path')
ax1.set_xlabel(r'Horizontal Position $x$ [ft]')
ax1.set_ylabel(r'Vertical Position $y$ [ft]')

ax2.set_title('Velocity')
ax2.set_xlabel(r'Time $t$ [s]')
ax2.set_ylabel(r'Velocity $v$ [ft/s]')

ax3.set_title('Velocity')
ax3.set_xlabel(r'Time $t$ [s]')
ax3.set_ylabel(r'Velocity $v$ [ft/s]')

ax4.set_title('Velocity Costate')
ax4.set_xlabel(r'Time $t$ [s]')
ax4.set_ylabel(r'Velocity Costate $\lambda_v$ [s^2/ft]')

# fig1.subplots_adjust(0.12, 0.09, 0.95, 0.9, 0.51, 1)

plt.show()

