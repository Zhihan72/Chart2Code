import matplotlib.pyplot as plt
import numpy as np

coffee_types = ['Latte', 'Amer.', 'Capp.', 'Mocha', 'Esp.']

sales_Q1 = [150, 200, 210, 220, 180]
sales_Q2 = [190, 230, 210, 160, 220]
sales_Q3 = [240, 220, 170, 200, 230]
sales_Q4 = [210, 180, 230, 240, 250]

data = [sales_Q1, sales_Q2, sales_Q3, sales_Q4]

x = np.arange(len(coffee_types))

fig, ax = plt.subplots(figsize=(12, 7))
width = 0.2

# New set of colors
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2']
for i, (sales, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, sales, width, color=color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(coffee_types, fontsize=11)

plt.tight_layout()
plt.show()