import numpy as np
import matplotlib.pyplot as plt

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

store_a_sales = [250, 300, 400, 350, 500, 450, 600, 700, 650, 750, 800, 850]
store_b_sales = [200, 250, 300, 320, 410, 390, 480, 520, 610, 680, 730, 760]
store_c_sales = [180, 230, 260, 290, 310, 280, 350, 400, 450, 470, 500, 540]

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.25

r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

bars1 = ax.bar(r1, store_a_sales, color='#5DA5DA', width=bar_width)
bars2 = ax.bar(r2, store_b_sales, color='#FAA43A', width=bar_width)
bars3 = ax.bar(r3, store_c_sales, color='#60BD68', width=bar_width)

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 20, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_xticks([r + bar_width for r in range(len(months))])

plt.tight_layout()
plt.show()