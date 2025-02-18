import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [1.2, 1.6, 2.0, 2.8, 3.5, 4.2, 5.1, 6.3, 7.4, 8.6, 9.8]
wind = [2.5, 3.0, 3.8, 4.5, 5.1, 5.8, 6.3, 7.0, 7.8, 9.0, 10.2]
hydro = [8.1, 8.2, 8.4, 8.5, 8.7, 8.9, 9.0, 9.2, 9.3, 9.5, 9.7]
geothermal = [0.4, 0.6, 0.8, 0.9, 1.0, 1.1, 1.3, 1.5, 1.6, 1.8, 2.0]

single_color = '#ff7f0e'
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar, color=single_color, marker='o', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, wind, color=single_color, marker='s', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, hydro, color=single_color, marker='^', linestyle='-', linewidth=2, markersize=8)
ax.plot(years, geothermal, color=single_color, marker='d', linestyle='-', linewidth=2, markersize=8)

ax.set_title("Renewable Energy Generation in EcoVille (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Energy Generation (GW)", fontsize=14)
ax.set_xticks(years)

ax.annotate('Major Solar Farm Established', xy=(2015, 4.2), xytext=(2013, 6),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()