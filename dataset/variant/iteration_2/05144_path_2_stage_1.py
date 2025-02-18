import matplotlib.pyplot as plt
import numpy as np

# Define the data for the box plot
solar_energy = [50, 55, 60, 65, 70, 72, 74, 76, 78, 80, 85]
wind_energy = [45, 50, 55, 60, 62, 64, 66, 68, 70, 75, 76]
hydroelectric_energy = [40, 42, 45, 47, 50, 53, 55, 57, 60, 64, 68]
geothermal_energy = [30, 32, 34, 36, 37, 40, 42, 44, 45, 48, 50]

data = [solar_energy, wind_energy, hydroelectric_energy, geothermal_energy]
energy_sources = ['Helios Power', 'Breeze Units', 'Water Kinetic', 'Earth Heat']

fig, ax = plt.subplots(figsize=(12, 8))

boxplot = ax.boxplot(data, vert=True, patch_artist=True, notch=True,
                    boxprops=dict(facecolor='skyblue', color='blue'),
                    whiskerprops=dict(color='blue'),
                    capprops=dict(color='blue'),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none'))

colors = ['#FFD700', '#90EE90', '#1E90FF', '#FF6347']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

plt.title("Energy Output by Source\nDecadal Comparison (2010-2020)", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Types of Power", fontsize=12)
plt.ylabel("Annual Output (Gigawatts)", fontsize=12)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.setp(boxplot['whiskers'], color='black', linestyle='-', linewidth=1.5)
plt.setp(boxplot['caps'], color='black', linewidth=1.5)
plt.setp(boxplot['medians'], color='red', linewidth=2)

overall_mean = np.mean(solar_energy + wind_energy + hydroelectric_energy + geothermal_energy)
ax.axhline(overall_mean, color='green', linestyle='--', linewidth=1.5, label='Overall Mean Output')

ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()