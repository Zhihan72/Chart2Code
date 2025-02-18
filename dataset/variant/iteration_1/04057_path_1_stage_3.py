import matplotlib.pyplot as plt
import numpy as np

# Data
happiness_score = np.array([5.0, 6.2, 6.5, 6.0, 7.0, 8.2, 7.5, 7.8, 9.0, 8.5, 7.0, 6.8, 8.0, 8.8, 9.2, 5.5])
sleep_hours = np.array([6, 7, 8, 7, 9, 10, 8, 9, 10, 8, 7, 6, 9, 10, 9, 7])
outdoor_hours = np.array([1, 2, 3, 2, 4, 5, 3, 4, 6, 5, 3, 2, 4, 5, 6, 2])

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot for Happiness vs. Sleep Hours
axs[0].scatter(sleep_hours, happiness_score, color='green', s=80, edgecolor='gray', alpha=0.6, marker='x')
axs[0].grid(True, linestyle='-', alpha=0.9)
axs[0].set_title('Happiness vs. Sleep Hours', fontsize=14)
axs[0].set_xlabel('Sleep Hours')
axs[0].set_ylabel('Happiness Score')

# Scatter plot for Happiness vs. Outdoor Hours
axs[1].scatter(outdoor_hours, happiness_score, color='purple', s=120, edgecolor='yellow', alpha=0.8, marker='*')
axs[1].grid(False)
axs[1].set_title('Happiness vs. Outdoor Hours', fontsize=14)
axs[1].set_xlabel('Outdoor Hours')

fig.tight_layout(rect=[0.03, 0.03, 1, 0.92])
fig.suptitle('Effects on Happiness Score', fontsize=16, weight='bold')
plt.show()