import numpy as np
import matplotlib.pyplot as plt

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

store_a_sales = [250, 300, 400, 350, 500, 450, 600, 700, 650, 750, 800, 850]
store_b_sales = [200, 250, 300, 320, 410, 390, 480, 520, 610, 680, 730, 760]

fig, ax = plt.subplots(figsize=(14, 8))
bar_height = 0.25

r1 = np.arange(len(months))
r2 = [x + bar_height for x in r1]

bars1 = ax.barh(r1, store_a_sales, color='#5DA5DA', height=bar_height)  # Adjusted for horizontal bar
bars2 = ax.barh(r2, store_b_sales, color='#FAA43A', height=bar_height)  # Adjusted for horizontal bar

for bars in [bars1, bars2]:
    for bar in bars:
        xval = bar.get_width()
        ax.text(xval + 20, bar.get_y() + bar.get_height()/2, f'{xval}', va='center', ha='left', fontsize=10, fontweight='bold', color='black')

ax.set_yticks([r + bar_height / 2 for r in range(len(months))])
ax.set_yticklabels(months)

plt.tight_layout()
plt.show()