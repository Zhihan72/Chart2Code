import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart illustrates the yearly sales of different types of chocolate bars in a candy company.
# The data spans from 2015 to 2020, showing an interesting trend in the chocolate market over six years.

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
milk_chocolate_sales = np.array([150, 180, 170, 190, 200, 220])
dark_chocolate_sales = np.array([100, 120, 130, 150, 160, 180])
white_chocolate_sales = np.array([70, 80, 75, 90, 95, 100])
sales_errors = np.array([10, 12, 11, 13, 14, 15])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
bar_positions1 = years - bar_width
bar_positions2 = years
bar_positions3 = years + bar_width

# Bar plot
bars1 = ax.bar(bar_positions1, milk_chocolate_sales, bar_width, yerr=sales_errors, capsize=5, label='Milk Chocolate', color='peru', alpha=0.8)
bars2 = ax.bar(bar_positions2, dark_chocolate_sales, bar_width, yerr=sales_errors, capsize=5, label='Dark Chocolate', color='brown', alpha=0.8)
bars3 = ax.bar(bar_positions3, white_chocolate_sales, bar_width, yerr=sales_errors, capsize=5, label='White Chocolate', color='wheat', alpha=0.8)

# Titles and labels
ax.set_title('Yearly Sales of Different Types of Chocolate Bars (2015-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales Volume (thousands of bars)', fontsize=12)

# Legend
ax.legend(title='Chocolate Type', fontsize=10, loc='upper left', frameon=True)

# Adjust ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=0, fontsize=12)

# Annotating bars with sales values
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom')
        
annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

# Grid and background customization
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()