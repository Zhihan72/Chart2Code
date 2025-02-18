import matplotlib.pyplot as plt
import numpy as np

gadgets = ['Laptops', 'Smartwatches', 'Smartphones', 'Tablets', 'Gaming Consoles']
years = ['2023', '2020', '2021', '2018', '2022', '2019']

data = np.array([
    [35, 33, 30, 28, 25, 22],
    [25, 26, 27, 26, 25, 24],
    [10, 12, 15, 18, 20, 22],
    [20, 18, 17, 15, 14, 13],
    [10, 11, 11, 13, 16, 19],
])

sorted_data = np.sort(data, axis=1)

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(14, 7))

bar_width = 0.15
x_positions = np.arange(len(years))
colors = ['#4c72b0', '#c44e52', '#ccb974', '#55a868', '#8172b3']

for i, (gadget, color) in enumerate(zip(gadgets, colors)):
    ax2.bar(x_positions + i * bar_width, sorted_data[i], width=bar_width, color=color, edgecolor='black')

ax2.set_title('Consumer Tech Gadgets Market\nShare (2018-2023)', fontsize=14)
ax2.set_xlabel('Years')
ax2.set_ylabel('Share of Market (%)')
ax2.set_xticks(x_positions + bar_width * 2)
ax2.set_xticklabels(years)

for i in range(len(years)):
    for j in range(len(gadgets)):
        ax2.text(x_positions[i] + j * bar_width, sorted_data[j, i] + 0.5, f"{sorted_data[j, i]}%", ha='center', va='bottom', fontsize=9)

smart_devices = data[0] + data[2] + data[3]
gaming_growth_rate = np.diff(data[4], prepend=data[4][0]) / data[4][0] * 100

ax1.plot(years, smart_devices, marker='o', color='#1f77b4')
ax1.set_title('Cumulative Share & Console Growth\nRate (2018-2023)', fontsize=14)
ax1.set_xlabel('Years')
ax1.set_ylabel('Cumulative Share (%)', color='#1f77b4')
ax1.tick_params(axis='y', labelcolor='#1f77b4')

ax3 = ax1.twinx()
ax3.plot(years, gaming_growth_rate, marker='x', color='#ff7f0e', linestyle='--')
ax3.set_ylabel('Rate of Growth (%)', color='#ff7f0e')
ax3.tick_params(axis='y', labelcolor='#ff7f0e')

plt.show()