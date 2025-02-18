import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
milk_chocolate_sales = np.array([150, 180, 170, 190, 200, 220])
dark_chocolate_sales = np.array([100, 120, 130, 150, 160, 180])
white_chocolate_sales = np.array([70, 80, 75, 90, 95, 100])
sales_errors = np.array([10, 12, 11, 13, 14, 15])

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
bar_positions1 = years - bar_width
bar_positions2 = years
bar_positions3 = years + bar_width

# Bar plot with altered styles
bars1 = ax.bar(bar_positions1, milk_chocolate_sales, bar_width, yerr=sales_errors, capsize=3, label='Milk Chocolate', color='chocolate', linestyle='dashdot', alpha=0.7)
bars2 = ax.bar(bar_positions2, dark_chocolate_sales, bar_width, yerr=sales_errors, capsize=3, label='Dark Chocolate', color='firebrick', linestyle='dotted', alpha=0.7)
bars3 = ax.bar(bar_positions3, white_chocolate_sales, bar_width, yerr=sales_errors, capsize=3, label='White Chocolate', color='tan', linestyle='solid', alpha=0.7)

ax.set_title('Yearly Sales of Chocolate Bars (2015-2020)', fontsize=16, fontweight='normal')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Sales Volume (000s of bars)', fontsize=12)

# Altered legend style
ax.legend(title='Type', fontsize=10, loc='upper right', frameon=False)

# Change tick appearance
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30, fontsize=10)

# Randomly styled grid
ax.grid(True, linestyle='-.', linewidth=0.75, alpha=0.4)

# Borders removed
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Annotating bars
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 5),
                    textcoords="offset points", ha='center', va='bottom')

annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

plt.tight_layout()
plt.show()