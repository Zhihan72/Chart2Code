import matplotlib.pyplot as plt

pacific_temps = [22, 24, 23, 23, 25, 26, 27, 24, 26, 28, 29, 30, 27, 25, 24, 28, 26, 23, 22, 29]
atlantic_temps = [20, 21, 22, 23, 22, 24, 25, 26, 23, 22, 21, 20, 22, 23, 24, 26, 27, 25, 23, 22]
indian_temps = [25, 27, 28, 29, 27, 26, 25, 24, 26, 27, 28, 29, 30, 29, 28, 27, 26, 25, 26, 27]
arctic_temps = [1, 2, 3, 2, 1, 0, -1, 1, 2, 3, -1, -2, 1, 0, 2, 3, -1, 1, 2, 1]

temperature_data = [pacific_temps, atlantic_temps, indian_temps, arctic_temps]
ocean_names = ['Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean']

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#7B68EE', '#FF69B4', '#8A2BE2', '#32CD32']

box = ax.boxplot(temperature_data, vert=False, patch_artist=True, notch=True,
                 boxprops=dict(color='navy'),
                 whiskerprops=dict(color='navy', linestyle='--'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkred', linewidth=2),
                 flierprops=dict(marker='o', color='red', alpha=0.5),
                 meanline=True, showmeans=True, meanprops=dict(marker='D', markerfacecolor='black', markeredgecolor='black', markersize=7))

for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(ocean_names)
ax.set_title('Temperature Distribution Across Major Oceans', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()