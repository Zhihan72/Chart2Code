import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

cars_usage = [700, 720, 740, 760, 750, 740, 730, 720, 710, 700]
bicycles_usage = [120, 130, 150, 170, 200, 230, 250, 270, 290, 300]
public_transit_usage = [300, 310, 320, 340, 350, 370, 400, 430, 450, 470]
walking_usage = [150, 160, 170, 180, 190, 200, 210, 220, 230, 250]
scooters_usage = [0, 0, 20, 30, 50, 110, 130, 150, 160, 180]

fig, ax = plt.subplots(figsize=(14, 8))

# Changed styles for visualization
ax.plot(years, cars_usage, label='Automobiles', marker='h', linestyle='--', linewidth=1, color='darkorange')
ax.plot(years, bicycles_usage, label='Cycles', marker='*', linestyle='-.', linewidth=1, color='mediumslateblue')
ax.plot(years, public_transit_usage, label='Mass Transit', marker='v', linestyle=':', linewidth=3, color='darkcyan')
ax.plot(years, walking_usage, label='Foot Traffic', marker='<', linestyle='--', linewidth=1, color='olive')
ax.plot(years, scooters_usage, label='Electric Scooters', marker='p', linestyle='-', linewidth=2, color='deeppink')

ax.set_title('Evolution of Commute Patterns in Metro City\n(2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Calendar Year', fontsize=14)
ax.set_ylabel('Trips Count (in Thousands)', fontsize=14)
ax.set_xticks(years)
ax.set_ylim(0, 800)

# Modified grid style
ax.grid(True, linestyle=':', alpha=0.3)

# Altered legend location and style
ax.legend(title='Transportation Methods', loc='center right', frameon=False)

# Keeping some annotations intact to maintain context
ax.annotate('Dwindling Automobile Usage', xy=(2016, 740), xytext=(2014, 780),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()

plt.show()