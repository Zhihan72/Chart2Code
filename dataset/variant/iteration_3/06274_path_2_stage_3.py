import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

tiger_population = np.array([3200, 3150, 3090, 3000, 2950, 2850, 2770, 2690, 2650, 2580, 2550, 2600, 2700, 2820, 3010, 
                             3210, 3420, 3500, 3550, 3690, 3800])
panda_population = np.array([1000, 1015, 1030, 1060, 1080, 1100, 1125, 1150, 1190, 1230, 1260, 1290, 1320, 1340, 1370, 
                             1400, 1425, 1450, 1480, 1510, 1550])
rhino_population = np.array([1450, 1460, 1470, 1455, 1440, 1420, 1410, 1405, 1410, 1420, 1435, 1450, 1480, 1500, 1530, 
                             1560, 1600, 1620, 1650, 1665, 1700])
elephant_population = np.array([5000, 5050, 5100, 5150, 5200, 5280, 5360, 5500, 5600, 5750, 5900, 6100, 6300, 6500, 6700, 
                                6900, 7100, 7300, 7500, 7700, 7900])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, tiger_population, marker='o', linestyle='-', color='purple', linewidth=2, markersize=6, label='Tigers')
ax.plot(years, panda_population, marker='s', linestyle='-', color='pink', linewidth=2, markersize=6, label='Pandas')
ax.plot(years, rhino_population, marker='^', linestyle='-', color='brown', linewidth=2, markersize=6, label='Rhinos')
ax.plot(years, elephant_population, marker='d', linestyle='-', color='cyan', linewidth=2, markersize=6, label='Elephants')

ax.set_title("Endangered Species (2000-20)", fontsize=18, weight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Population", fontsize=14)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(1000, 8100, 1000))
ax.grid(True, linestyle='--', alpha=0.6)

ax.annotate("Efforts Up", 
            xy=(2012, 2600), xytext=(2005, 3300),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, fontweight='bold', color='black')

ax.annotate("Pandas Grow", 
            xy=(2020, 1550), xytext=(2014, 1800),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=12, fontweight='bold', color='black')

ax.legend(title="Species", fontsize=12, title_fontsize=14, loc='upper left')

plt.tight_layout()
plt.show()