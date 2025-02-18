import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

technology_index = [40 + 3 * np.sin(0.3 * x) + 5 * np.log(x + 1) for x in range(len(years))]
environment_index = [45 + 2 * np.cos(0.2 * x) + 4 * np.sqrt(x) for x in range(len(years))]
medicine_index = [48 + 1.5 * np.sin(0.2 * x + np.pi / 4) + 3.5 * np.sqrt(x) for x in range(len(years))]
history_index = [35 + np.sin(0.5 * x) + 2 * x / 10 for x in range(len(years))]
physics_index = [50 + np.cos(0.4 * x + np.pi / 6) + 2.5 * np.log(x + 1) for x in range(len(years))]
mathematics_index = [38 + 1.2 * np.sin(0.25 * x + np.pi / 3) + 2.8 * np.sqrt(x) for x in range(len(years))]

artificial_intelligence_index = [30 + 2.5 * np.sin(0.4 * x + np.pi / 5) + 4 * x / 20 for x in range(len(years))]
robotics_index = [42 + 3 * np.sin(0.2 * x - np.pi / 3) + 4.5 * np.sqrt(x) for x in range(len(years))]

fig, ax = plt.subplots(2, 1, figsize=(14, 10))

moving_avg = np.convolve(technology_index, np.ones(5) / 5, mode='valid')

# Plot with updated styles
ax[0].plot(years[2:-2], moving_avg, color='darkorange', linestyle='-.', linewidth=2.5, label='Tech 5-yr Avg')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('5-yr Moving Average')
ax[0].set_title('Tech Insights Over Time', fontweight='bold')
ax[0].grid(True, linestyle='-', alpha=0.8, color='grey')
ax[0].legend(loc='upper right', fontsize=10, frameon=False)

ax[1].plot(years, technology_index, marker='D', linestyle='--', linewidth=2.5, color='slategrey', label='Tech')
ax[1].plot(years, environment_index, marker='x', linestyle='-.', linewidth=2.5, color='darkolivegreen', label='Enviro')
ax[1].plot(years, medicine_index, marker='*', linestyle=':', linewidth=2.5, color='crimson', label='Med')
ax[1].plot(years, history_index, marker='v', linestyle='-', linewidth=2.5, color='purple', label='Hist')
ax[1].plot(years, physics_index, marker='o', linestyle='--', linewidth=2.5, color='darkcyan', label='Phys')
ax[1].plot(years, mathematics_index, marker='s', linestyle='-.', linewidth=2.5, color='coral', label='Math')
ax[1].plot(years, artificial_intelligence_index, marker='p', linestyle='-', linewidth=2.5, color='blueviolet', label='AI')
ax[1].plot(years, robotics_index, marker='h', linestyle=':', linewidth=2.5, color='sienna', label='Robotics')

ax[1].set_xlabel('Year')
ax[1].set_ylabel('Knowledge Index')
ax[1].set_title('Growth in Different Knowledge Areas (2000-2030)', fontweight='bold')
ax[1].grid(False)
ax[1].legend(title='Fields', loc='upper right', fontsize=9, frameon=True)

ax[1].annotate('Breakthrough', xy=(2025, technology_index[25]), xytext=(2018, 80),
               arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=9)
ax[1].annotate('Peak', xy=(2015, medicine_index[15]), xytext=(2008, 65),
               arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=9)

plt.tight_layout()
plt.show()