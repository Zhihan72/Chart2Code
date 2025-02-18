import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

usa_ev_growth = np.array([1, 5, 10, 20, 35, 60, 100, 155, 230, 330, 450, 590, 740])
china_ev_growth = np.array([1, 4, 12, 30, 65, 130, 280, 550, 950, 1400, 2000, 2800, 3800])
norway_ev_growth = np.array([0.5, 1.2, 2.8, 7, 15, 33, 70, 150, 290, 520, 800, 1200, 1700])

fig, axs = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('EV Growth (2010-2022)', fontsize=16, fontweight='bold')

# First subplot: Line Chart for EV growth
axs[0].plot(years, usa_ev_growth, color='blue', linestyle='-', marker='o', linewidth=2)
axs[0].plot(years, china_ev_growth, color='red', linestyle='-', marker='s', linewidth=2)
axs[0].plot(years, norway_ev_growth, color='green', linestyle='-', marker='^', linewidth=2)

axs[0].set_title('EVs in Use', fontsize=13, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=11)
axs[0].set_ylabel('EVs (k)', fontsize=11)

axs[0].annotate('Rapid in China', xy=(2017, 130), xytext=(2015, 700),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')
axs[0].annotate('Norway Leads', xy=(2016, 33), xytext=(2013, 300),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')

# Second subplot: Stacked Line Chart for relative contributions
usa_contribution = usa_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)
china_contribution = china_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)
norway_contribution = norway_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)

axs[1].plot(years, usa_contribution, color='blue', linestyle='--', marker='o', linewidth=2)
axs[1].plot(years, china_contribution, color='red', linestyle='--', marker='s', linewidth=2)
axs[1].plot(years, norway_contribution, color='green', linestyle='--', marker='^', linewidth=2)

axs[1].set_title('Contribution to Global EVs', fontsize=13, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=11)
axs[1].set_ylabel('Global EV Share', fontsize=11)

fig.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()