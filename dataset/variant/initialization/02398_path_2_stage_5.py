import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

features = [
    "Food Stall", "Restrooms", "Playground", "Amphitheater", 
    "Dog Park", "Walking Path", "Fountain", "Garden", "Picnic Area",
    "Lake", "Bike Rental", "Petting Zoo"
]

connections = [
    ("Food Stall", "Restrooms"),
    ("Restrooms", "Fountain"),
    ("Fountain", "Walking Path"),
    ("Walking Path", "Dog Park"),
    ("Dog Park", "Amphitheater"),
    ("Amphitheater", "Garden"),
    ("Garden", "Playground"),
    ("Playground", "Picnic Area"),
    ("Picnic Area", "Food Stall"),
    ("Lake", "Bike Rental"),
    ("Bike Rental", "Petting Zoo"),
    ("Petting Zoo", "Lake")
]

G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)
node_colors = ['#ff69b4', '#8b4513', '#9acd32', '#dda0dd', '#ff6347', 
               '#adff2f', '#ffeb3b', '#f4a460', '#1e90ff', '#00ced1', 
               '#7f00ff', '#4b0082']
node_sizes = [800, 850, 1200, 1050, 800, 1100, 900, 950, 1000, 1100, 1150, 1200]

visitor_interactions = np.array([
    [70, 75, 80, 85, 80, 75, 70],
    [40, 45, 50, 45, 40, 35, 30],
    [50, 60, 70, 60, 80, 90, 100],
    [100, 105, 110, 115, 120, 125, 130],
    [30, 35, 40, 45, 50, 55, 60],
    [90, 85, 80, 85, 90, 100, 105],
    [80, 85, 90, 85, 95, 80, 70],
    [25, 30, 35, 40, 30, 25, 20],
    [60, 65, 70, 75, 80, 85, 90],
    [55, 60, 65, 70, 75, 80, 85],
    [45, 50, 55, 60, 55, 50, 45],
    [32, 37, 42, 40, 45, 47, 43]
])

days = ["Wed", "Fri", "Tue", "Sun", "Mon", "Thu", "Sat"]

fig, axes = plt.subplots(2, 1, figsize=(12, 20))

nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, edge_color='gray', width=2.0, ax=axes[0], arrows=True)

axes[0].set_title('Extended Urban Park Feature Network', fontsize=14)

heatmap = axes[1].imshow(visitor_interactions, cmap='YlGnBu', aspect='auto')

axes[1].set_xticks(np.arange(len(days)))
axes[1].set_xticklabels(days)
axes[1].set_yticks(np.arange(len(features)))
axes[1].set_yticklabels(features)
axes[1].set_title('Extended Weekly Visitor Activity', fontsize=14)

plt.suptitle(
    'Analysis of Park Patterns: Expanded Insights on Visits and Structure',
    fontsize=16, y=0.95
)

plt.tight_layout(rect=[0, 0.03, 1, 0.93])
plt.show()