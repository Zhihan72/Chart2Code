import matplotlib.pyplot as plt
import numpy as np

retreats = ['Mars Valley', 'Jupiter Halo', 'Venus Outpost', 'Saturn Rings', 'Neptune Seas']

intellectual_diversity = np.array([80, 60, 70, 85, 55])
environmental_diversity = np.array([75, 50, 90, 65, 80])
creative_output = np.array([88, 65, 92, 78, 70])
attendees = np.array([120, 90, 150, 110, 95])

bubble_size = attendees / np.max(attendees) * 500

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(intellectual_diversity, environmental_diversity, creative_output, 
           s=bubble_size, c=creative_output, cmap='viridis', alpha=0.8)

ax.set_title('Galactic Writers\' Retreats:\nNavigating the Universe of Creativity', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Intellectual Diversity', fontsize=12, labelpad=10)
ax.set_ylabel('Environmental Diversity', fontsize=12, labelpad=10)
ax.set_zlabel('Creative Output', fontsize=12, labelpad=10)

for i, retreat in enumerate(retreats):
    ax.text(intellectual_diversity[i], environmental_diversity[i], creative_output[i],
            retreat, fontsize=10, ha='right')

plt.show()