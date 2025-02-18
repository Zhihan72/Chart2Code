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

for data in wind_data:
    ax.plot(angles, data, marker='s', linestyle='-.', color=single_color, linewidth=1.5)
    ax.fill(angles, data, color=single_color, alpha=0.2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Remove direction labels
ax.grid(color='black', linestyle=':', linewidth=0.7, alpha=0.6)

plt.tight_layout()
plt.show()