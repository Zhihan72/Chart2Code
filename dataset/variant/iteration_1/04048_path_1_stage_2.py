import matplotlib.pyplot as plt

# Define nodes with altered weights
nodes = {
    'Solar Panels': 3,
    'Wind Turbines': 6,
    'Hydropower': 2,
    'Geothermal': 4,
    'Biomass': 5,
    'Energy Storage': 7,
    'Grid Distribution': 3,
    'Smart Grids': 6
}

# Sort nodes by weights in descending order
sorted_nodes = sorted(nodes.items(), key=lambda item: item[1], reverse=True)

# Split into two lists: labels and values
labels, values = zip(*sorted_nodes)

# Create the bar chart
plt.figure(figsize=(12, 8))
plt.bar(labels, values, color=plt.cm.viridis([val / max(values) for val in values]))

# Add labels and title
plt.xlabel('Components')
plt.ylabel('Importance')
plt.title('Sorted Importance of Renewable Energy Components', fontsize=16, fontweight='bold')

# Add values on top of bars
for i, v in enumerate(values):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')

# Rotate x labels for better readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()