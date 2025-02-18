import matplotlib.pyplot as plt
import numpy as np

crop_types = ['Wheat', 'Corn', 'Barley', 'Soy', 'Oats', 'Rice', 'Quinoa']
quantities_2020 = [500, 750, 400, 600, 200, 450, 100]
quantities_2021 = [550, 800, 450, 650, 220, 480, 120]
quantities_2022 = [600, 850, 500, 700, 250, 520, 140]
quantities_2023 = [650, 900, 550, 750, 300, 560, 160]
quantities_2024 = [700, 950, 600, 800, 350, 600, 180]

fig, ax = plt.subplots(figsize=(14, 8))
height = 0.12

bar_positions_2020 = np.arange(len(crop_types))
bar_positions_2021 = bar_positions_2020 + height
bar_positions_2022 = bar_positions_2021 + height
bar_positions_2023 = bar_positions_2022 + height
bar_positions_2024 = bar_positions_2023 + height

bars_2020 = ax.barh(bar_positions_2020, quantities_2020, height=height, label='2020', color='#ff9999', edgecolor='black')
bars_2021 = ax.barh(bar_positions_2021, quantities_2021, height=height, label='2021', color='#66b3ff', edgecolor='black')
bars_2022 = ax.barh(bar_positions_2022, quantities_2022, height=height, label='2022', color='#99ff99', edgecolor='black')
bars_2023 = ax.barh(bar_positions_2023, quantities_2023, height=height, label='2023', color='#ffcc99', edgecolor='black')
bars_2024 = ax.barh(bar_positions_2024, quantities_2024, height=height, label='2024', color='#c2c2f0', edgecolor='black')

def add_value_labels(bars):
    for bar in bars:
        xval = bar.get_width()
        ax.text(xval + 15, bar.get_y() + bar.get_height() / 2, f'{xval}', ha='left', va='center')

add_value_labels(bars_2020)
add_value_labels(bars_2021)
add_value_labels(bars_2022)
add_value_labels(bars_2023)
add_value_labels(bars_2024)

ax.set_title('Crop Yields (5 Years)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Crops', fontsize=14)
ax.set_xlabel('Qty (tons)', fontsize=14)
ax.set_yticks(bar_positions_2020 + 2 * height)
ax.set_yticklabels(crop_types)

ax.grid(True, linestyle='--', alpha=0.6, axis='x')

ax.legend(title='Year', title_fontsize='13', fontsize='11', loc='lower right', frameon=True)

plt.tight_layout()
plt.show()