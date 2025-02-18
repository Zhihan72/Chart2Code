import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Figs', 'Grapes', 'Honeydew']

sales_apples = np.array([4, 5, 6, 7, 5, 6, 8, 7, 6, 5, 4, 5])
sales_bananas = np.array([6, 7, 8, 9, 8, 7, 8, 9, 6, 7, 6, 5])
sales_cherries = np.array([2, 3, 4, 5, 4, 3, 5, 6, 5, 4, 3, 3])
sales_dates = np.array([1, 2, 2, 3, 2, 1, 2, 2, 3, 4, 5, 4])
sales_elderberries = np.array([0.5, 1, 1.5, 2, 2, 1.5, 2, 2.5, 2, 1.5, 1, 1.5])
sales_figs = np.array([1, 1.5, 2, 2.5, 2, 2.5, 3, 2.5, 2, 2.5, 3, 3.5])
sales_grapes = np.array([3, 3.5, 4, 4.5, 4, 3.5, 3, 4, 4.5, 4.5, 5, 5.5])
sales_honeydew = np.array([2, 2.5, 2, 1.5, 2, 2.5, 3, 3.5, 3, 2.5, 3, 2])

data = np.array([sales_apples, sales_bananas, sales_cherries, sales_dates, sales_elderberries, sales_figs, sales_grapes, sales_honeydew])

n_months = len(months)
x = np.arange(n_months)
bar_width = 0.7

fig, ax = plt.subplots(figsize=(14, 8))

bottom = np.zeros(n_months)
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
for i, (sales, color) in enumerate(zip(data, new_colors)):
    bars = ax.bar(x, sales, width=bar_width, color=color, bottom=bottom)
    bottom += sales
    
    if i == 6:  # Labeling Grapes
        for bar in bars:
            yval = bar.get_height() + bar.get_y()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval:.1f}', ha='center', va='bottom', fontsize=9, color='black')

ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales (in thousands of units)', fontsize=12)
ax.set_title('Monthly Fruit Sales Performance in Grocery Store\n(Jan - Dec)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(months)
plt.xticks(rotation=30, ha='right')

total_sales = data.sum(axis=0)
for idx, total in enumerate(total_sales):
    ax.annotate(f'Total: {total:.1f}', xy=(idx, total + 1), fontsize=10, ha='center', color='black')

# Removing axes spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()