import matplotlib.pyplot as plt
import numpy as np

crop_types = ['Oats', 'Barley', 'Corn', 'Rice', 'Soybeans', 'Wheat']
quantities_2020 = [200, 400, 750, 300, 600, 500]
quantities_2021 = [220, 450, 800, 320, 650, 550]
quantities_2022 = [250, 500, 850, 340, 700, 600]
quantities_2023 = [300, 550, 900, 360, 750, 650]
quantities_2024 = [350, 600, 950, 380, 800, 700]

sorted_indices = np.argsort(quantities_2024)[::-1]
sorted_crop_types = [crop_types[i] for i in sorted_indices]
sorted_quantities_2020 = [quantities_2020[i] for i in sorted_indices]
sorted_quantities_2021 = [quantities_2021[i] for i in sorted_indices]
sorted_quantities_2022 = [quantities_2022[i] for i in sorted_indices]
sorted_quantities_2023 = [quantities_2023[i] for i in sorted_indices]
sorted_quantities_2024 = [quantities_2024[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.15

bar_positions = np.arange(len(sorted_crop_types))

color = '#66b3ff'

bars_2020 = ax.bar(bar_positions - 2*width, sorted_quantities_2020, width=width, label='20-20', color=color, edgecolor='black')
bars_2021 = ax.bar(bar_positions - width, sorted_quantities_2021, width=width, label='21', color=color, edgecolor='black')
bars_2022 = ax.bar(bar_positions, sorted_quantities_2022, width=width, label='Year: 22', color=color, edgecolor='black')
bars_2023 = ax.bar(bar_positions + width, sorted_quantities_2023, width=width, label='2023/2024*', color=color, edgecolor='black')
bars_2024 = ax.bar(bar_positions + 2*width, sorted_quantities_2024, width=width, label='Two Thousand & Twenty-four', color=color, edgecolor='black')

def add_value_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 15, f'{yval}', ha='center', va='bottom')

add_value_labels(bars_2020)
add_value_labels(bars_2021)
add_value_labels(bars_2022)
add_value_labels(bars_2023)
add_value_labels(bars_2024)

ax.set_title('HarvYstdQuantities:Last5yrs.', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Plant Variety', fontsize=14)
ax.set_ylabel('Amt Hrvstd. (Metric Tonnes)', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_crop_types)

ax.grid(True, linestyle='--', alpha=0.6, axis='y')
ax.legend(title='CalendarYr.', title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

plt.tight_layout()
plt.show()