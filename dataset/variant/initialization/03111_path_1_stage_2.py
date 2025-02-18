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

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

single_color = '#1f77b4'
labels = ['Winter', 'Autumn', 'Spring', 'Summer']

for data, label in zip(wind_data, labels):
    ax.plot(angles, data, marker='s', linestyle='-.', color=single_color, linewidth=1.5, label=label)
    ax.fill(angles, data, color=single_color, alpha=0.2)

for data, label in zip(wind_data, labels):
    max_idx = np.argmax(data[:-1])
    ax.annotate(f'{label}\nMax: {data[max_idx]}',
                xy=(angles[max_idx], data[max_idx]),
                xytext=(angles[max_idx] + 0.2, data[max_idx] + 3),
                textcoords='data',
                arrowprops=dict(arrowstyle="-|>", color='darkblue'),
                ha='center', fontsize=9, color='darkred')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(directions, fontsize=13, fontweight='bold')
ax.grid(color='black', linestyle=':', linewidth=0.7, alpha=0.6)

ax.set_title("Mystic Isles Wind Patterns\nSeasonal Frequencies", fontsize=15, fontweight='bold', pad=25)

ax.legend(loc='lower left', bbox_to_anchor=(0.9, -0.1), fontsize=11, title='Seasons', title_fontsize='12')

plt.tight_layout()
plt.show()