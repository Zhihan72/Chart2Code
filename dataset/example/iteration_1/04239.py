import matplotlib.pyplot as plt
import numpy as np

# Backstory: Migration patterns to cities have become a hot topic in recent years. We will visualize the number of people migrating from rural areas to cities across different continents from 2000 to 2020.

# Data preparation
years = np.arange(2000, 2021)
migration_africa = np.array([2, 3, 5, 8, 12, 14, 16, 18, 20, 23, 25, 28, 30, 32, 35, 39, 42, 45, 48, 52, 55])
migration_asia = np.array([5, 7, 10, 14, 18, 20, 24, 28, 35, 40, 45, 48, 54, 57, 60, 65, 70, 76, 80, 85, 90])
migration_europe = np.array([3, 4, 6, 10, 12, 13, 14, 15, 16, 18, 20, 22, 24, 25, 27, 28, 30, 32, 34, 36, 38])
migration_namerica = np.array([2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26])
migration_samerica = np.array([3, 5, 7, 10, 12, 15, 18, 21, 24, 28, 30, 33, 35, 37, 40, 42, 45, 48, 51, 54, 57])
migration_oceania = np.array([1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17])

# Stack the data for plotting
migration_data = np.vstack([migration_africa, migration_asia, migration_europe, migration_namerica, migration_samerica, migration_oceania])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Use stackplot to create the chart
ax.stackplot(years, migration_data, labels=['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania'], 
             colors=['#FFA07A', '#20B2AA', '#778899', '#DAA520', '#FF6347', '#4682B4'], alpha=0.8)

# Customize the chart with title and labels
ax.set_title('Global Urban Migration Patterns\n(2000-2020)', fontsize=16, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, weight='bold')
ax.set_ylabel('Number of Migrants (millions)', fontsize=12, weight='bold')

# Ensure x-axis labels are clearly readable
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=45)

# Position the legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Continents', fontsize=11)

# Improve layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()