import matplotlib.pyplot as plt
import numpy as np

gadgets = {
    'Mobiles': [250, 300, 350, 380, 450, 500, 520, 530, 600, 650, 700],
    'Tabs': [120, 130, 135, 140, 160, 170, 175, 190, 200, 220, 230],
    'Laps': [80, 95, 100, 105, 110, 120, 125, 130, 140, 150, 160]
}

total_sales = {gadget: sum(sales) for gadget, sales in gadgets.items()}
sorted_gadgets = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)
gadget_names, sorted_sales = zip(*sorted_gadgets)

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.6
range_gadgets = np.arange(len(gadget_names))

# Changed bar colors
ax.bar(range_gadgets, sorted_sales, width=bar_width, color=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

ax.set_title('Gadget Sales (2015-2025)', fontsize=14, fontweight='bold')
ax.set_ylabel('Units Sold', fontsize=12)
ax.set_xlabel('Gadgets', fontsize=12)
ax.set_xticks(range_gadgets)
ax.set_xticklabels(gadget_names)

# Modified grid to dotted style
ax.grid(True, linestyle=':', alpha=0.7)

# Hide top and right spines for stylistic effect
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Added legend
ax.legend(['Sales'], loc='upper left')

plt.tight_layout()
plt.show()