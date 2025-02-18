import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2021', '2020', '2022']
fruits = ['Cherries', 'Bananas', 'Apples', 'Elderberries']

sales_data = {
    'Cherries': [10, 12, 8, 14, 9],
    'Bananas': [15, 20, 13, 18, 22],
    'Apples': [25, 30, 22, 28, 35],
    'Elderberries': [8, 10, 9, 6, 11]
}

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

years_count = len(years)
bar_width = 0.4
year_positions = np.arange(years_count)

fig, ax1 = plt.subplots(figsize=(14, 8))

# Calculate the offsets from the center
offsets = {-1: 0, 1: 0}
for idx, (fruit, sales) in enumerate(sales_data.items()):
    current_sales = np.array(sales)
    positive_mask = current_sales >= 0

    ax1.bar(year_positions, current_sales * positive_mask, bar_width,
            bottom=offsets[1] * positive_mask, color=colors[idx], label=fruit)

    ax1.bar(year_positions, current_sales * ~positive_mask, bar_width,
            bottom=offsets[-1] * ~positive_mask, color=colors[idx], label=f'{fruit} Neg')

    offsets[1] += current_sales * positive_mask
    offsets[-1] += current_sales * ~positive_mask

ax1.set_xticks(year_positions)
ax1.set_xticklabels(years)
ax1.axhline(0, color='black', linewidth=0.8)  # central axis line
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()