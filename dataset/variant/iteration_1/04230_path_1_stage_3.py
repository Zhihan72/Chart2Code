import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']

sales_data = {
    'Elderberries': [-4, -5, -4.5, -3, -5.5],
    'Bananas': [7.5, 10, 6.5, 9, 11],
    'Apples': [12.5, 15, 11, 14, 17.5],
    'Dates': [-2.5, -1.5, -2, -3.5, -3],
    'Cherries': [-5, -6, -4, -7, -4.5]
}

years_count = len(years)
bar_width = 0.5
year_positions = np.arange(years_count)

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffle the order of fruits and styles
bottoms = np.zeros(years_count)
styles = ['x', 'D', 's', 'o', '*']  # Different marker types for variety
colors = ['blue', 'orange', 'green', 'purple', 'red']  # Different colors for variety
line_styles = ['-', '--', '-.', ':', '-']  # Different line styles for variety

# Adjust the order of iteration
for i, (fruit, sales) in enumerate(reversed(sales_data.items())):
    ax.bar(year_positions, sales, bar_width, bottom=bottoms, 
           label=fruit, color=colors[i], linestyle=line_styles[i], hatch=styles[i])

# Alter the annotations - move annotations slightly differently for variety
for fruit, sales in sales_data.items():
    for i, sale in enumerate(sales):
        ax.text(year_positions[i], sale + (4 if sale < 0 else -4), 
                f'{abs(sale)}', ha='center', va='center', fontsize=8, color='white')

# Change the legend and grid style
ax.set_title("Diverging Bar Chart of Fruit Sales\nFarmer's Market Overview 2018-2022", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Diverging Sales (in tons)", fontsize=12)
ax.set_xticks(year_positions)
ax.set_xticklabels(years)
ax.axhline(0, color='black', linewidth=0.8)
ax.legend(loc='best', title="Fruits", fontsize=10, title_fontsize='13')

# Remove the grid to make changes to stylistic elements
ax.grid(False)

plt.tight_layout()
plt.show()