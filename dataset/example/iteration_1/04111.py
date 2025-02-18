import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the distribution of various types of cuisines in top urban areas during a gastronomic festival

# Define the cities and the types of cuisines
cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
cuisines = ['Italian', 'Chinese', 'Indian', 'Mexican', 'French']

# Data: The counts of participating restaurants showcasing each type of cuisine in different cities
data = np.array([
    [120, 90, 60, 50, 75],  # New York
    [100, 110, 95, 70, 80],  # London
    [85, 95, 110, 60, 90],  # Tokyo
    [90, 85, 70, 65, 100],  # Paris
    [80, 75, 60, 55, 95]   # Sydney
])

# Bar width
bar_width = 0.15

# Positions of the bars on the x-axis
r1 = np.arange(len(cities))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

# Create the bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each cuisine type, placing bars next to each other in each city
bar1 = ax.bar(r1, data[:, 0], color='red', width=bar_width, edgecolor='grey', label=cuisines[0])
bar2 = ax.bar(r2, data[:, 1], color='blue', width=bar_width, edgecolor='grey', label=cuisines[1])
bar3 = ax.bar(r3, data[:, 2], color='green', width=bar_width, edgecolor='grey', label=cuisines[2])
bar4 = ax.bar(r4, data[:, 3], color='orange', width=bar_width, edgecolor='grey', label=cuisines[3])
bar5 = ax.bar(r5, data[:, 4], color='purple', width=bar_width, edgecolor='grey', label=cuisines[4])

# Labeling the axes and setting the title
ax.set_xlabel('Cities', fontweight='bold', fontsize=12)
ax.set_ylabel('Number of Restaurants', fontweight='bold', fontsize=12)
ax.set_title('Gastronomic Festival 2023\nDistribution of Cuisines in Top Urban Areas', fontweight='bold', fontsize=14, pad=20)

# Customizing the x-axis ticks
ax.set_xticks([r + 2 * bar_width for r in range(len(cities))])
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)

# Adding the legend
ax.legend(title='Cuisine Types', loc='upper right', fontsize=10, edgecolor='grey')

# Adding grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Adding data labels to each bar
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height - 5, f'{int(height)}', ha='center', va='bottom', color='white', fontweight='bold')

# Add labels for each bar
add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)
add_labels(bar5)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()