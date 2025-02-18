import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 11)
sales = np.array([60, 75, 90, 120, 130, 160, 170, 150, 135, 125])

shuffled_satisfaction = np.array([9, 7.5, 8.5, 8, 9, 7, 9.5, 8, 7.5, 6])

plt.figure(figsize=(14, 9))
plt.barh(weeks, sales, color=plt.cm.viridis(shuffled_satisfaction / max(shuffled_satisfaction)), edgecolor='black')

# Removing the textual elements: title, axis labels, and group labels.
plt.tight_layout()
plt.show()