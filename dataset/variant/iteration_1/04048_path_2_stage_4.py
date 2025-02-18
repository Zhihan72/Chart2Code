import matplotlib.pyplot as plt

# Data for nodes
nodes = {
    'Solar Power': 5,
    'Turbine Winds': 4,
    'Water Power': 3,
    'Earth Heat': 2,
    'Biofuel': 4,
    'Storage': 6,
    'Distribution': 7,
    'Smart Lines': 5
}

# Sorting nodes based on their values in descending order for the plot
sorted_nodes = dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))

plt.figure(figsize=(10, 6))

# Create a bar chart
plt.bar(sorted_nodes.keys(), sorted_nodes.values(), color=plt.cm.plasma([v / max(sorted_nodes.values()) for v in sorted_nodes.values()]))

plt.title('Renewable Energy Node Capacities', fontsize=14, fontweight='bold')
plt.xlabel('Energy Sources and Infrastructure', fontsize=12)
plt.ylabel('Capacity', fontsize=12)
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()