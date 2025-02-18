import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

north_america = np.array([2200, 2185, 2170, 2160, 2140, 2120, 2100, 2085, 2070, 2060, 2045, 2025, 
                          2005, 1985, 1970, 1950, 1935, 1915, 1900, 1885, 1870])
south_america = np.array([5400, 5375, 5350, 5325, 5300, 5275, 5250, 5225, 5200, 5175, 5150, 5125, 
                          5100, 5075, 5050, 5025, 5000, 4975, 4950, 4925, 4900])
europe = np.array([1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 
                   1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210])
asia = np.array([2200, 2195, 2190, 2185, 2180, 2175, 2170, 2165, 2160, 2155, 2150, 2145, 2140,
                 2135, 2130, 2125, 2120, 2115, 2110, 2105, 2100])
australia = np.array([1370, 1365, 1360, 1355, 1350, 1345, 1340, 1335, 1330, 1325, 1320, 1315, 
                      1310, 1305, 1300, 1295, 1290, 1285, 1280, 1275, 1270])

# Stack to exclude the 'africa' dataset
regions = np.row_stack((north_america, south_america, europe, asia, australia))

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#6A994E', '#165B33', '#8A3AB9', '#D72638', '#288BA8'] # Removed color for the africa region
ax.stackplot(years, regions, labels=['NA Region', 'SA Continent', 'European Terrain', 'Asian Grounds', 'Aussie Area'], colors=colors, alpha=0.7)

ax.set_title('Global Lumber Regions (2000-2020)', fontsize=18, fontweight='normal', pad=15)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Thousand sq km', fontsize=14)

ax.set_xticks(np.arange(2000, 2021, 3))
ax.yaxis.grid(True, linestyle='-', linewidth=0.8, alpha=0.5)

ax.legend(loc='center left', fontsize=9, bbox_to_anchor=(1, 0.5))

highlight_years = {2005: "Enviro Summit", 2015: "Climate Accord"}
for year, event in highlight_years.items():
    ax.axvline(x=year, color='black', linestyle='-', linewidth=1)
    ax.text(year, 1000, event, rotation=90, verticalalignment='bottom', horizontalalignment='right', color='black', fontsize=8)

plt.xticks(rotation=30)
plt.tight_layout(rect=[0, 0, 0.9, 1])

plt.show()