import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)
revenue = np.array([50, 120, 180, 260, 350])
profit = revenue - np.array([30, 70, 110, 130, 150])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, revenue, marker='o', linestyle='-', linewidth=2, color='blue', label='Rev')
ax.plot(years, profit, marker='^', linestyle=':', linewidth=2, color='green', label='Prof')

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Amount (k$)', fontsize=12)
ax.set_title("Startup Growth: Revenue & Profit (2018-22)", fontsize=14, fontweight='bold', pad=20)

ax.legend(title='Metrics', loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate('Major Profit', xy=(2019, profit[1]), xytext=(2019, profit[1] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()