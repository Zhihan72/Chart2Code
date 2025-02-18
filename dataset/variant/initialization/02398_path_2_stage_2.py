import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

features = [
    "Playground", "Picnic Area", "Fountain", "Walking Path", 
    "Dog Park", "Garden", "Amphitheater", "Restrooms", "Food Stall"
]

connections = [
    ("Playground", "Picnic Area"),
    ("Picnic Area", "Garden"),
    ("Garden", "Fountain"),
    ("Fountain", "Walking Path"),
    ("Walking Path", "Amphitheater"),
    ("Amphitheater", "Restrooms"),
    ("Restrooms", "Food Stall"),
    ("Food Stall", "Dog Park"),
    ("Dog Park", "Playground")
]

# Change graph to directed graph
G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)

node_colors = ['#9acd32', '#ff6347', '#1e90ff', '#ffeb3b', '#f4a460', '#adff2f', '#dda0dd', '#8b4513', '#ff69b4']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800]

visitor_interactions = np.array([
    [50, 60, 70, 60, 80, 90, 100],
    [80, 85, 90, 85, 95, 80, 70],
    [30, 35, 40, 45, 50, 55, 60],
    [90, 85, 80, 85, 90, 100, 105],
    [25, 30, 35, 40, 30, 25, 20],
    [60, 65, 70, 75, 80, 85, 90],
    [100, 105, 110, 115, 120, 125, 130],
    [40, 45, 50, 45, 40, 35, 30],
    [70, 75, 80, 85, 80, 75, 70]
])

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Maintain the subplot configuration as 2 rows and 1 column
fig, axes = plt.subplots(2, 1, figsize=(10, 18))

# Plot the directed graph on the first subplot
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, font_weight='bold', edge_color='gray', width=2.0, alpha=0.7, ax=axes[0], arrows=True)

axes[0].set_title('Directed Network of Urban Park Features', fontsize=14, fontweight='bold')

# Plot the heatmap on the second subplot
heatmap = axes[1].imshow(visitor_interactions, cmap='YlGnBu', aspect='auto')

axes[1].set_xticks(np.arange(len(days)))
axes[1].set_xticklabels(days)
axes[1].set_yticks(np.arange(len(features)))
axes[1].set_yticklabels(features)
axes[1].set_title('Visitor Interactions Over a Week', fontsize=14, fontweight='bold')

cbar = fig.colorbar(heatmap, ax=axes[1], orientation='vertical')
cbar.set_label('Number of Visitors', fontsize=12)

plt.suptitle(
    'Urban Park Analysis: Connectivity and Visitor Interaction\nEnhancing Visitor Experience Through Visual Insights',
    fontsize=16, fontweight='bold', y=1.02
)

for ax in axes:
    ax.set_xlabel('Day', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.label_outer()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()