import matplotlib.pyplot as plt
import numpy as np

# Updated species list
species = ['Oak', 'Pine', 'Maple', 'Redw', 'Willow', 'Seq']

# Updated data arrays
sunlight_hrs = np.array([4, 6, 5, 2, 9, 3])
prev = np.array([200, 250, 180, 220, 270, 320])

plt.figure(figsize=(12, 8))
plt.barh(species, sunlight_hrs, color=plt.cm.plasma(prev/max(prev)))

plt.title('Sunlight for Trees in Eldoria', fontsize=16, fontweight='bold')
plt.xlabel('Sunlight (Hr/Day)', fontsize=12, fontweight='bold')
plt.ylabel('Species', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()