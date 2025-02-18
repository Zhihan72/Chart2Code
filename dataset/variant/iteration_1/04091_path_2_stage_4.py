import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = np.array([5, 10, 18, 30, 45, 65, 90, 120, 155, 200, 250])
wind = np.array([10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 340])
hydro = np.array([60, 63, 65, 68, 70, 72, 74, 76, 78, 80, 82])
fossil = np.array([300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200])
nuclear = np.array([50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70])

renewable = solar + wind + hydro
total = renewable + fossil + nuclear

fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16, 12))

ax1.stackplot(
    years, solar, wind, hydro, fossil, nuclear,
    colors=['#FF6347', '#4682B4', '#32CD32', '#8B4513', '#9932CC'], alpha=0.7
)
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Power Production (GWh)', fontsize=14)
ax1.set_title('Shift in Energy Production over a Decade', fontsize=18, fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

ax2.fill_between(years, 0, total, color='mediumorchid', alpha=0.7)
ax2.fill_between(years, 0, renewable + nuclear, color='mediumseaGreen', alpha=0.8)
ax2.set_xlabel('Timeline', fontsize=14)
ax2.set_ylabel('Aggregate Energy Production (GWh)', fontsize=14)
ax2.set_title('Annual Energy Yield Totals', fontsize=18, fontweight='bold')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()