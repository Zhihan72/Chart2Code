import matplotlib.pyplot as plt
import numpy as np

directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
spring_winds = np.array([8, 12, 15, 10, 6, 4, 3, 5])
summer_winds = np.array([5, 6, 8, 15, 18, 10, 4, 2])
autumn_winds = np.array([3, 5, 10, 8, 9, 14, 17, 10])
winter_winds = np.array([10, 7, 4, 3, 2, 5, 12, 18])

wind_data = [spring_winds, summer_winds, autumn_winds, winter_winds]

angles = np.linspace(0, 2 * np.pi, len(directions), endpoint=False).tolist()
angles += angles[:1]

for i in range(len(wind_data)):
    wind_data[i] = np.append(wind_data[i], wind_data[i][0])

fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))

colors = ['#FFDDC1', '#FF677D', '#FFC3A0', '#FFABAB']
labels = ['Sum', 'Win', 'Aut', 'Spr']

marker_styles = ['s', 'p', 'd', '^']  # square, pentagon, diamond, triangle_up
line_styles = [':', '-.', '--', '-']

for data, color, label, marker, linestyle in zip(wind_data, colors, labels, marker_styles, line_styles):
    ax.plot(angles, data, marker=marker, linestyle=linestyle, color=color, linewidth=2, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(directions, fontsize=10, fontweight='light')
ax.set_yticklabels([0, 5, 10, 15, 20], fontsize=8)
ax.grid(color='black', linestyle='--', linewidth=0.3, alpha=0.8)

ax.set_title("Wind Patterns in Mystic Isles", fontsize=18, fontstyle='italic', color='darkblue', pad=40)

ax.legend(loc='lower left', bbox_to_anchor=(-0.1, 0.2), fontsize=9, title='Wind Season', title_fontsize='11')

plt.tight_layout()
plt.show()