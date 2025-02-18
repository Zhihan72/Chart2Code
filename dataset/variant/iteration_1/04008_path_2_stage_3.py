import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

revenue = np.array([180, 120, 350, 50, 260])
expenses = np.array([110, 70, 150, 30, 130])
profit = np.array([70, 50, 200, 20, 130])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, revenue, marker='o', linestyle='-', linewidth=2, color='red', label='Rev')
ax.plot(years, expenses, marker='s', linestyle='--', linewidth=2, color='green', label='Exp')
ax.plot(years, profit, marker='^', linestyle=':', linewidth=2, color='blue', label='Prof')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Amount (k$)', fontsize=12)
ax.set_title("Startup Metrics", fontsize=14, fontweight='bold', pad=20)

ax.legend(title='Legend', loc='upper left', fontsize=10)

ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate('Profit Peak', xy=(2019, profit[1]), xytext=(2019, profit[1] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Exp. Control', xy=(2021, expenses[3]), xytext=(2020, expenses[3] + 30),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()

plt.show()