import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

electricity_bills = np.array([
    [60, 65, 70, 55, 80, 85, 75, 50, 105, 100, 90, 95],
    [100, 130, 125, 90, 85, 125, 110, 95, 135, 80, 115, 120],
    [160, 125, 145, 130, 140, 165, 155, 175, 150, 170, 120, 135],
])

water_bills = np.array([
    [31, 22, 25, 40, 33, 24, 28, 38, 35, 36, 30, 20],
    [45, 50, 32, 37, 43, 41, 48, 30, 34, 35, 47, 39],
    [55, 51, 46, 60, 42, 58, 50, 44, 40, 48, 53, 57],
])

gas_bills = np.array([
    [36, 38, 40, 25, 33, 30, 26, 39, 35, 32, 31, 27],
    [40, 47, 54, 38, 50, 44, 49, 52, 35, 42, 45, 36],
    [62, 50, 66, 56, 48, 64, 60, 58, 55, 46, 52, 45],
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

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()