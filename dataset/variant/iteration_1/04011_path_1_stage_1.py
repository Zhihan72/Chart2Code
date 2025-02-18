import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

cars_usage = [700, 720, 740, 760, 750, 740, 730, 720, 710, 700]
bicycles_usage = [120, 130, 150, 170, 200, 230, 250, 270, 290, 300]
public_transit_usage = [300, 310, 320, 340, 350, 370, 400, 430, 450, 470]
walking_usage = [150, 160, 170, 180, 190, 200, 210, 220, 230, 250]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, cars_usage, marker='o', linestyle='-', linewidth=2, color='royalblue')
ax.plot(years, bicycles_usage, marker='s', linestyle='-', linewidth=2, color='forestgreen')
ax.plot(years, public_transit_usage, marker='^', linestyle='-', linewidth=2, color='firebrick')
ax.plot(years, walking_usage, marker='d', linestyle='-', linewidth=2, color='goldenrod')

ax.set_title('Trends in Transportation Mode Usage in Metroville\n(2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Trips (Thousands)', fontsize=14)
ax.set_xticks(years)
ax.set_ylim(0, 800)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.annotate('Surge in Bicycle Usage', xy=(2017, 200), xytext=(2015, 300),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Steady Growth in Public Transit', xy=(2018, 430), xytext=(2017, 550),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Decrease in Car Trips', xy=(2016, 740), xytext=(2014, 780),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()