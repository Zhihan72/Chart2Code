import matplotlib.pyplot as plt
import numpy as np

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
variances = np.array([80.58, 10.25, 88.92, 54.67])  # Manually provided variances

fig, (ax2, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), gridspec_kw={'width_ratios': [1, 3]})

single_color = 'royalblue'

# Change horizontal bar plot in ax2 to a vertical bar plot
ax2.bar(cities, variances, color=single_color, edgecolor='black', hatch='/')
ax2.set_title('Temp Variability by City', fontsize=14, fontweight='bold', style='italic')
ax2.set_ylabel('Temp Variability (°C²)', fontsize=12, style='italic')
ax2.set_xlabel('Cities', fontsize=12, fontweight='bold')

for i, variance in enumerate(variances):
    ax2.text(i, variance + 0.1, f'{variance:.2f}', ha='center', va='bottom', fontsize=12, style='italic')

ax2.grid(True, linestyle=':', alpha=0.5, axis='y')

# Retaining the second subplot (ax1) as it is already a base bar chart
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temp_data = np.array([
    [3, 5, 10, 15, 21, 26, 30, 29, 24, 18, 11, 6],
    [15, 16, 17, 18, 20, 22, 24, 24, 23, 20, 17, 15],
    [-1, 1, 5, 11, 17, 23, 27, 26, 21, 14, 7, 2],
    [12, 14, 19, 23, 27, 30, 32, 32, 29, 24, 18, 13]
])
bar_width = 0.2
x_positions = np.arange(len(months))

for i, city in enumerate(cities):
    ax1.bar(x_positions + i * bar_width, temp_data[i], width=bar_width, label=city, color=single_color, edgecolor='black', capstyle='round')

ax1.set_title('Monthly Temperatures (°C)', fontsize=16, fontweight='bold', color='purple')
ax1.set_xlabel('Month', fontsize=14, fontstyle='italic')
ax1.set_ylabel('Temperature (°C)', fontsize=14, color='brown')
ax1.set_xticks(x_positions + bar_width * 1.5)
ax1.set_xticklabels(months, fontsize=12)

for i in range(len(months)):
    for j in range(len(cities)):
        ax1.text(i + j * bar_width, temp_data[j][i] + 0.5, str(temp_data[j][i]), ha='center', va='bottom', fontsize=10)

ax1.legend(title='Cities', fontsize=12)
ax1.grid(True, linestyle=':', alpha=0.5, axis='y')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()