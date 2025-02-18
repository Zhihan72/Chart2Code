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

# Create the plot
plt.figure(figsize=(8, 8))
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color=node_colors, edgecolors='black')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='gray', width=2)

plt.axis('off')
plt.tight_layout()
plt.show()