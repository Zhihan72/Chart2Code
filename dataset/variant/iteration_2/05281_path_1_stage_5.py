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

# Sort data in descending order and keep track of indices
store_a_sorted_indices = np.argsort(store_a_sales)[::-1]
store_b_sorted_indices = np.argsort(store_b_sales)[::-1]
store_c_sorted_indices = np.argsort(store_c_sales)[::-1]
store_d_sorted_indices = np.argsort(store_d_sales)[::-1]

# Sort months according to sorted sales indices
sorted_months_a = [months[i] for i in store_a_sorted_indices]
sorted_months_b = [months[i] for i in store_b_sorted_indices]
sorted_months_c = [months[i] for i in store_c_sorted_indices]
sorted_months_d = [months[i] for i in store_d_sorted_indices]

# Sort sales data
store_a_sales_sorted = sorted(store_a_sales, reverse=True)
store_b_sales_sorted = sorted(store_b_sales, reverse=True)
store_c_sales_sorted = sorted(store_c_sales, reverse=True)
store_d_sales_sorted = sorted(store_d_sales, reverse=True)

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.20

r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

ax.bar(r1, store_a_sales_sorted, color='#FF5733', width=bar_width, label='Store A')
ax.bar(r2, store_b_sales_sorted, color='#33FF57', width=bar_width, label='Store B')
ax.bar(r3, store_c_sales_sorted, color='#3357FF', width=bar_width, label='Store C')
ax.bar(r4, store_d_sales_sorted, color='#FF33A6', width=bar_width, label='Store D')

ax.set_xticks([r + 1.5*bar_width for r in range(len(months))])
ax.set_xticklabels(sorted_months_a)  # Set x-ticks to sorted months labels of Store A

plt.tight_layout()
plt.legend()
plt.show()