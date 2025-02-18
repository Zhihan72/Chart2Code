import numpy as np
import matplotlib.pyplot as plt

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

store_a_sales = [250, 300, 400, 350, 500, 450, 600, 700, 650, 750, 800, 850]
store_b_sales = [200, 250, 300, 320, 410, 390, 480, 520, 610, 680, 730, 760]
store_c_sales = [180, 230, 260, 290, 310, 280, 350, 400, 450, 470, 500, 540]
store_d_sales = [220, 280, 290, 330, 410, 380, 450, 490, 550, 590, 610, 680]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.20

r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

# Updated color scheme
ax.bar(r1, store_a_sales, color='#FF5733', width=bar_width, edgecolor='grey')  # New color
ax.bar(r2, store_b_sales, color='#33FF57', width=bar_width, edgecolor='grey')  # New color
ax.bar(r3, store_c_sales, color='#3357FF', width=bar_width, edgecolor='grey')  # New color
ax.bar(r4, store_d_sales, color='#FF33A6', width=bar_width, edgecolor='grey')  # New color

ax.set_xticks([r + 1.5*bar_width for r in range(len(months))])

ax.grid(True, axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.show()