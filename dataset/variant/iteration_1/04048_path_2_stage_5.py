import matplotlib.pyplot as plt

# Data for nodes with shuffled content
nodes = {
    'Solar Power': 3,
    'Turbine Winds': 6,
    'Water Power': 5,
    'Earth Heat': 4,
    'Biofuel': 2,
    'Storage': 7,
    'Distribution': 4,
    'Smart Lines': 5
}

# Sorting nodes based on their values in descending order for the plot
sorted_nodes = dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))

plt.figure(figsize=(10, 6))
plt.bar(sorted_nodes.keys(), sorted_nodes.values(), color=plt.cm.plasma([v / max(sorted_nodes.values()) for v in sorted_nodes.values()]))

plt.title('Renewable Energy Node Capacities', fontsize=14, fontweight='bold')
plt.xlabel('Energy Sources and Infrastructure', fontsize=12)
plt.ylabel('Capacity', fontsize=12)
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()