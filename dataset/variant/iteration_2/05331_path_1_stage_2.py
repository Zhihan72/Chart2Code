import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023, 1)

# Stock prices (fictional data)
opening_price = np.array([20, 22, 26, 30, 25, 28, 35, 40, 45, 50])
closing_price = np.array([22, 26, 28, 25, 28, 35, 40, 45, 50, 55])
highest_price = np.array([24, 28, 32, 30, 30, 37, 43, 48, 55, 60])
lowest_price = np.array([18, 20, 23, 20, 24, 27, 32, 39, 42, 47])

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(years, opening_price, marker='o', color='blue', label='Open Price', linewidth=2)
ax.plot(years, closing_price, marker='o', color='green', label='Close Price', linewidth=2)
ax.plot(years, highest_price, marker='o', color='red', label='Peak Price', linewidth=2)
ax.plot(years, lowest_price, marker='o', color='orange', label='Bottom Price', linewidth=2)

ax.set_title('XYZ Ltd. Stock Performance (13-22)', fontsize=16, fontweight='bold')
ax.set_ylabel('USD Value', fontsize=14)
ax.set_xlabel('Year of Trading', fontsize=14)
ax.legend(title='Price Data', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)

plt.xticks(years, rotation=45)
plt.tight_layout(pad=4)
plt.show()