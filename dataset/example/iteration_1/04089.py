import matplotlib.pyplot as plt
import numpy as np

# Defining the story:
# Space Exploration Initiatives from 2010 to 2020 by Different Agencies
# Agencies: NASA, SpaceX, ESA (European Space Agency) and ROSCOSMOS (Russian Space Agency)
# Key metrics: Number of Successful Missions

# Define the years
years = np.arange(2010, 2021)

# Number of successful missions by each agency
nasa_missions = np.array([15, 16, 15, 17, 16, 18, 19, 21, 18, 19, 22])
spacex_missions = np.array([1, 2, 3, 4, 5, 7, 10, 12, 14, 18, 22])
esa_missions = np.array([10, 11, 11, 13, 12, 14, 13, 16, 15, 14, 15])
roscosmos_missions = np.array([12, 13, 12, 14, 15, 14, 13, 14, 15, 16, 16])

# Stack the data for an area plot
data = np.vstack([nasa_missions, spacex_missions, esa_missions, roscosmos_missions])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 9))

# Create the stacked area plot
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
agencies = ['NASA', 'SpaceX', 'ESA', 'ROSCOSMOS']

ax.stackplot(years, data, labels=agencies, colors=colors, alpha=0.8)

# Annotations to highlight significant trends
ax.annotate('Rapid rise in SpaceX missions', xy=(2019, 14), xytext=(2016, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

# Adding title and labels
ax.set_title('Space Exploration Initiatives (2010-2020)\nNumber of Successful Missions by Agency', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Successful Missions', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 71, 10))
ax.set_ylim(0, 70)

# Adding legend
ax.legend(loc='upper left', fontsize=10, title='Agencies')

# Refined gridlines and axis
ax.grid(linestyle='--', alpha=0.5)

# Customizing the x-axis label rotation for clarity
plt.xticks(rotation=45, ha='right')

# Automatically adjust the layout
plt.tight_layout()

# Display the plot
plt.show()