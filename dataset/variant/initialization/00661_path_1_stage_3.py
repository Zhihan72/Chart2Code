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
hydro = np.array([
    30, 35, 40, 45, 50, 55, 60, 70, 80, 95, 
    115, 135, 160, 190, 225, 265, 310, 360, 420, 490, 570
])

energy_data = [solar, wind, hydro]
labels = ['Solar', 'Wind', 'Hydro']

fig, ax = plt.subplots(figsize=(14, 8))

ax.boxplot(energy_data, vert=False, patch_artist=True,
           labels=labels, boxprops=dict(facecolor='#FFD700', alpha=0.75))

ax.set_title("Renewable Energy Generation Over Time", fontsize=18, fontweight='bold')
ax.set_xlabel('Adoption (GW)', fontsize=14)

ax.grid(linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()