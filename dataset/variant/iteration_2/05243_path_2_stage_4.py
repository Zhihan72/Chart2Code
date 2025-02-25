import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021, 4)

solaria_investment = [5, 10, 15, 25, 35, 50]
ventura_investment = [3, 8, 12, 20, 30, 40]
hydrona_investment = [2, 7, 10, 15, 25, 35]
geotherma_investment = [1, 4, 7, 10, 17, 25]
aquatera_investment = [4, 9, 11, 18, 28, 38]

solaria_impact = [1, 5, 10, 20, 35, 50]
ventura_impact = [2, 4, 8, 15, 25, 40]
hydrona_impact = [0.5, 3, 6, 10, 20, 30]
geotherma_impact = [0.2, 2, 5, 8, 15, 25]
aquatera_impact = [1.5, 5, 9, 13, 22, 33]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

# Use a single color for all plots
color = '#FF6347'  # Tomato color

# First subplot
ax1.plot(years, solaria_investment, marker='o', linestyle='-', color=color, linewidth=2)
ax1.plot(years, ventura_investment, marker='s', linestyle='--', color=color, linewidth=2)
ax1.plot(years, hydrona_investment, marker='^', linestyle='-.', color=color, linewidth=2)
ax1.plot(years, geotherma_investment, marker='D', linestyle=':', color=color, linewidth=2)
ax1.plot(years, aquatera_investment, marker='*', linestyle='-', color=color, linewidth=2)

ax1.set_title('Renewable Energy Investment Growth (2000-2020)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Investment (Billion Dollars)', fontsize=14)
ax1.set_xticks(years)

for spine in ax1.spines.values():
    spine.set_visible(False)

# Second subplot
ax2.plot(years, solaria_impact, marker='o', linestyle='-', color=color, linewidth=2)
ax2.plot(years, ventura_impact, marker='s', linestyle='--', color=color, linewidth=2)
ax2.plot(years, hydrona_impact, marker='^', linestyle='-.', color=color, linewidth=2)
ax2.plot(years, geotherma_impact, marker='D', linestyle=':', color=color, linewidth=2)
ax2.plot(years, aquatera_impact, marker='*', linestyle='-', color=color, linewidth=2)

ax2.set_title('Impact of Renewable Energy on Total Energy (2000-2020)', fontsize=16, weight='bold', pad=20)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Energy Contribution (%)', fontsize=14)
ax2.set_xticks(years)

for spine in ax2.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()