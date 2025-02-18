import matplotlib.pyplot as plt
import numpy as np

coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']

sales_Q1 = [150, 200, 180, 220, 210]
sales_Q3 = [170, 220, 200, 240, 230]
sales_Q4 = [180, 230, 210, 250, 240]

data = [sales_Q1, sales_Q3, sales_Q4]

x = np.arange(len(coffee_types))
fig, ax = plt.subplots(figsize=(12, 7))
width = 0.2

single_color = '#3498db'  # Consistent color for all groups

for i, sales in enumerate(data):
    rects = ax.bar(x + i * width, sales, width, 
                   label=f'Q{i+1 if i < 1 else i+2}', color=single_color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, color='white')

ax.set_title('Coffee Sales by Type (2023)', fontsize=14, fontweight='medium', pad=15)
ax.set_xlabel('Coffee Types', fontsize=11)
ax.set_ylabel('Sales', fontsize=11)
ax.set_xticks(x + width)
ax.set_xticklabels(coffee_types, fontsize=10)

ax.legend(title='Quarter', fontsize=9, loc='lower right')

ax.yaxis.grid(True, linestyle=':', linewidth=1, alpha=0.3)

plt.tight_layout()
plt.show()