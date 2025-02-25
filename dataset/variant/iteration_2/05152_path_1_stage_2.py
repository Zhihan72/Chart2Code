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

bar_width = 0.2
x = np.arange(len(months))

ax.bar(x - bar_width, electricity_bills[0], width=bar_width, color='#FF5733')
ax.bar(x - bar_width, water_bills[0], width=bar_width, bottom=electricity_bills[0], color='#33FFBD')
ax.bar(x - bar_width, gas_bills[0], width=bar_width, bottom=electricity_bills[0] + water_bills[0], color='#3380FF')

ax.bar(x, electricity_bills[1], width=bar_width, color='#C70039')
ax.bar(x, water_bills[1], width=bar_width, bottom=electricity_bills[1], color='#7DFF33')
ax.bar(x, gas_bills[1], width=bar_width, bottom=electricity_bills[1] + water_bills[1], color='#FF33B5')

ax.bar(x + bar_width, electricity_bills[2], width=bar_width, color='#900C3F')
ax.bar(x + bar_width, water_bills[2], width=bar_width, bottom=electricity_bills[2], color='#FFD133')
ax.bar(x + bar_width, gas_bills[2], width=bar_width, bottom=electricity_bills[2] + water_bills[2], color='#33D1FF')

ax.set_title("Monthly Utility Bills for Different House Sizes in 2023\nSuburban Neighborhood", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Utility Bills (in dollars)", fontsize=12)

ax.set_xticks(x)
ax.set_xticklabels(months)

# Removing grid and legend
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()