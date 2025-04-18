import matplotlib.pyplot as plt
import numpy as np

crop_types = ['Wheat', 'Corn', 'Barley', 'Soybeans', 'Oats', 'Rice']
quantities_2020 = [500, 750, 400, 600, 200, 300]
quantities_2021 = [550, 800, 450, 650, 220, 320]
quantities_2022 = [600, 850, 500, 700, 250, 340]
quantities_2023 = [650, 900, 550, 750, 300, 360]
quantities_2024 = [700, 950, 600, 800, 350, 380]

# Sort based on quantities_2024 in descending order
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

# Use a consistent color for all bars
color = '#66b3ff'  # Using the blue color for illustration

bars_2020 = ax.bar(bar_positions - 2*width, sorted_quantities_2020, width=width, label='2020', color=color, edgecolor='black')
bars_2021 = ax.bar(bar_positions - width, sorted_quantities_2021, width=width, label='2021', color=color, edgecolor='black')
bars_2022 = ax.bar(bar_positions, sorted_quantities_2022, width=width, label='2022', color=color, edgecolor='black')
bars_2023 = ax.bar(bar_positions + width, sorted_quantities_2023, width=width, label='2023', color=color, edgecolor='black')
bars_2024 = ax.bar(bar_positions + 2*width, sorted_quantities_2024, width=width, label='2024', color=color, edgecolor='black')

def add_value_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 15, f'{yval}', ha='center', va='bottom')

add_value_labels(bars_2020)
add_value_labels(bars_2021)
add_value_labels(bars_2022)
add_value_labels(bars_2023)
add_value_labels(bars_2024)

ax.set_title('Organic Crop Yields Over Five Years', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Crop Types', fontsize=14)
ax.set_ylabel('Quantity Harvested (in metric tons)', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(sorted_crop_types)

ax.grid(True, linestyle='--', alpha=0.6, axis='y')
ax.legend(title='Year', title_fontsize='13', fontsize='11', loc='upper left', frameon=True)

plt.tight_layout()
plt.show()