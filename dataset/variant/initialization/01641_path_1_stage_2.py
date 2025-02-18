import matplotlib.pyplot as plt
import numpy as np

# Data: Art gallery visitors (in thousands) from 2010 to 2020
years = np.arange(2010, 2021)
gallery_visitors = {
    'New York': [950, 920, 970, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1400],
    'Paris': [750, 780, 760, 800, 850, 880, 910, 930, 950, 970, 1000],
    'Tokyo': [600, 620, 650, 670, 700, 730, 750, 770, 800, 830, 860],
    'London': [890, 870, 880, 920, 940, 960, 1000, 1020, 1040, 1060, 1100]
}

# Calculate cumulative visitors each year across remaining cities
cumulative_visitors = np.sum(list(gallery_visitors.values()), axis=0)

# Setup the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Colors for each city line
colors = ['#D2691E', '#8A2BE2', '#5F9EA0', '#006400']

# Plot data for each city with lines
marker_styles = ['s', 'D', 'x', '^']  # Square, Diamond, Cross, Triangle
line_styles = ['--', '-.', ':', '-']

for (city, visitors), color, marker, line_style in zip(gallery_visitors.items(), colors, marker_styles, line_styles):
    ax1.plot(years, visitors, linestyle=line_style, marker=marker, label=city, color=color, linewidth=2, markersize=8, alpha=0.9)
    
    # Annotate for key data points for each city
    midpoint_index = len(years) // 2
    key_points = [(years[0], visitors[0]), (years[midpoint_index], visitors[midpoint_index]), (years[-1], visitors[-1])]
    for (year, visitor) in key_points:
        ax1.annotate(f'{visitor}k', xy=(year, visitor), xytext=(5, -15 if visitor < max(visitors) else 5), 
                     textcoords='offset points', arrowprops=dict(arrowstyle='-|>', color=color), 
                     fontsize=10, color=color, ha='center')

# Plot cumulative visitors as an area plot
ax2 = ax1.twinx()
ax2.fill_between(years, 0, cumulative_visitors, color='slategray', alpha=0.3)
ax2.set_ylabel('Cumulative Visitors (in thousands)', fontsize=12)
ax2.spines['right'].set_color('darkred')  # Change color of the right side border
ax2.set_ylim(0, np.max(cumulative_visitors) + 500)

# Set titles and labels
ax1.set_title('Art Gallery Visitors Trend (2010-2020)\nPublic Engagement in Major Cities', 
              fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Visitors (in thousands)', fontsize=12)

# Add a legend with stylish title
ax1.legend(title='Top Cities', loc='upper left', fontsize=10, fancybox=True, shadow=True)

# Add grid with full lines
ax1.grid(True, which='major', axis='both', linestyle='-', linewidth=0.7, alpha=0.5)

# Ensure tight layout for readability
plt.tight_layout()

# Show the plot
plt.show()