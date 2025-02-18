import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

modules = [
    "Command Center", "Habitat Module", "Research Lab", 
    "Satellite Uplink", "Rover Operations", "Power Plant"
]

communication_links = [
    ("Rover Operations", "Habitat Module"),
    ("Command Center", "Power Plant"),
    ("Research Lab", "Command Center"),
    ("Satellite Uplink", "Research Lab"),
    ("Habitat Module", "Rover Operations"),
    ("Power Plant", "Satellite Uplink"),
    ("Command Center", "Rover Operations"),
    ("Habitat Module", "Power Plant")
]

G = nx.DiGraph()
G.add_nodes_from(modules)
G.add_edges_from(communication_links)

pos = nx.spring_layout(G, seed=42)

# New color set for the modules
module_colors = {
    "Command Center": "tomato", 
    "Habitat Module": "lightsteelblue", 
    "Research Lab": "peachpuff",
    "Satellite Uplink": "mediumseagreen", 
    "Rover Operations": "cornflowerblue", 
    "Power Plant": "gold"
}
node_colors = [module_colors[module] for module in G.nodes]

edge_labels = {
    ("Rover Operations", "Habitat Module"): "Energy Share",
    ("Command Center", "Power Plant"): "Command",
    ("Research Lab", "Command Center"): "Research Data",
    ("Satellite Uplink", "Research Lab"): "Link Data",
    ("Habitat Module", "Rover Operations"): "Logistics",
    ("Power Plant", "Satellite Uplink"): "Sensor Info",
    ("Command Center", "Rover Operations"): "Tasks",
    ("Habitat Module", "Power Plant"): "Maintenance"
}

communication_quality = [6, 9, 8, 7, 5, 8, 4, 6]

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

axs[0].set_title("Mission to Mars:\nCommunication Network of the Mars Base", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color=node_colors, edgecolors='black', ax=axs[0])
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2, ax=axs[0])
nx.draw_networkx_labels(G, pos, font_size=10, font_family="serif", font_weight='bold', ax=axs[0])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', font_size=8, label_pos=0.3, ax=axs[0])
axs[0].legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=module)
             for module, color in module_colors.items()],
    title='Mars Base Modules',
    loc='upper left'
)
axs[0].axis('off')

axs[1].barh(modules, communication_quality[:len(modules)], color=[module_colors[module] for module in modules])
axs[1].set_title("Communication Quality Metrics", fontsize=12, fontweight='bold')
axs[1].set_xlabel("Quality Score")
axs[1].set_xlim(0, max(communication_quality) + 2)
axs[1].invert_yaxis()
axs[1].grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()