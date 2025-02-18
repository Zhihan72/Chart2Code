import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2023)

usa_ev_growth = np.array([1, 20, 10, 5, 35, 60, 100, 230, 330, 155, 450, 740, 590])
china_ev_growth = np.array([1, 12, 30, 4, 130, 280, 65, 950, 550, 1400, 2000, 3800, 2800])
norway_ev_growth = np.array([0.5, 7, 2.8, 1.2, 33, 70, 15, 290, 150, 800, 520, 1700, 1200])

fig, axs = plt.subplots(2, 1, figsize=(10,12))
fig.suptitle('EV Usage Rise Insights (2010-2022)', fontsize=16, fontweight='bold')

usa_contribution = usa_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)
china_contribution = china_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)
norway_contribution = norway_ev_growth / (usa_ev_growth + china_ev_growth + norway_ev_growth)

axs[0].plot(years, usa_contribution, label='USA Share', color='blue', linestyle='--', marker='o', linewidth=2)
axs[0].plot(years, china_contribution, label='China Share', color='red', linestyle='--', marker='s', linewidth=2)
axs[0].plot(years, norway_contribution, label='Norway Share', color='green', linestyle='--', marker='^', linewidth=2)

axs[0].set_title('Proportionate Contribution to EV Expansion', fontsize=13, fontweight='bold')
axs[0].set_xlabel('Timeline', fontsize=11)
axs[0].set_ylabel('Global EV Fraction', fontsize=11)
axs[0].legend(loc='upper left', fontsize=9)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)

axs[1].plot(years, usa_ev_growth, label='USA Growth', color='blue', linestyle='-', marker='o', linewidth=2)
axs[1].plot(years, china_ev_growth, label='China Growth', color='red', linestyle='-', marker='s', linewidth=2)
axs[1].plot(years, norway_ev_growth, label='Norway Growth', color='green', linestyle='-', marker='^', linewidth=2)

axs[1].set_title('EV Population Surge per Country', fontsize=13, fontweight='bold')
axs[1].set_xlabel('Timeline', fontsize=11)
axs[1].set_ylabel('EV Count (thousands)', fontsize=11)
axs[1].legend(title="Nation", loc='upper left', fontsize=9)
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5)

axs[1].annotate('China\'s Boost', xy=(2017, 130), xytext=(2015, 700),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')
axs[1].annotate('Norway\'s Pioneering', xy=(2016, 33), xytext=(2013, 300),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, backgroundcolor='w')

fig.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()