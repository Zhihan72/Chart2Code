import matplotlib.pyplot as plt
import numpy as np

# Data for years and brands
years = np.arange(2020, 2026)
brands = ['Eco', 'Threads', 'Wear', 'Knits', 'Trend']

# Data arrays for different materials
organic_cotton = np.array([
    [5, 10, 15, 20, 25, 30],
    [4, 8, 12, 16, 20, 24],
    [6, 11, 17, 23, 29, 35],
    [5, 9, 14, 18, 23, 28],
    [3, 7, 11, 15, 19, 23]
])

recycled_polyester = np.array([
    [3, 5, 8, 12, 15, 19],
    [4, 7, 11, 14, 18, 21],
    [2, 6, 9, 13, 17, 22],
    [3, 5, 9, 13, 16, 20],
    [4, 6, 10, 14, 18, 22]
])

hemp = np.array([
    [2, 4, 6, 8, 10, 12],
    [1, 3, 5, 7, 9, 11],
    [3, 5, 8, 11, 14, 17],
    [2, 4, 7, 10, 13, 15],
    [1, 2, 4, 6, 8, 10]
])

# Creating a plot
fig, ax = plt.subplots(figsize=(14, 9))

# Bar properties
bar_width = 0.25
x_indexes = np.arange(len(years))
offset = bar_width * 3

# New style elements: colors and linestyle
colors = ['#FF33A1', '#33FFA5', '#A533FF']

# Plotting the bars with different markers
for i, brand in enumerate(brands):
    ax.bar(x_indexes + i * offset, organic_cotton[i], width=bar_width, label='Organic Cotton' if i == 0 else "", color=colors[0], alpha=0.8, edgecolor='black', linestyle='dotted')
    ax.bar(x_indexes + i * offset + bar_width, recycled_polyester[i], width=bar_width, label='Recycled Polyester' if i == 0 else "", color=colors[1], alpha=0.8, edgecolor='black', linestyle='dashdot')
    ax.bar(x_indexes + i * offset + bar_width * 2, hemp[i], width=bar_width, label='Hemp' if i == 0 else "", color=colors[2], alpha=0.8, edgecolor='black', linestyle='solid')
    
# Set labels and title with some styling
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Usage (in Tons)', fontsize=14, fontweight='bold')
ax.set_title('Eco Materials Adoption Trend (2020-2025)', fontsize=16, fontweight='bold', pad=25)

# Adjusted x-ticks for clarity
ax.set_xticks(x_indexes + 1.5 * bar_width)
ax.set_xticklabels(years)

# Legend settings
handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))
ax.legend(unique_labels.values(), unique_labels.keys(), loc='best', fontsize=12, title='Materials', title_fontsize='14', shadow=True, fancybox=True)

# Grid with modified style
ax.grid(axis='y', linestyle='-.', linewidth=0.8, color='grey', alpha=0.6)

# Layout adjustment for better appearance
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Display the plot
plt.show()