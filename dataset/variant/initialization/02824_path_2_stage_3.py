import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
solar = [2, 3, 5, 10, 20, 30, 40]
geothermal = [3, 4, 6, 7, 10, 8, 5]
hydropower = [25, 30, 35, 28, 22, 18, 15]
biomass = [9, 8, 6, 5, 3, 2, 2]

data = np.vstack([solar, geothermal, hydropower, biomass])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(decades, data, colors=['#FF6347', '#40E0D0', '#FFDAB9', '#8A2BE2'], alpha=0.85)

ax.set_title('The Rise and Fall of Renewable Energy Sources in Urban Development\n(1960s to 2020s)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Energy Share (%)', fontsize=12)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()