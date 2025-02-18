import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
years = np.arange(2000, 2021)
population = np.array([
    152, 157, 159, 166, 172, 175, 182, 189, 199, 209,
    220, 236, 250, 259, 273, 286, 296, 311, 324, 339, 354
])
businesses = np.array([
    52, 54, 62, 67, 66, 70, 82, 88, 92, 102,
    109, 115, 130, 134, 141, 152, 156, 166, 178, 182, 194
])
household_income = np.array([
    34, 37, 39, 41, 41, 46, 49, 51, 54, 55,
    62, 61, 66, 72, 73, 79, 81, 87, 89, 95, 97
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each data set with a new set of colors
ax.plot(years, population, color='purple', linestyle='-', marker='o', linewidth=2)
ax.plot(years, businesses, color='orange', linestyle='-', marker='s', linewidth=2)
ax.plot(years, household_income, color='cyan', linestyle='-', marker='^', linewidth=2)

# Add grid
ax.grid(True, linestyle='--', alpha=0.6)

# Configure x-axis tick marks
ax.set_xticks(np.arange(2000, 2021, 2))

# Highlight significant milestones
milestones = [2005, 2010, 2015]
for year in milestones:
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)

# Ensure layout is not overlapping
plt.tight_layout()

# Display the plot
plt.show()