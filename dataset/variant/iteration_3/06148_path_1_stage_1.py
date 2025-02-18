import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
years = np.arange(2000, 2021)
population = np.array([
    150, 154, 158, 165, 170, 176, 183, 190, 198, 210,
    222, 235, 248, 260, 272, 285, 297, 310, 325, 340, 355
])
businesses = np.array([
    50, 55, 60, 65, 68, 72, 80, 87, 93, 100,
    108, 117, 125, 133, 142, 150, 158, 165, 175, 185, 195
])
household_income = np.array([
    35, 36, 38, 40, 42, 45, 48, 50, 53, 56,
    60, 63, 67, 70, 74, 78, 82, 86, 90, 94, 98
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each data set
ax.plot(years, population, color='blue', linestyle='-', marker='o', linewidth=2)
ax.plot(years, businesses, color='green', linestyle='-', marker='s', linewidth=2)
ax.plot(years, household_income, color='red', linestyle='-', marker='^', linewidth=2)

# Remove legend
# ax.legend(loc='upper left', fontsize=12)

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