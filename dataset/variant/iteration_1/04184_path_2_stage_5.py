import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.arange(1, 13)
coffee_sales = np.array([10, 12, 15, 18, 20, 22, 25, 27, 30, 33, 35, 40])
tea_sales = np.array([8, 9, 11, 13, 15, 16, 17, 19, 21, 23, 24, 26])
juice_sales = np.array([5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22])
smoothie_sales = np.array([3, 4, 5, 6, 8, 9, 10, 12, 13, 15, 17, 19])

sales_data = [coffee_sales, tea_sales, juice_sales, smoothie_sales]
labels = ['Coffee', 'Tea', 'Juice', 'Smoothie']
colors = ['#8B4513', '#006400', '#FFD700', '#FF69B4']

fig, axs = plt.subplots(3, 4, figsize=(12, 9))
fig.suptitle('2022 Monthly Sales by Categories', fontsize=16, fontweight='bold')

for i in range(3):
    for j in range(4):
        month_index = i * 4 + j
        monthly_sales = [coffee_sales[month_index], tea_sales[month_index], juice_sales[month_index], smoothie_sales[month_index]]
        
        wedges, texts = axs[i, j].pie(monthly_sales, labels=labels, colors=colors, startangle=90)
        
        # Create donut shape by adding a white circle in the middle
        circle = plt.Circle((0, 0), 0.70, fc='white')
        axs[i, j].add_artist(circle)
        
        axs[i, j].set_title(f'Month: {["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][month_index]}')

for ax in axs.flat:
    ax.label_outer()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()