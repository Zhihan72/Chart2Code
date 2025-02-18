import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

cities = ['NY', 'LA', 'Chi', 'Hou']

temp_data = np.array([
    [3, 5, 10, 15, 21, 26, 30, 29, 24, 18, 11, 6],
    [15, 16, 17, 18, 20, 22, 24, 24, 23, 20, 17, 15],
    [-1, 1, 5, 11, 17, 23, 27, 26, 21, 14, 7, 2],
    [12, 14, 19, 23, 27, 30, 32, 32, 29, 24, 18, 13]
])

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})

bar_width = 0.2
x_positions = np.arange(len(months))
colors = ['skyblue', 'lightgreen', 'coral', 'gold']

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