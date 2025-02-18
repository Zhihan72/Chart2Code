import matplotlib.pyplot as plt
import numpy as np

years = np.array([2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023])

species_a_landing_density = np.array([30, 45, 33, 35, 65, 50, 60, 55, 37, 62])
species_b_landing_density = np.array([27, 20, 30, 42, 25, 35, 38, 45, 32, 40])
species_c_landing_density = np.array([17, 10, 23, 15, 25, 13, 30, 27, 32, 35])

landing_site_sizes_a = np.array([7, 5, 6, 9, 6, 8, 7, 10, 6, 8])
landing_site_sizes_b = np.array([5, 4, 8, 5, 4, 6, 7, 8, 6, 7])
landing_site_sizes_c = np.array([5, 4, 6, 3, 5, 4, 7, 6, 8, 7])

fig, ax = plt.subplots(figsize=(14, 8))

scatter_a = ax.scatter(years, species_a_landing_density, s=landing_site_sizes_a*30, c=landing_site_sizes_a, cmap='Reds', alpha=0.7, edgecolor='purple', label='Species A')
scatter_b = ax.scatter(years, species_b_landing_density, s=landing_site_sizes_b*30, c=landing_site_sizes_b, cmap='Greens', alpha=0.7, edgecolor='orange', label='Species B')
scatter_c = ax.scatter(years, species_c_landing_density, s=landing_site_sizes_c*30, c=landing_site_sizes_c, cmap='Blues', alpha=0.7, edgecolor='royalblue', label='Species C')

trend_line = np.poly1d(np.polyfit(years, species_a_landing_density, 3))
year_range = np.linspace(years.min(), years.max(), 300)
ax.plot(year_range, trend_line(year_range), color='maroon', linestyle='-', linewidth=2, label='Species A Trend')

trend_line_b = np.poly1d(np.polyfit(years, species_b_landing_density, 3))
ax.plot(year_range, trend_line_b(year_range), color='forestgreen', linestyle='-.', linewidth=2, label='Species B Trend')

trend_line_c = np.poly1d(np.polyfit(years, species_c_landing_density, 3))
ax.plot(year_range, trend_line_c(year_range), color='navy', linestyle=':', linewidth=2, label='Species C Trend')

ax.set_title('Migration Patterns of Bird Species (2005 - 2023)', fontsize=16, fontweight='bold', color='navy')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Landing Density (Birds per km²)', fontsize=12)

legend1 = ax.legend(loc='lower left', frameon=True, fontsize=12)
ax.legend(loc='lower right', fontsize=12)
ax.add_artist(legend1)

colorbar = fig.colorbar(scatter_a, ax=ax, orientation='vertical')
colorbar.set_label('Landing Site Size (hectares)', fontsize=12)

ax.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.show()