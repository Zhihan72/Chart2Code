import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

technology_index = [40 + 3*np.sin(0.3*x) + 5*np.log(x+1) for x in range(len(years))]
environment_index = [45 + 2*np.cos(0.2*x) + 4*np.sqrt(x) for x in range(len(years))]
medicine_index = [48 + 1.5*np.sin(0.2*x + np.pi/4) + 3.5*np.sqrt(x) for x in range(len(years))]
history_index = [35 + np.sin(0.5*x) + 2*x/10 for x in range(len(years))]
physics_index = [50 + np.cos(0.4*x + np.pi/6) + 2.5*np.log(x+1) for x in range(len(years))]
mathematics_index = [38 + 1.2*np.sin(0.25*x + np.pi/3) + 2.8*np.sqrt(x) for x in range(len(years))]

# New data series
astronomy_index = [47 + 2.5*np.sin(0.25*x) + 3.2*x/10 for x in range(len(years))]
linguistics_index = [36 + 1.8*np.cos(0.3*x + np.pi/4) + 2*x/5 for x in range(len(years))]

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

ax[0].plot(years, technology_index, marker='o', linestyle='-', linewidth=2, color='b')
ax[0].plot(years, environment_index, marker='s', linestyle='--', linewidth=2, color='g')
ax[0].plot(years, medicine_index, marker='^', linestyle='-.', linewidth=2, color='r')
ax[0].plot(years, history_index, marker='d', linestyle=':', linewidth=2, color='m')
ax[0].plot(years, physics_index, marker='x', linestyle='-', linewidth=2, color='c')
ax[0].plot(years, mathematics_index, marker='p', linestyle='--', linewidth=2, color='orange')
ax[0].plot(years, astronomy_index, marker='*', linestyle='-', linewidth=2, color='y')
ax[0].plot(years, linguistics_index, marker='h', linestyle='--', linewidth=2, color='purple')

ax[0].set_xlabel('Year')
ax[0].set_ylabel('Global Knowledge Index')
ax[0].set_title('Two Decades of Knowledge Growth\nA Comparative Analysis (2000-2030)', fontweight='bold')

ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].spines['left'].set_visible(False)

ax[0].annotate('Tech Breakthrough', xy=(2025, technology_index[25]), xytext=(2018, 80),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)
ax[0].annotate('Medicine Peak', xy=(2015, medicine_index[15]), xytext=(2008, 65),
               arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)

moving_avg = np.convolve(technology_index, np.ones(5)/5, mode='valid')

ax[1].plot(years[2:-2], moving_avg, color='blue', linestyle='-', linewidth=2)

ax[1].set_xlabel('Year')
ax[1].set_ylabel('5-Year Moving Average')
ax[1].set_title('Statistical Insights on Technology', fontweight='bold')

ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(False)
ax[1].spines['left'].set_visible(False)

plt.tight_layout()
plt.show()