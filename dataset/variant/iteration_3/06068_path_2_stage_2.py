import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

prod_development = [15, 20, 10, 18, 28, 16, 22, 30, 17, 27, 35, 24]
prod_marketing = [16, 12, 22, 14, 21, 15, 25, 26, 19, 20, 30, 28]
prod_sales = [18, 22, 19, 25, 30, 20, 27, 33, 29, 26, 34, 29]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(months, prod_development, marker='o', linestyle='-', color='blue')
ax.plot(months, prod_marketing, marker='s', linestyle='--', color='green')
ax.plot(months, prod_sales, marker='^', linestyle=':', color='red')

ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()