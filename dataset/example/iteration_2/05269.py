import matplotlib.pyplot as plt
import numpy as np

# Define a backstory:
# The chart is about the annual travel statistics from different continents, showcasing the total number of tourists to a country over a decade.
# This would help us understand the trends in global tourism from various regions over time.

# Define years
years = np.arange(2010, 2020)

# Mock data representing tourists from different continents (in millions)
north_america = np.array([3, 3.5, 4, 4.2, 4.8, 5, 5.5, 5.8, 6, 6.2])
south_america = np.array([1, 1.2, 1.4, 1.5, 1.7, 1.8, 2, 2.2, 2.4, 2.6])
europe = np.array([7, 7.5, 8, 8.5, 9, 9.2, 9.5, 10, 10.5, 11])
asia = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8, 8.3, 8.7, 9])
africa = np.array([0.5, 0.6, 0.7, 0.8, 1, 1.2, 1.3, 1.5, 1.7, 1.9])
oceania = np.array([0.3, 0.35, 0.4, 0.45, 0.48, 0.5, 0.55, 0.6, 0.65, 0.7])

# Combine data for area plot
tourism_data = np.vstack([north_america, south_america, europe, asia, africa, oceania])

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Colors for each continent
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Generate the stacked area plot
ax.stackplot(years, tourism_data, labels=['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania'], colors=colors, alpha=0.8)

# Add chart details
ax.set_title("Decade of Tourism: \nTourists to the Country by Continent (2010-2019)", fontsize=16, fontweight='bold', loc='left')
ax.set_xlabel('Year', fontsize=12, weight='bold')
ax.set_ylabel('Millions of Tourists', fontsize=12, weight='bold')
ax.legend(loc='upper left', title='Continents', fontsize=10, bbox_to_anchor=(1, 1), title_fontsize='13')

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 13, 1))
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Highlight significant year for a peak in tourism
peak_year = 2017
peak_value = np.sum(tourism_data[:, years == peak_year])
ax.axvline(x=peak_year, color='grey', linestyle='--', lw=1)
ax.annotate(f'Peak Tourism Year\nTotal: {peak_value} million', xy=(peak_year, peak_value), xytext=(peak_year+1, peak_value-2), 
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkred')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()