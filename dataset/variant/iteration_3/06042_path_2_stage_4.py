import matplotlib.pyplot as plt
import numpy as np

# Manually shuffled data arrays
sleep_hours = np.array([9, 6, 10, 7, 8, 5])
productivity_scores = np.array([85, 65, 90, 70, 80, 60])

fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar chart
ax.barh(sleep_hours, productivity_scores, color='skyblue', edgecolor='k')

ax.set_xlabel('Productivity Score (out of 100)', fontsize=12)
ax.set_ylabel('Hours of Sleep', fontsize=12)

plt.tight_layout()
plt.show()