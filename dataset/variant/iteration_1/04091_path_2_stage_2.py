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
    colors=['#FFD700', '#7FFFD4', '#1E90FF', '#B22222', '#FF8C00'], alpha=0.7
)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Generation (GWh)', fontsize=14)
ax1.set_title('Decade of Energy Transition:\nGeneration by Source', fontsize=18, fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

ax2.fill_between(years, 0, total, color='lightsteelblue', alpha=0.7)
ax2.fill_between(years, 0, renewable + nuclear, color='lightgreen', alpha=0.8)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Total Energy Generation (GWh)', fontsize=14)
ax2.set_title('Cumulative Energy Generation by Year', fontsize=18, fontweight='bold')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()