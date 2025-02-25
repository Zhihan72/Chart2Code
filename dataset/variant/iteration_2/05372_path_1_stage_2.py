import matplotlib.pyplot as plt
import numpy as np

coffee_types = ['Esp.', 'Latte', 'Capp.', 'Amer.', 'Mocha']

# Manually shuffled sales data while maintaining the dimensional structure
sales_Q1 = [180, 150, 210, 200, 220]
sales_Q2 = [220, 190, 210, 230, 160]
sales_Q3 = [230, 240, 170, 220, 200]
sales_Q4 = [250, 210, 230, 180, 240]

data = [sales_Q1, sales_Q2, sales_Q3, sales_Q4]

x = np.arange(len(coffee_types))

fig, ax = plt.subplots(figsize=(12, 7))
width = 0.2

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for i, (sales, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, sales, width, label=f'Q{i+1}', color=color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

ax.set_title('Coffee Sales Qtrs 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Types', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(coffee_types, fontsize=11)
ax.legend(title='Qtrs', fontsize=10, loc='upper left')

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()