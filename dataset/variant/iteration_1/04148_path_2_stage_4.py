import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
revenue = np.array([18.0, 3.9, 10.2, 24.0, 7.0, 32.5, 0.5, 45.0, 13.5, 2.1])

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(years, revenue, marker='o', linestyle='-', color='darkred', lw=2, markersize=8)

# Removing textual elements
ax.tick_params(axis='both', which='major', labelsize=12)
plt.xticks(np.arange(2013, 2023, step=1))
plt.tight_layout()
plt.show()