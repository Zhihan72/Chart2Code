import matplotlib.pyplot as plt
import numpy as np

# Shuffled Data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_celsius = np.array([4, 19, 25, 21, 12, 24, 10, -2, 5, -5, 16, -1])  # Manually shuffled
precipitation_mm = np.array([50, 75, 90, 60, 70, 82, 45, 65, 40, 85, 70, 55])   # Manually shuffled

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, temperature_celsius, color='gray', marker='o', linestyle='-', linewidth=2, markersize=6)
ax1.tick_params(axis='y', labelcolor='gray', labelleft=False)  # Remove y-axis labels
ax1.set_ylim(-10, 30)

ax2 = ax1.twinx()
ax2.bar(months, precipitation_mm, color='gray', alpha=0.5)
ax2.tick_params(axis='y', labelcolor='gray', labelleft=False)  # Remove y-axis labels
ax2.set_ylim(0, 100)

plt.xticks([])  # Remove x-axis labels
plt.tight_layout()
plt.show()