import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2026)
energy = [400, 385, 370, 350, 330, 310, 290, 270, 250, 230, 215]
transport = [300, 295, 285, 275, 260, 245, 230, 215, 200, 185, 170]
industry = [250, 245, 240, 230, 220, 210, 200, 190, 180, 170, 160]
agriculture = [150, 148, 145, 142, 138, 132, 125, 118, 112, 108, 100]
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