import matplotlib.pyplot as plt
import numpy as np

# Data
happiness_score = np.array([5.0, 6.2, 6.5, 6.0, 7.0, 8.2, 7.5, 7.8, 9.0, 8.5, 7.0, 6.8, 8.0, 8.8, 9.2, 5.5])
sleep_hours = np.array([6, 7, 8, 7, 9, 10, 8, 9, 10, 8, 7, 6, 9, 10, 9, 7])
outdoor_hours = np.array([1, 2, 3, 2, 4, 5, 3, 4, 6, 5, 3, 2, 4, 5, 6, 2])

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot for Happiness vs. Sleep Hours
axs[0].scatter(sleep_hours, happiness_score, color='blue', s=100, edgecolor='black', alpha=0.7)
axs[0].grid(True, linestyle='--', alpha=0.6)

# Scatter plot for Happiness vs. Outdoor Hours
axs[1].scatter(outdoor_hours, happiness_score, color='red', s=100, edgecolor='black', alpha=0.7)
axs[1].grid(True, linestyle='--', alpha=0.6)

fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()