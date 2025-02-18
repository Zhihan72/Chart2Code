import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Over the last decade (2012-2022), the Sanctuary Wildlife Reserve has been monitoring the bird population
# of four different species. The aim is to observe how these species thrive throughout the years in the reserve.
# The data reflects the changes in the population of these species over time.

# Define the years for the study
years = np.arange(2012, 2023)

# Artificial data for bird population (in thousands)
sparrows = np.array([15, 14, 13, 12, 14, 15, 16, 17, 19, 21, 23])
robins = np.array([10, 12, 11, 10, 10, 12, 14, 15, 16, 17, 19])
blue_jays = np.array([5, 6, 7, 8, 8, 9, 10, 10, 12, 12, 14])
eagles = np.array([2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7])

# Stack the data
data = np.vstack([sparrows, robins, blue_jays, eagles])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(years, data, labels=['Sparrows', 'Robins', 'Blue Jays', 'Eagles'],
             colors=['#FFD700', '#FFA07A', '#87CEFA', '#98FB98'], alpha=0.8)

# Add title and labels
ax.set_title('Bird Population Trends at Sanctuary Wildlife Reserve (2012-2022)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Population (in thousands)', fontsize=14)

# Fine-tune legend appearance and placement
ax.legend(loc='upper left', fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Highlight significant milestones
milestones = {
    2014: 'Peak in Sparrow Population',
    2018: 'Introduction of New Feeding Programs',
    2022: 'Initiation of Eagle Conservation'
}

for year, event in milestones.items():
    total_population = sparrows[year-2012] + robins[year-2012] + blue_jays[year-2012] + eagles[year-2012]
    ax.annotate(event, xy=(year, total_population/2),
                xytext=(year, total_population/2 + 10),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, ha='center', backgroundcolor='white')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()