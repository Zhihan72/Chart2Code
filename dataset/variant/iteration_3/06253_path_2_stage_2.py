import matplotlib.pyplot as plt
import networkx as nx

modules = [
    "Command Center", "Habitat Module", "Research Lab", 
    "Satellite Uplink", "Rover Operations", "Power Plant"
]

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

G = nx.DiGraph()
G.add_nodes_from(modules)
G.add_edges_from(communication_links)

pos = nx.spring_layout(G, seed=42)

module_colors = {
    "Command Center": "skyblue", 
    "Habitat Module": "lightgreen", 
    "Research Lab": "lightyellow",
    "Satellite Uplink": "lightcoral", 
    "Rover Operations": "lightpink", 
    "Power Plant": "lightgray"
}
node_colors = [module_colors[module] for module in G.nodes]

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

# Create the plot
plt.figure(figsize=(8, 8))
plt.title("Mission to Mars:\nCommunication Network of the Mars Base", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="serif", font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', font_size=8, label_pos=0.3)

plt.legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=module)
             for module, color in module_colors.items()],
    title='Mars Base Modules',
    loc='upper left'
)
plt.axis('off')

plt.tight_layout()
plt.show()