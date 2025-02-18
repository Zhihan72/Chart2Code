import matplotlib.pyplot as plt
import numpy as np

electricity_bills = np.array([
    [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],
    [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175],
])

water_bills = np.array([
    [20, 22, 24, 25, 28, 30, 31, 33, 35, 36, 38, 40],
    [30, 32, 34, 35, 37, 39, 41, 43, 45, 47, 48, 50],
    [40, 42, 44, 46, 48, 50, 51, 53, 55, 57, 58, 60],
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57']
bar_width = 0.3
x = np.arange(12)

# Plot electricity bills (positive side)
ax.bar(x - bar_width, electricity_bills[0], width=bar_width, color=colors[0])
ax.bar(x, electricity_bills[1], width=bar_width, color=colors[0])
ax.bar(x + bar_width, electricity_bills[2], width=bar_width, color=colors[0])

# Plot water bills (negative side)
ax.bar(x - bar_width, -water_bills[0], width=bar_width, color=colors[1])
ax.bar(x, -water_bills[1], width=bar_width, color=colors[1])
ax.bar(x + bar_width, -water_bills[2], width=bar_width, color=colors[1])

ax.yaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.5)
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.axhline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()