import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
north_america = np.array([4, 6, 3.5, 5.8, 5, 6.2, 5.5, 3, 4.2, 4.8])
south_america = np.array([1.8, 1.4, 2.4, 2.2, 1.2, 2, 1, 1.5, 1.7, 2.6])
europe = np.array([9, 8, 10.5, 8.5, 7, 9.2, 11, 7.5, 9.5, 10])
asia = np.array([8.3, 9, 5.5, 8, 8.7, 7, 5, 6, 6.5, 7.5])
africa = np.array([0.7, 1.3, 0.5, 1, 0.6, 1.2, 1.7, 0.8, 1.5, 1.9])
oceania = np.array([0.6, 0.55, 0.35, 0.48, 0.3, 0.65, 0.7, 0.5, 0.4, 0.45])

tourism_data = np.vstack([north_america, south_america, europe, asia, africa, oceania])

fig, ax = plt.subplots(figsize=(14, 8))

new_colors = ['#17becf', '#bcbd22', '#e377c2', '#7f7f7f', '#b5cf6b', '#ffbb78']

ax.stackplot(years, tourism_data, labels=['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania'], colors=new_colors, alpha=0.8)

ax.set_title("Decade of Tourism: \nTourists to the Country by Continent (2010-2019)", fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Year', fontsize=12, weight='bold')
ax.set_ylabel('Millions of Tourists', fontsize=12, weight='bold')
ax.legend(loc='upper left', title='Continents', fontsize=10, bbox_to_anchor=(1, 1), title_fontsize='13')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 13, 1))
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

peak_year = 2017
peak_value = np.sum(tourism_data[:, years == peak_year])
ax.axvline(x=peak_year, color='grey', linestyle='--', lw=1)
ax.annotate(f'Peak Tourism Year\nTotal: {peak_value} million', xy=(peak_year, peak_value), xytext=(peak_year+1, peak_value-2), 
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkred')

plt.tight_layout()
plt.show()