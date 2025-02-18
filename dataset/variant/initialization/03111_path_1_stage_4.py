import matplotlib.pyplot as plt
import numpy as np

# The content within the data groups is altered
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
spring_winds = np.array([10, 6, 4, 12, 8, 3, 5, 15])
summer_winds = np.array([8, 18, 6, 5, 2, 10, 4, 15])
autumn_winds = np.array([5, 3, 17, 9, 14, 10, 8, 10])
winter_winds = np.array([4, 18, 3, 7, 2, 12, 10, 5])

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
ax.set_xticklabels([])  # Direction labels are still removed
ax.grid(color='black', linestyle=':', linewidth=0.7, alpha=0.6)

plt.tight_layout()
plt.show()