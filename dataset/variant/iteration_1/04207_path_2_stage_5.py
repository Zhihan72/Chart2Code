import matplotlib.pyplot as plt
import numpy as np

# Data for the horizontal bar chart
average_age_adulthood = np.array([18, 25, 14, 33, 120, 70])
average_years_education = np.array([12, 15, 6, 20, 80, 50])

# Shuffle the colors by reordering the data indices
shuffled_indices = np.array([2, 4, 0, 5, 1, 3])
shuffled_colors = average_years_education[shuffled_indices]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a horizontal bar chart
ax.barh(np.arange(len(average_age_adulthood)), average_age_adulthood, 
        color=plt.cm.plasma(shuffled_colors / max(shuffled_colors)), 
        edgecolor='black', alpha=0.8)

# Remove grid and borders
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Adjust x and y limits without ticks
ax.set_xlim(0, 130)
ax.set_ylim(-0.5, len(average_age_adulthood) - 0.5)
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

plt.tight_layout()
plt.show()