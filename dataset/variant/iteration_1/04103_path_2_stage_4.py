import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 101, 10)

distance_to_planets = {
    'Zeta': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Eris': [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500],
    'Titan': [0, 100, 200, 300, 400, 500, 650, 800, 950, 1100, 1250],
    'Hyperion': [0, 150, 300, 450, 600, 750, 950, 1150, 1350, 1550, 1750],
    'Kuiper': [0, 200, 400, 600, 800, 1000, 1250, 1500, 1750, 2000, 2250],
    'Iota': [0, 75, 150, 225, 300, 375, 450, 525, 600, 675, 750],
    'Kappa': [0, 125, 250, 375, 500, 625, 750, 875, 1000, 1125, 1250],
    'Lambda': [0, 180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, 1800]
}

colors = ['#66b3ff', '#ff9999', '#c2f0c2', '#99ff99', '#ffb3e6', '#ffcc99', '#c2c2f0', '#ff6666']

fig, ax = plt.subplots(figsize=(14, 8))

markers = ['o', '^', 's', 'D', 'x', '*', 'p', 'h']
linestyles = ['-', '--', ':', '-.', '-', '--', ':', '-.']
for (body, distances), color, marker, linestyle in zip(distance_to_planets.items(), colors, markers, linestyles):
    ax.plot(time, distances, label=body, marker=marker, linestyle=linestyle, linewidth=2, alpha=0.8, color=color)

ax.set_title('Voyager Z: Exploring Uncharted Realms', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Duration (Months)', fontsize=12)
ax.set_ylabel('Separation from Origin (Million km)', fontsize=12)

ax.grid(True, linestyle=':', alpha=0.3)

ax.legend(fontsize=10, loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=4)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.annotate('Eris Arrival', xy=(50, 500), xytext=(20, 700),
            arrowprops=dict(facecolor='grey', arrowstyle='->', alpha=0.6), fontsize=11)

ax.annotate('Titan Approach', xy=(60, 650), xytext=(70, 850),
            arrowprops=dict(facecolor='grey', arrowstyle='->', alpha=0.6), fontsize=11)

ax.annotate('Hyperion Observations', xy=(80, 1150), xytext=(40, 1400),
            arrowprops=dict(facecolor='grey', arrowstyle='->', alpha=0.6), fontsize=11)

fig.tight_layout()
plt.show()