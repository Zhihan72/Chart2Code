import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = np.array([5, 10, 18, 30, 45, 65, 90, 120, 155, 200, 250])
wind = np.array([10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 340])
hydro = np.array([60, 63, 65, 68, 70, 72, 74, 76, 78, 80, 82])
fossil = np.array([300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200])

renewable = solar + wind + hydro
total = renewable + fossil

fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16, 12))

ax1.stackplot(years, solar, wind, hydro, fossil,
              labels=['Sun', 'Windy', 'Water', 'Traditional'],
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33F6'], alpha=0.7)
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Generation in GWh', fontsize=14)
ax1.set_title('Energy Evolution 2010-2020:\nSupply by Type', fontsize=18, fontweight='bold')
ax1.legend(loc='upper right', title='Kinds of Energy', shadow=True, fancybox=True)
ax1.grid(visible=False)
ax1.annotate('Renewable Surge', xy=(2014, 140), xytext=(2011, 250),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax2.fill_between(years, 0, total, label='All-inclusive Energy', color='#A1CAF1', hatch='/', alpha=0.5)
ax2.fill_between(years, 0, renewable, label='Renewable Flow', color='#90EE90', hatch='\\', alpha=0.8)
ax2.set_xlabel('Era', fontsize=14)
ax2.set_ylabel('Overall Energy Production (GWh)', fontsize=14)
ax2.set_title('Yearly Energy Accumulation', fontsize=18, fontweight='bold')
ax2.legend(loc='lower center', title='Category of Power', frameon=False)
ax2.grid(visible=True, which='major', linestyle=':', linewidth=1.0, color='blue', alpha=0.5)
ax2.annotate('2020 Green Level', xy=(2020, renewable[-1]), xytext=(2017, renewable[-1] + 100),
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2", facecolor='red', shrinkA=5, shrinkB=5),
             fontsize=12)

plt.tight_layout()
plt.show()