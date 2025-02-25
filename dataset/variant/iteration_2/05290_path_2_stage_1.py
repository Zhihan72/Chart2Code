import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

# Manually altered original growth data to randomize within data groups.
usa_ev_growth = np.array([1, 20, 10, 5, 35, 60, 100, 230, 330, 155, 450, 740, 590])
china_ev_growth = np.array([1, 12, 30, 4, 130, 280, 65, 950, 550, 1400, 2000, 3800, 2800])
norway_ev_growth = np.array([0.5, 7, 2.8, 1.2, 33, 70, 15, 290, 150, 800, 520, 1700, 1200])

fig, axs = plt.subplots(2, 1, figsize=(10,12))
fig.suptitle('Electric Vehicle Growth Statistics (2010-2022)', fontsize=16, fontweight='bold')

# First subplot: Line Chart for EV growth
axs[0].plot(years, usa_ev_growth, label='USA', color='blue', linestyle='-', marker='o', linewidth=2)
axs[0].plot(years, china_ev_growth, label='China', color='red', linestyle='-', marker='s', linewidth=2)
axs[0].plot(years, norway_ev_growth, label='Norway', color='green', linestyle='-', marker='^', linewidth=2)

axs[0].set_title('Growth of Electric Vehicles in Use', fontsize=13, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=11)
axs[0].set_ylabel('Number of EVs (in thousands)', fontsize=11)
axs[0].legend(title="Country", loc='upper left', fontsize=9)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)

axs[0].annotate('Rapid Growth in China', xy=(2017, 130), xytext=(2015, 700),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')
axs[0].annotate('Early Adoption in Norway', xy=(2016, 33), xytext=(2013, 300),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')

# Second subplot: Manual Stacked Line Chart to show relative contributions
usa_contribution = usa_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)
china_contribution = china_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)
norway_contribution = norway_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)

axs[1].plot(years, usa_contribution, label='USA Contribution', color='blue', linestyle='--', marker='o', linewidth=2)
axs[1].plot(years, china_contribution, label='China Contribution', color='red', linestyle='--', marker='s', linewidth=2)
axs[1].plot(years, norway_contribution, label='Norway Contribution', color='green', linestyle='--', marker='^', linewidth=2)

axs[1].set_title('Relative Contribution to Global EV Growth', fontsize=13, fontweight='bold')
axs[1].set_xlabel('Year', fontsize=11)
axs[1].set_ylabel('Fraction of Global EVs', fontsize=11)
axs[1].legend(loc='upper left', fontsize=9)
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5)

fig.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()