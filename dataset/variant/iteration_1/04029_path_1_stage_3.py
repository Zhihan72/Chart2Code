import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
# Manually altered values within the same dimensional structure
energy = [410, 370, 375, 340, 320, 315, 300, 260, 255, 235, 220]
transport = [290, 300, 280, 270, 270, 250, 240, 210, 205, 180, 160]
industry = [260, 240, 235, 225, 215, 205, 195, 185, 175, 165, 155]
agriculture = [140, 150, 150, 140, 135, 130, 120, 115, 110, 110, 105]
total_emissions = np.array(energy) + np.array(transport) + np.array(industry) + np.array(agriculture)

fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

ax1.stackplot(years, energy, transport, industry, agriculture, colors=['#66b3ff', '#99ff99', '#ff9999', '#ffcc99'], alpha=0.7)
ax2.plot(years, total_emissions, 'k--', linewidth=2)

for i, value in enumerate(total_emissions):
    ax2.annotate(f'{value}', (years[i], total_emissions[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=8)

ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('CO2 Emissions by Sector (MMT)', fontsize=14)
ax2.set_ylabel('Total CO2 Emissions (MMT)', fontsize=14)

ax1.tick_params(axis='x', labelrotation=45)
plt.tight_layout()
plt.show()