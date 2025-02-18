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

pos = nx.shell_layout(G)

module_colors = {
    "Command Center": "orange",
    "Habitat Module": "purple",
    "Research Lab": "red",
    "Satellite Uplink": "blue",
    "Rover Operations": "green",
    "Power Plant": "brown"
}
node_colors = [module_colors[module] for module in G.nodes]

plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=node_colors, edgecolors='white')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='black', width=1, style='dashed')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

plt.grid(True)
plt.box(on=True)
plt.legend(["Modules & Communication Links"], loc='lower left')
plt.tight_layout()
plt.show()