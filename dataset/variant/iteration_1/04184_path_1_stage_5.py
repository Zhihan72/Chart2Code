import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
coffee_sales = np.array([10, 12, 15, 18, 20, 22, 25, 27, 30, 33, 35, 40])
tea_sales = np.array([8, 9, 11, 13, 15, 16, 17, 19, 21, 23, 24, 26])
juice_sales = np.array([5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22])

cumulative_sales = np.array([sum(coffee_sales), sum(tea_sales), sum(juice_sales)])
beverages = ['Java', 'Chai', 'Nectar']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 16))

# First subplot: Bar chart with modified styles
width = 0.25
ax1.bar(months - width, coffee_sales, width=width, color='skyblue', edgecolor='black', linestyle='-.', label='Java')
ax1.bar(months, tea_sales, width=width, color='orange', edgecolor='black', linestyle='--', label='Chai')
ax1.bar(months + width, juice_sales, width=width, color='green', edgecolor='black', linestyle='-', label='Nectar')

ax1.set_title('Beverage Sales Per Month (2022)', fontsize=14, fontweight='normal', style='italic')
ax1.set_xlabel('Months', fontsize=12)
ax1.set_ylabel('Quantity Sold (K Units)', fontsize=12)
ax1.set_xticks(months)
ax1.set_xticklabels(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], rotation=45)
ax1.legend(loc='upper right', fontsize=10, title='Drink Types', title_fontsize='12')
ax1.grid(axis='y', linestyle=':', alpha=0.5)

for i in range(len(months)):
    ax1.text(months[i] - width, coffee_sales[i] + 0.5, str(coffee_sales[i]), ha='center', va='bottom', fontsize=8, style='italic')
    ax1.text(months[i], tea_sales[i] + 0.5, str(tea_sales[i]), ha='center', va='bottom', fontsize=8, style='italic')
    ax1.text(months[i] + width, juice_sales[i] + 0.5, str(juice_sales[i]), ha='center', va='bottom', fontsize=8, style='italic')

# Second subplot: Donut chart with modified styles
ax2.pie(cumulative_sales, labels=beverages, colors=['lightcoral', 'lightgreen', 'lightblue'], autopct='%1.1f%%', startangle=90,
        explode=(0, 0.1, 0), wedgeprops=dict(width=0.4))
ax2.set_title('Market Distribution for 2022', fontsize=14, fontweight='normal', style='italic')

plt.tight_layout()
plt.show()