import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']

temp_data = np.array([
    [3, 5, 10, 15, 21, 26, 30, 29, 24, 18, 11, 6],
    [15, 16, 17, 18, 20, 22, 24, 24, 23, 20, 17, 15],
    [-1, 1, 5, 11, 17, 23, 27, 26, 21, 14, 7, 2],
    [12, 14, 19, 23, 27, 30, 32, 32, 29, 24, 18, 13]
])

fig, (ax2, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), gridspec_kw={'width_ratios': [1, 3]})

bar_width = 0.2
x_positions = np.arange(len(months))

colors = ['skyblue', 'lightgreen', 'coral', 'gold']

variances = np.var(temp_data, axis=1)
ax2.barh(cities, variances, color=colors, edgecolor='black')
ax2.set_title('Temperature Variability Over the Year by City', fontsize=14, fontweight='bold')
ax2.set_xlabel('Temperature Variability (°C²)', fontsize=12)
ax2.set_ylabel('Cities', fontsize=12)

for i in range(len(cities)):
    ax2.text(variances[i] + 0.1, i, f'{variances[i]:.2f}', va='center', fontsize=12)

for i, city in enumerate(cities):
    ax1.bar(x_positions + i * bar_width, temp_data[i], width=bar_width, label=city, color=colors[i])

ax1.set_title('Average Monthly Temperatures in Four Major Cities (°C)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14)
ax1.set_xticks(x_positions + bar_width * 1.5)
ax1.set_xticklabels(months, fontsize=12)

for i in range(len(months)):
    for j in range(len(cities)):
        ax1.text(i + j * bar_width, temp_data[j][i] + 0.5, str(temp_data[j][i]), ha='center', va='bottom', fontsize=10)

ax1.legend(title='Cities', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.show()