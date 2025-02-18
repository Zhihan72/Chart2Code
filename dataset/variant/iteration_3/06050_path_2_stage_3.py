import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)
batteries = np.array([5, 10, 20, 35, 50, 70, 90, 115, 140, 170, 205, 240, 280, 320, 365, 410, 460, 510, 570, 630, 700])
pumped_hydro = np.array([50, 55, 63, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155])
thermal_storage = np.array([10, 12, 15, 18, 22, 27, 33, 40, 48, 57, 67, 78, 90, 103, 117, 132, 148, 165, 183, 202, 222])
flywheels = np.array([2, 3, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59])
supercapacitors = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 23, 26, 29, 33, 37, 42])

storage_data = np.vstack((batteries, pumped_hydro, thermal_storage, flywheels, supercapacitors))

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.stackplot(years, storage_data, labels=['Capsules', 'Hydro Pump', 'Temp Storage', 'Spinners', 'Mega Caps'],
              colors=['#32CD32', '#FF6347', '#FFCC00', '#8A2BE2', '#1E90FF'], alpha=0.85)

ax1.set_title('Future Patterns in Energy Reserves of Technotopia (2010-2030)', fontsize=14, fontweight='normal', pad=15)
ax1.set_xlabel('Timeline (Years)', fontsize=10)
ax1.set_ylabel('Storage Units (GWh)', fontsize=10)

ax1.legend(loc='upper right', fontsize=9, bbox_to_anchor=(0.95, 0.95), title='Energy Storage')

ax1.grid(True, linestyle='-.', alpha=0.5)
ax1.set_ylim(0, 800)

summary_text = "Capsules lead the charge in Technotopia's growth."
ax1.annotate(summary_text, xy=(2015, 500), xytext=(2019, 600),
             bbox=dict(boxstyle="round,pad=0.4", edgecolor='none', facecolor='lightblue'),
             arrowprops=dict(facecolor='blue', arrowstyle='->'),
             fontsize=9, ha='center')

plt.tight_layout()
plt.show()