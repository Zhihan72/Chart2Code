import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

cities = ['NY', 'LA', 'Chi', 'Hou']

# Randomly altered temperature data, preserving dimensional structure
temp_data = np.array([
    [30, 26, 21, 15, 11, 5, 3, 6, 10, 18, 24, 29],
    [24, 23, 20, 22, 15, 17, 16, 18, 24, 20, 17, 15],
    [17, 11, 7, 5, 23, 2, 26, 1, 14, 27, 21, -1],
    [32, 13, 12, 14, 18, 19, 27, 24, 32, 23, 29, 30]
])

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

bar_width = 0.2
x_positions = np.arange(len(months))
colors = ['coral', 'gold', 'skyblue', 'lightgreen']

for i, city in enumerate(cities):
    ax1.bar(x_positions + i * bar_width, temp_data[i], width=bar_width, color=colors[i])

ax1.set_xlabel('Mon', fontsize=14)
ax1.set_ylabel('Temp (°C)', fontsize=14)
ax1.set_xticks(x_positions + bar_width * 1.5)
ax1.set_xticklabels(months, fontsize=12)

for i in range(len(months)):
    for j in range(len(cities)):
        ax1.text(i + j * bar_width, temp_data[j][i] + 0.5, str(temp_data[j][i]), ha='center', va='bottom', fontsize=10)

variances = np.var(temp_data, axis=1)
ax2.barh(cities, variances, color=colors)

ax2.set_xlabel('Temp Var (°C²)', fontsize=12)

for i in range(len(cities)):
    ax2.text(variances[i] + 0.1, i, f'{variances[i]:.2f}', va='center', fontsize=12)

plt.tight_layout()
plt.show()