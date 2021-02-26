import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.gridspec import GridSpec
from beluga.utils import load
from matplotlib.colors import LinearSegmentedColormap

re = 6.3781e6

rad2deg = 180/3.141592653589793

file = 'hyper_example.beluga'

data = load(file)
sols = data['solutions'][-1][::2]

fig1 = plt.figure()
fig1.suptitle('Continuation of Hypersonic Vechicle')

gs = GridSpec(2, 2, figure=fig1)

ax1 = fig1.add_subplot(gs[0, 0])
ax2 = fig1.add_subplot(gs[0, 1])
ax3 = fig1.add_subplot(gs[1, 0])
ax4 = fig1.add_subplot(gs[1, 1])

colors = LinearSegmentedColormap.from_list('simple', ["C0", "C9"],
                                           N=len(sols))(list(range(len(sols))))


def plot_sol(_sol, _color='C0', linewidth=1):
    t = _sol.t

    h = _sol.y[:, 0]
    theta = _sol.y[:, 1]
    v = _sol.y[:, 2]
    gam = _sol.y[:, 3]

    alpha = _sol.u[:, 0]

    ax1.plot(theta * re / 1000, h / 1000, color=_color, linewidth=linewidth)
    ax2.plot(v / 1000, h / 1000, color=_color, linewidth=linewidth)
    ax3.plot(t, gam * rad2deg, color=_color, linewidth=linewidth)
    ax4.plot(t, alpha * rad2deg, color=_color, linewidth=linewidth)


root_colors = ['C9', 'C1', 'C2', 'C0', 'C3', 'C8', 'C9', 'C4']

plot_sol(data['solutions'][0][0], _color=root_colors[0], linewidth=2)

for k, sols in enumerate(data['solutions']):

    colors = LinearSegmentedColormap.from_list('simple', [root_colors[k], root_colors[k + 1]],
                                               N=len(sols))(list(range(len(sols))))

    for sol, color in zip(sols, colors):
        plot_sol(sol, _color=color)

    plot_sol(sols[-1], _color=root_colors[k + 1], linewidth=3)

ax1.set_title('Trajectory')
ax1.set_xlabel(r'Downrange $\theta*r_e$ [km]')
ax1.set_ylabel(r'Altitude $h$ [km]')

ax2.set_title('h-v Diagram')
ax2.set_xlabel(r'Velocity $v$ [km/s]')
ax2.set_ylabel(r'Altitude $h$ [km]')

ax3.set_title('Flight Path Angle')
ax3.set_xlabel(r'Time $t$ [s]')
ax3.set_ylabel(r'FPA $\gamma$ [deg]')

ax4.set_title('Angle of Attack')
ax4.set_xlabel(r'Time $t$ [s]')
ax4.set_ylabel(r'AoA $\alpha$ [deg]')

plt.show()
