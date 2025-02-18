import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define modules (nodes)
modules = [
    "Command Center", "Habitat Module", "Research Lab", 
    "Satellite Uplink", "Rover Operations", "Power Plant"
]

# Define the communication channels (directed edges)
communication_links = [
    ("Command Center", "Habitat Module"),
    ("Command Center", "Research Lab"),
    ("Command Center", "Satellite Uplink"),
    ("Habitat Module", "Command Center"),
    ("Research Lab", "Satellite Uplink"),
    ("Satellite Uplink", "Rover Operations"),
    ("Rover Operations", "Power Plant"),
    ("Power Plant", "Habitat Module")
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(modules)
G.add_edges_from(communication_links)

# Position nodes using a spring layout
pos = nx.spring_layout(G, seed=42)

# Node colors based on module type
module_colors = {
    "Command Center": "skyblue", 
    "Habitat Module": "lightgreen", 
    "Research Lab": "lightyellow",
    "Satellite Uplink": "lightcoral", 
    "Rover Operations": "lightpink", 
    "Power Plant": "lightgray"
}
node_colors = [module_colors[module] for module in G.nodes]

# Edge labels with direction descriptions
edge_labels = {
    ("Command Center", "Habitat Module"): "Status Updates",
    ("Command Center", "Research Lab"): "Research Coordination",
    ("Command Center", "Satellite Uplink"): "Data Transfer",
    ("Habitat Module", "Command Center"): "Reports",
    ("Research Lab", "Satellite Uplink"): "Findings",
    ("Satellite Uplink", "Rover Operations"): "Remote Commands",
    ("Rover Operations", "Power Plant"): "Energy Needs",
    ("Power Plant", "Habitat Module"): "Power Levels"
}

# Communication quality metrics for additional subplot - sorted in descending order
communication_quality = [8, 6, 7, 5, 9, 4,]
sorted_indices = np.argsort(communication_quality)[::-1]
sorted_modules = [modules[i] for i in sorted_indices]
sorted_qualities = [communication_quality[i] for i in sorted_indices]

# Create the plot with a grid layout
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Original network plot
axs[0].set_title("Mission to Mars:\nCommunication Network of the Mars Base", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color=node_colors, edgecolors='black', ax=axs[0])
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2, ax=axs[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_family="serif", font_weight='bold', ax=axs[0])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', font_size=8, label_pos=0.3, ax=axs[0])

# Adjusting the legend: Use colors that match the node colors for modules
axs[0].legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=module)
             for module, color in module_colors.items()],
    title='Mars Base Modules',
    loc='upper left'
)
axs[0].axis('off')

# Sorted Communication Quality Bar Chart
axs[1].barh(sorted_modules, sorted_qualities, color=[module_colors[module] for module in sorted_modules])
axs[1].set_title("Communication Quality Metrics", fontsize=12, fontweight='bold')
axs[1].set_xlabel("Quality Score")
axs[1].set_xlim(0, max(communication_quality) + 2)
axs[1].invert_yaxis()
axs[1].grid(axis='x', linestyle='--', alpha=0.6)

# Adjust layout for visualization
plt.tight_layout()
plt.show()
