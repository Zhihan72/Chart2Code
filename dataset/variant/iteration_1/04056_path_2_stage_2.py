import numpy as np
import matplotlib.pyplot as plt

# Data: Monthly Sales (2022)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
flavors = ['Van', 'Choc', 'Straw', 'Mint', 'Cookies']

# Define sales data in thousand units
vanilla_sales = np.array([12, 15, 13, 14, 18, 22, 30, 28, 25, 20, 18, 16])
chocolate_sales = np.array([10, 12, 11, 13, 15, 17, 25, 23, 19, 17, 16, 15])
strawberry_sales = np.array([8, 10, 9, 10, 11, 12, 20, 18, 15, 13, 12, 11])
mint_sales = np.array([6, 7, 6, 7, 8, 10, 15, 13, 11, 10, 9, 8])
cookies_cream_sales = np.array([5, 6, 5, 6, 8, 9, 14, 13, 12, 10, 9, 8])

sales_data = [vanilla_sales, chocolate_sales, strawberry_sales, mint_sales, cookies_cream_sales]
colors = ['#FFDDC1', '#D4E157', '#FF80AB', '#80DEEA', '#FFC107']

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting grouped bar chart
n_flavors = len(flavors)
bar_width = 0.15
x_indices = np.arange(len(months))

for i, (sales, color) in enumerate(zip(sales_data, colors)):
    ax.bar(x_indices + i * bar_width, sales, width=bar_width, label=flavors[i], color=color, edgecolor='black')

ax.set_title("Ice Cream Sales (2022)", fontsize=18, fontweight='bold')
ax.set_xlabel("Mon", fontsize=14)
ax.set_ylabel("Units (k)", fontsize=14)
ax.set_xticks(x_indices + bar_width * (n_flavors - 1) / 2)
ax.set_xticklabels(months)
ax.legend(title='Flav', title_fontsize=12, fontsize=10, loc='upper left')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.text(7, 75, 'Summer Surge', fontsize=12, style='italic', color='darkblue',
        bbox=dict(facecolor='lightyellow', edgecolor='darkblue', boxstyle='round,pad=0.2'))
ax.text(1, 50, 'Winter Dip', fontsize=12, style='italic', color='darkblue',
        bbox=dict(facecolor='lightyellow', edgecolor='darkblue', boxstyle='round,pad=0.2'))

def annotate_bars(ax):
    for bar in ax.patches:
        ax.annotate(f'{bar.get_height():.0f}', 
                    (bar.get_x() + bar.get_width() / 2, bar.get_height() - 1), 
                    ha='center', va='center', fontsize=10, color='black', 
                    fontweight='bold', rotation=0)

annotate_bars(ax)

plt.tight_layout()
plt.show()