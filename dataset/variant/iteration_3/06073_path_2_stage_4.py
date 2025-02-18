import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

# Randomly altered the data within certain data groups
north_america = np.array([2170, 2165, 2200, 2185, 2145, 2120, 2125, 2085, 2060, 2070, 2100, 2005, 
                          1915, 1985, 1970, 1950, 2140, 1935, 1885, 1900, 1870])
south_america = np.array([5375, 5325, 5300, 5400, 5275, 5250, 5250, 5100, 5200, 5175, 5350, 5150, 
                          4900, 4925, 5050, 5025, 5075, 4975, 4950, 4975, 5225])
africa = np.array([1760, 1790, 1780, 1770, 1800, 1750, 1660, 1730, 1720, 1710, 1690, 1700, 1680, 
                   1740, 1670, 1650, 1640, 1620, 1630, 1610, 1600])
europe = np.array([1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1010, 1140, 
                   1130, 1150, 1160, 1170, 1180, 1190, 1200, 1210])
asia = np.array([2185, 2195, 2190, 2200, 2175, 2170, 2145, 2165, 2150, 2155, 2180, 2140, 2145,
                 2135, 2130, 2125, 2120, 2115, 2110, 2105, 2100])
australia = np.array([1370, 1360, 1365, 1345, 1350, 1355, 1330, 1335, 1330, 1325, 1320, 1315, 
                      1310, 1305, 1300, 1295, 1290, 1285, 1280, 1275, 1270])

regions = np.row_stack((north_america, south_america, africa, europe, asia, australia))

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', '#8F33FF']

ax.stackplot(years, regions, colors=colors, alpha=0.8)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(0, 5501, 500))

for spine in ax.spines.values():
    spine.set_visible(False)

ax.yaxis.grid(False)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()