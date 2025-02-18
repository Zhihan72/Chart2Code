import matplotlib.pyplot as plt
import numpy as np

# Data
happiness_score = np.array([5.0, 6.2, 6.5, 6.0, 7.0, 8.2, 7.5, 7.8, 9.0, 8.5, 7.0, 6.8, 8.0, 8.8, 9.2, 5.5])
sleep_hours = np.array([6, 7, 8, 7, 9, 10, 8, 9, 10, 8, 7, 6, 9, 10, 9, 7])

fig, ax = plt.subplots(figsize=(7, 6))

# Scatter plot for Happiness vs. Sleep Hours
ax.scatter(sleep_hours, happiness_score, color='green', s=80, edgecolor='gray', alpha=0.6, marker='x')
ax.grid(True, linestyle='-', alpha=0.9)
ax.set_title('Happiness vs. Sleep Hours', fontsize=14)
ax.set_xlabel('Sleep Hours')
ax.set_ylabel('Happiness Score')

fig.tight_layout(rect=[0.03, 0.03, 1, 0.92])
fig.suptitle('Effects on Happiness Score', fontsize=16, weight='bold')
plt.show()