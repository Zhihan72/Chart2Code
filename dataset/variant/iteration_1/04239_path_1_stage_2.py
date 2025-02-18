import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2000, 2021)
migration_africa = np.array([2, 3, 5, 8, 12, 14, 16, 18, 20, 23, 25, 28, 30, 32, 35, 39, 42, 45, 48, 52, 55])
migration_asia = np.array([5, 7, 10, 14, 18, 20, 24, 28, 35, 40, 45, 48, 54, 57, 60, 65, 70, 76, 80, 85, 90])
migration_europe = np.array([3, 4, 6, 10, 12, 13, 14, 15, 16, 18, 20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
migration_namerica = np.array([2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26])
migration_samerica = np.array([3, 5, 7, 10, 12, 15, 18, 21, 24, 28, 30, 33, 35, 37, 40, 42, 45, 48, 51, 54, 57])

# Stack the data for plotting
migration_data = np.vstack([migration_africa, migration_asia, migration_europe, migration_namerica, migration_samerica])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Use stackplot to create the chart without labels and titles
ax.stackplot(years, migration_data, colors=['#FFA07A', '#20B2AA', '#778899', '#DAA520', '#FF6347'], alpha=0.8)

# Remove axis labels and title
ax.set_xticks([])
ax.set_yticks([])

# Remove legend
ax.legend().remove()

# Show the plot
plt.show()