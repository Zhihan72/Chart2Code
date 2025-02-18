import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
city_zephyr = np.array([500, 550, 600, 650, 700])
city_aerios = np.array([400, 450, 470, 490, 520])
city_nimus = np.array([300, 350, 400, 450, 460])

fig, ax = plt.subplots(figsize=(12, 7))

# Using the same color for all data groups
ax.plot(years, city_zephyr, marker='o', linestyle='-', color='dodgerblue')
ax.plot(years, city_aerios, marker='s', linestyle='-', color='dodgerblue')
ax.plot(years, city_nimus, marker='^', linestyle='-', color='dodgerblue')

ax.set_title('Energy Consumption Trends on Planet Xaerith (2018-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (GWh)', fontsize=14)
ax.set_xticks(years)

milestones = [
    (2018, 500, 'Zephyr: Population Boom'),
    (2020, 470, 'Aerios: New Renewable Plant'),
    (2021, 450, 'Nimus: Industrial Expansion')
]

for (year, value, text) in milestones:
    ax.annotate(text, xy=(year, value), xytext=(year + 0.1, value + 50 if value < 600 else value - 50),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='gray'),
                fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.5))

plt.tight_layout()

plt.show()