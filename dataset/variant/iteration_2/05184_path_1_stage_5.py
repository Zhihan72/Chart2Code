import numpy as np
import matplotlib.pyplot as plt

sectors = ['AI', 'Cloud Computing', 'Cybersecurity', 'IoT']
total_revenues = np.array([63, 45, 118, 90])

# New set of colors
colors = ['#8A2BE2', '#5F9EA0', '#FF4500', '#7FFF00']

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(sectors, total_revenues, color=colors)

ax.set_xlabel('Industries', fontsize=14)
ax.set_ylabel('Revenue (Billion USD)', fontsize=14)
ax.set_title('Revenue Overview by Industry', fontsize=16, fontweight='bold')

ax.set_frame_on(False)  # Remove borders
plt.tight_layout()
plt.axis('off')  # Eliminate axes

plt.show()