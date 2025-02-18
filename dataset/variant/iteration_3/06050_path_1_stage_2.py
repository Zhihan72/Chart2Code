import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

batteries_altered = np.array([10, 20, 35, 50, 70, 90, 115, 140, 170, 205, 240, 280, 320, 365, 410, 460, 510, 570, 630, 700, 5])
pumped_hydro_altered = np.array([55, 63, 50, 80, 85, 75, 70, 95, 100, 105, 120, 125, 115, 135, 130, 140, 145, 150, 155, 50, 110])
thermal_storage_altered = np.array([12, 15, 10, 27, 33, 18, 22, 48, 57, 67, 78, 103, 90, 132, 117, 148, 165, 183, 202, 222, 40])
flywheels_altered = np.array([3, 5, 8, 14, 17, 2, 11, 23, 26, 29, 32, 38, 35, 44, 41, 50, 47, 53, 56, 59, 20])

storage_data = np.vstack((batteries_altered, pumped_hydro_altered, thermal_storage_altered, flywheels_altered))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Use a single color for all data groups
single_color = '#FFD700'  # Gold color
ax1.stackplot(years, storage_data, labels=['Batteries', 'Pumped Hydro', 'Thermal Storage', 'Flywheels'], 
              colors=[single_color]*4, alpha=0.85)

ax1.set_title('Evolution of Renewable Energy Storage Capacities in Greenopolis (2010-2030)', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Storage Capacity (GWh)', fontsize=12)

ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title='Storage Types')

ax1.grid(True, linestyle='--', alpha=0.7)

ax1.set_ylim(0, 800)

summary_text = "Greenopolis has significantly increased its renewable energy storage capacity over the years, " \
               "with batteries seeing the most substantial growth."

ax1.annotate(summary_text, xy=(2011, 600), xytext=(2015, 700),
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightgrey'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, ha='center')

plt.tight_layout()

plt.show()