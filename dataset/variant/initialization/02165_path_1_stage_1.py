import matplotlib.pyplot as plt
import numpy as np

# Years of interest
years = np.arange(2020, 2031)

# Number of space tourists each year (in thousands)
space_tourists = np.array([0.5, 1.2, 2.5, 5.0, 8.5, 12.0, 15.0, 18.5, 22.0, 28.5, 35.0])

# Revenue from space tourism (in millions)
revenue_per_tourist = 1.0
space_revenue = space_tourists * revenue_per_tourist * (1.0 + np.array([0.1, 0.15, 0.2, 0.18, 0.25, 0.22, 0.3, 0.28, 0.35, 0.33, 0.4]))

# Sorting the revenue data and rearranging other data accordingly
sorted_indices = np.argsort(space_revenue)
sorted_years = years[sorted_indices]
sorted_space_tourists = space_tourists[sorted_indices]
sorted_space_revenue = space_revenue[sorted_indices]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Plotting the sorted bar chart for revenue data
ax.bar(sorted_years, sorted_space_revenue, color='lightblue', alpha=0.6, label='Revenue ($M)', width=0.5)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Revenue (in millions)", fontsize=12, color='lightblue')
ax.tick_params(axis='y', labelcolor='lightblue')

# Annotate significant milestones (re-sorted according to revenue)
milestones = {2021: "1K Tourists Achieved", 2023: "Launch of Space Hotel I", 2026: "Commercial Flights Double", 2029: "30K Tourists Milestone"}
for year, label in milestones.items():
    idx = np.where(sorted_years == year)[0]
    if idx.size > 0:
        ax.annotate(label,
                    (sorted_years[idx[0]], sorted_space_revenue[idx[0]]),
                    textcoords="offset points",
                    xytext=(0, 15),
                    ha='center',
                    fontsize=9,
                    arrowprops=dict(arrowstyle='->', color='gray'))

# Title with multi-line
plt.title("Sorted Revenue from Space Tourism\n(2020 to 2030)", fontsize=16, fontweight='bold', pad=20)

# Customizing the grid and vertical lines for milestones
ax.grid(True, linestyle='--', alpha=0.7)

for year in milestones.keys():
    if year in sorted_years:
        ax.axvline(year, color='blue', linestyle='--', linewidth=1)

# Ensuring clarity in ticks
ax.set_xticks(sorted_years)
ax.set_yticks(np.arange(0, max(sorted_space_revenue) + 5, 5))

# Automatic layout adjustment
fig.tight_layout()

# Display the chart
plt.show()