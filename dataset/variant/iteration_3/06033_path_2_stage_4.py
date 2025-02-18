import matplotlib.pyplot as plt
import numpy as np

flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Cookie Dough']

chocolate_sales = [50, 55, 60, 48, 70, 85, 90, 95, 60, 55, 60, 50]
vanilla_sales = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
strawberry_sales = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
cookie_dough_sales = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

monthly_sales = np.array([chocolate_sales, vanilla_sales, strawberry_sales, cookie_dough_sales])
average_sales = np.mean(monthly_sales, axis=1)

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

bars = axs[0].bar(flavors, average_sales, color=['#F08080', '#87CEEB', '#32CD32', '#FFD700'])
axs[0].set_title('Average Monthly Sales of Ice Cream Flavors', fontsize=14)
axs[0].set_xlabel('Flavors', fontsize=11)
axs[0].set_ylabel('Sales (hundreds)', fontsize=11)
axs[0].grid(axis='y', linestyle=':', color='grey', alpha=0.4)
axs[0].set_ylim(0, 100)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)

for bar in bars:
    height = bar.get_height()
    axs[0].text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom')

months = np.arange(1, 13)
new_colors = ['#F08080', '#87CEEB', '#32CD32', '#FFD700']
markers = ['s', '^', 'd', '*']  
line_styles = ['-', '--', '-.', ':']
for i, sales in enumerate(monthly_sales):
    axs[1].plot(months, sales, marker=markers[i], linestyle=line_styles[i], color=new_colors[i], label=flavors[i])

axs[1].set_title('Monthly Sales Trends of Ice Cream Flavors', fontsize=14)
axs[1].set_xlabel('Month', fontsize=11)
axs[1].set_ylabel('Sales (hundreds)', fontsize=11)
axs[1].set_xticks(months)
axs[1].legend(title='', fontsize=9, loc='upper left', frameon=False)
axs[1].grid(True, linestyle=':', color='grey', alpha=0.3)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()