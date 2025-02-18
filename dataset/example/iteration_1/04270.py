import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the growth of different means of commuting in the city of Metrotopia over the span of 15 years (2005-2020).
# The categories include Car, Public Transport, Cycling, and Walking.

# Years from 2005 to 2020
years = np.arange(2005, 2021)

# Artificial data representing average daily commuters (in thousands)
car_commuters = np.array([50, 55, 58, 60, 62, 65, 66, 68, 70, 73, 75, 74, 73, 73, 74, 75])
public_transport_commuters = np.array([30, 32, 35, 37, 41, 45, 48, 52, 55, 57, 60, 63, 65, 68, 71, 74])
cycling_commuters = np.array([2, 3, 4, 5, 7, 9, 11, 14, 17, 19, 22, 25, 28, 30, 32, 35])
walking_commuters = np.array([10, 11, 12, 13, 14, 15, 15, 15, 15, 15, 14, 13, 12, 12, 12, 12])

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Create stacked area chart
ax.stackplot(years, car_commuters, public_transport_commuters, cycling_commuters, walking_commuters,
             labels=['Car', 'Public Transport', 'Cycling', 'Walking'],
             colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], alpha=0.8)

# Set title and labels
ax.set_title('Commuting Trends in Metrotopia (2005-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Average Daily Commuters (in thousands)', fontsize=14)
ax.set_xticks(years[::1])
ax.set_xticklabels(years, rotation=45, fontsize=10)
ax.set_yticks(np.arange(0, 160, 10))
ax.set_yticklabels(np.arange(0, 160, 10), fontsize=10)

# Adding a grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adding legend
ax.legend(loc='upper left', title='Mode of Commute', fontsize=10)

# Automatically adjust plot dimensions to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()