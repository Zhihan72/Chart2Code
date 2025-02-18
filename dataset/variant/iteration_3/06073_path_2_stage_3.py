import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

north_america = np.array([2200, 2185, 2170, 2160, 2140, 2120, 2100, 2085, 2070, 2060, 2045, 2025, 
                          2005, 1985, 1970, 1950, 1935, 1915, 1900, 1885, 1870])
south_america = np.array([5400, 5375, 5350, 5325, 5300, 5275, 5250, 5225, 5200, 5175, 5150, 5125, 
                          5100, 5075, 5050, 5025, 5000, 4975, 4950, 4925, 4900])
africa = np.array([1800, 1790, 1780, 1770, 1760, 1750, 1740, 1730, 1720, 1710, 1700, 1690, 1680, 
                   1670, 1660, 1650, 1640, 1630, 1620, 1610, 1600])
europe = np.array([1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 
                   1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210])
asia = np.array([2200, 2195, 2190, 2185, 2180, 2175, 2170, 2165, 2160, 2155, 2150, 2145, 2140,
                 2135, 2130, 2125, 2120, 2115, 2110, 2105, 2100])
australia = np.array([1370, 1365, 1360, 1355, 1350, 1345, 1340, 1335, 1330, 1325, 1320, 1315, 
                      1310, 1305, 1300, 1295, 1290, 1285, 1280, 1275, 1270])

regions = np.row_stack((north_america, south_america, africa, europe, asia, australia))

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', '#8F33FF']

ax.stackplot(years, regions, colors=colors, alpha=0.8)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(0, 5501, 500))

# Borders (spines) are removed
for spine in ax.spines.values():
    spine.set_visible(False)

# Grid removal
ax.yaxis.grid(False)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()