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

ax.barh(bar_positions_2020, quantities_2020, height=height, color='#66b3ff')  # Changed color
ax.barh(bar_positions_2021, quantities_2021, height=height, color='#99ff99')  # Changed color
ax.barh(bar_positions_2022, quantities_2022, height=height, color='#ffcc99')  # Changed color
ax.barh(bar_positions_2023, quantities_2023, height=height, color='#c2c2f0')  # Changed color
ax.barh(bar_positions_2024, quantities_2024, height=height, color='#ff9999')  # Changed color

def add_value_labels(bars, positions):
    for i, xval in enumerate(bars):
        ax.text(xval + 15, positions[i] + height / 2, f'{xval}', ha='left', va='center')

add_value_labels(quantities_2020, bar_positions_2020)
add_value_labels(quantities_2021, bar_positions_2021)
add_value_labels(quantities_2022, bar_positions_2022)
add_value_labels(quantities_2023, bar_positions_2023)
add_value_labels(quantities_2024, bar_positions_2024)

ax.set_title('Crop Yields (5 Years)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Crops', fontsize=14)
ax.set_xlabel('Qty (tons)', fontsize=14)
ax.set_yticks(bar_positions_2020 + 2 * height)
ax.set_yticklabels(crop_types)

plt.tight_layout()
plt.show()