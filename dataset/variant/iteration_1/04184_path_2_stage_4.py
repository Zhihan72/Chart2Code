import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.arange(1, 13)
coffee_sales = np.array([10, 12, 15, 18, 20, 22, 25, 27, 30, 33, 35, 40])
tea_sales = np.array([8, 9, 11, 13, 15, 16, 17, 19, 21, 23, 24, 26])
juice_sales = np.array([5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22])
smoothie_sales = np.array([3, 4, 5, 6, 8, 9, 10, 12, 13, 15, 17, 19])

fig, ax1 = plt.subplots(figsize=(10, 8))

# Bar chart: Monthly sales
width = 0.2
ax1.bar(months - width * 1.5, coffee_sales, width=width, color='#8B4513', label='Coffee')
ax1.bar(months - width / 2, tea_sales, width=width, color='#006400', label='Tea')
ax1.bar(months + width / 2, juice_sales, width=width, color='#FFD700', label='Juice')
ax1.bar(months + width * 1.5, smoothie_sales, width=width, color='#FF69B4', label='Smoothie')  # New data series

ax1.set_title('2022 Monthly Sales', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Sales (k units)', fontsize=14)
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Add data labels
for i in range(len(months)):
    ax1.text(months[i] - width * 1.5, coffee_sales[i], str(coffee_sales[i]), ha='center', va='bottom', fontsize=10)
    ax1.text(months[i] - width / 2, tea_sales[i], str(tea_sales[i]), ha='center', va='bottom', fontsize=10)
    ax1.text(months[i] + width / 2, juice_sales[i], str(juice_sales[i]), ha='center', va='bottom', fontsize=10)
    ax1.text(months[i] + width * 1.5, smoothie_sales[i], str(smoothie_sales[i]), ha='center', va='bottom', fontsize=10)

ax1.legend()  # Add legend for clarity

plt.tight_layout()
plt.show()