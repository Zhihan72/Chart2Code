import numpy as np
import matplotlib.pyplot as plt

solar = np.array([
    5, 10, 15, 20, 30, 45, 60, 85, 110, 140,
    175, 215, 250, 295, 350, 410, 475, 550, 640, 740, 850
])
wind = np.array([
    10, 15, 20, 30, 45, 60, 75, 90, 110, 130,
    155, 185, 220, 265, 320, 380, 450, 530, 620, 720, 830
])

energy_data = np.vstack([solar, wind]).T  # Transposed for boxplot compatibility

fig, ax = plt.subplots(figsize=(14, 8))

# Creating a horizontal boxplot
ax.boxplot(energy_data, vert=False, patch_artist=True,
           boxprops=dict(facecolor='#00BFFF', color='#00BFFF'),
           whiskerprops=dict(color='#00BFFF'),
           capprops=dict(color='#00BFFF'),
           medianprops=dict(color='black'))

ax.set_title("Energy Usage Distribution in Renewable Sectors\n(2000-2020)", fontsize=18, fontweight='bold')
ax.set_xlabel('Usage (GW)', fontsize=14)
ax.set_yticklabels(['Solar', 'Wind'])  # Update y-ticks to reflect data categories

plt.tight_layout()
plt.show()