import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']

# Normalize data for illustration, where the first half of fruits go upwards and the second half downwards
sales_data = {
    'Apples': [12.5, 15, 11, 14, 17.5],
    'Bananas': [7.5, 10, 6.5, 9, 11],
    'Cherries': [-5, -6, -4, -7, -4.5],
    'Dates': [-2.5, -1.5, -2, -3.5, -3],
    'Elderberries': [-4, -5, -4.5, -3, -5.5]
}

years_count = len(years)
fruit_count = len(fruits)
bar_width = 0.5  # Wider bars for clearer view
year_positions = np.arange(years_count)

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting diverging bar chart
bottoms = np.zeros(years_count)
for fruit, sales in sales_data.items():
    ax.bar(year_positions, sales, bar_width, bottom=bottoms, label=fruit)

# Adding text annotations for bars
for fruit, sales in sales_data.items():
    for i, sale in enumerate(sales):
        ax.text(year_positions[i], sale + (3 if sale < 0 else -3), f'{abs(sale)}',
                ha='center', va='center', fontsize=8, color='white')

# Customizing the plot
ax.set_title("Diverging Bar Chart of Fruit Sales\nFarmer's Market Overview 2018-2022", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Diverging Sales (in tons)", fontsize=12)
ax.set_xticks(year_positions)
ax.set_xticklabels(years)
ax.axhline(0, color='black', linewidth=0.8)  # Central axis
ax.legend(loc='upper left', title="Fruits")

ax.grid(True, axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()