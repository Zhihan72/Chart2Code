import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The year is 2045, and the world has transitioned to relying almost exclusively on renewable energy sources.
# Various nations have been tracking their month-to-month growth in solar energy production.
# The data below reflects the growth percentage of solar energy production over a year for different countries.

# Data: Monthly growth (in percentage) of solar energy production for different countries
country_labels = ['USA', 'China', 'India', 'Germany', 'Japan']
growth_usa = [3.1, 2.8, 3.6, 4.0, 5.2, 3.8, 4.1, 4.7, 5.0, 4.5, 3.9, 4.3]
growth_china = [4.5, 4.2, 4.8, 5.0, 5.3, 4.9, 5.1, 5.4, 5.7, 5.8, 5.2, 5.0]
growth_india = [3.5, 3.6, 3.8, 4.1, 3.9, 4.0, 3.7, 4.2, 4.5, 4.3, 3.4, 3.9]
growth_germany = [2.8, 2.9, 3.1, 3.3, 4.0, 3.5, 3.8, 3.6, 3.7, 3.9, 4.1, 3.8]
growth_japan = [4.2, 4.1, 4.3, 4.6, 4.9, 4.8, 5.0, 4.5, 5.1, 4.8, 4.2, 4.7]

# Combining all growth data into a single dataset
growth_combined = growth_usa + growth_china + growth_india + growth_germany + growth_japan

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Create a histogram
n, bins, patches = ax.hist(growth_combined, bins=np.arange(2.5, 6.5, 0.5), edgecolor='black', color='orange', alpha=0.7, rwidth=0.85)

# Titles and labels
ax.set_title('Rays of Progress:\nAnnual Solar Energy Growth Across Leading Nations (2045)', fontsize=16, fontweight='bold')
ax.set_xlabel('Monthly Growth Percentage', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Adding a legend
legend_labels = country_labels
ax.legend(legend_labels, title='Countries', loc='upper right', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)

# Adding annotations for each bar
for count, rect in zip(n, patches):
    height = rect.get_height()
    ax.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=10)

# Adjust layout
plt.xticks(np.arange(2.5, 6.5, 0.5))
plt.tight_layout()

# Display the plot
plt.show()