import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023, 1)

# Stock prices (fictional data)
opening_price = np.array([20, 25, 22, 30, 35, 28, 26, 45, 40, 50])
closing_price = np.array([26, 22, 35, 28, 50, 28, 40, 55, 25, 45])
highest_price = np.array([28, 24, 55, 48, 30, 32, 60, 30, 37, 43])
lowest_price = np.array([20, 23, 32, 24, 42, 27, 18, 39, 47, 30])

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(years, opening_price, marker='o', color='blue', linewidth=2)
ax.plot(years, closing_price, marker='o', color='green', linewidth=2)
ax.plot(years, highest_price, marker='o', color='red', linewidth=2)
ax.plot(years, lowest_price, marker='o', color='orange', linewidth=2)

ax.set_title('XYZ Ltd. Stock Performance (13-22)', fontsize=16, fontweight='bold')
ax.set_ylabel('USD Value', fontsize=14)
ax.set_xlabel('Year of Trading', fontsize=14)

plt.xticks(years, rotation=45)
plt.tight_layout(pad=4)
plt.show()