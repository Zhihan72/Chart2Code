import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

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

gas_bills = np.array([
    [25, 26, 27, 30, 31, 32, 33, 35, 36, 38, 39, 40],
    [35, 36, 38, 40, 42, 44, 45, 47, 49, 50, 52, 54],
    [45, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66],
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF'] 
bar_width = 0.3
x = np.arange(len(months))

ax.bar(x - bar_width, electricity_bills[0], width=bar_width, label='Electric (Small)', color=colors[0], hatch='/')
ax.bar(x - bar_width, water_bills[0], width=bar_width, bottom=electricity_bills[0], color=colors[1], hatch='\\')
ax.bar(x - bar_width, gas_bills[0], width=bar_width, bottom=electricity_bills[0] + water_bills[0], color=colors[2], hatch='|')

ax.bar(x, electricity_bills[1], width=bar_width, label='Electric (Medium)', color=colors[0], linestyle='--', edgecolor='black')
ax.bar(x, water_bills[1], width=bar_width, bottom=electricity_bills[1], color=colors[1], linestyle='-.', edgecolor='black')
ax.bar(x, gas_bills[1], width=bar_width, bottom=electricity_bills[1] + water_bills[1], color=colors[2], linestyle=':', edgecolor='black')

ax.bar(x + bar_width, electricity_bills[2], width=bar_width, label='Electric (Large)', color=colors[0], hatch='x')
ax.bar(x + bar_width, water_bills[2], width=bar_width, bottom=electricity_bills[2], color=colors[1], hatch='+')
ax.bar(x + bar_width, gas_bills[2], width=bar_width, bottom=electricity_bills[2] + water_bills[2], color=colors[2], hatch='o')

ax.set_title("Monthly Utility Bills for Different House Sizes", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Utility Bills (in dollars)", fontsize=12)

ax.set_xticks(x)
ax.set_xticklabels(months)

ax.legend(loc='upper right', fontsize=10, title='Utility (Size)', shadow=True)

ax.yaxis.grid(True, linestyle='-', linewidth=0.5, alpha=0.5)
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()