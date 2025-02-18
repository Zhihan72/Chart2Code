import matplotlib.pyplot as plt
import numpy as np

gravitational_anomalies = np.array([2.3, 3.1, 1.8, 2.9, 1.2, 4.5, 3.8, 3.5, 2.5, 3.0, 1.7, 4.1, 2.8, 4.2])
organic_signature_strengths = np.array([3.0, 2.5, 3.9, 2.8, 3.1, 3.7, 2.1, 3.5, 2.9, 3.2, 3.3, 3.6, 3.8, 3.0])
sensor_sizes = np.array([150, 200, 120, 160, 100, 190, 180, 110, 140, 130, 135, 170, 145, 185])

# Use a single color, e.g., 'blue', for all data points
consistent_color = 'blue'

plt.figure(figsize=(14, 8))
plt.scatter(gravitational_anomalies, organic_signature_strengths, s=sensor_sizes, c=consistent_color, 
            alpha=0.85, edgecolors=consistent_color, linewidth=2, zorder=2)
plt.gca().set_facecolor('#f0f8ff')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)

plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

plt.xticks(np.arange(1, 5.5, 0.5), labels=[])
plt.yticks(np.arange(2, 4.5, 0.5), labels=[])

plt.tight_layout()
plt.show()