import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

tiger_population = np.array([3200, 3150, 3090, 3000, 2950, 2850, 2770, 2690, 2650, 2580, 2550, 2600, 2700, 2820, 3010, 
                             3210, 3420, 3500, 3550, 3690, 3800])
panda_population = np.array([1000, 1015, 1030, 1060, 1080, 1100, 1125, 1150, 1190, 1230, 1260, 1290, 1320, 1340, 1370, 
                             1400, 1425, 1450, 1480, 1510, 1550])
rhino_population = np.array([1450, 1460, 1470, 1455, 1440, 1420, 1410, 1405, 1410, 1420, 1435, 1450, 1480, 1500, 1530, 
                             1560, 1600, 1620, 1650, 1665, 1700])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, tiger_population, marker='*', linestyle='--', color='blue', linewidth=2, markersize=8, label='Tigers')
ax.plot(years, panda_population, marker='d', linestyle='-.', color='red', linewidth=2, markersize=8, label='Pandas')
ax.plot(years, rhino_population, marker='+', linestyle=':', color='purple', linewidth=2, markersize=8, label='Rhinos')

ax.set_title("Endangered Species (2000-2020)", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14, labelpad=10)
ax.set_ylabel("Population", fontsize=14, labelpad=10)

ax.set_xticks(np.arange(2000, 2021, 2))
ax.set_yticks(np.arange(1000, 4100, 500))
ax.grid(True, linestyle='-.', alpha=0.8)

ax.annotate("Conservation Efforts", 
            xy=(2012, 2600), xytext=(2005, 3300),
            arrowprops=dict(facecolor='green', arrowstyle='-|>', lw=1.5),
            fontsize=12, fontweight='bold', color='darkgreen')

ax.annotate("Growth in Pandas", 
            xy=(2020, 1550), xytext=(2014, 1800),
            arrowprops=dict(facecolor='green', arrowstyle='-|>', lw=1.5),
            fontsize=12, fontweight='bold', color='darkgreen')

ax.legend(title="Species", fontsize=12, title_fontsize=14, loc='lower right')

plt.tight_layout()
plt.show()