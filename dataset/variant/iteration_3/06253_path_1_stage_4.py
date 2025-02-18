import matplotlib.pyplot as plt
import networkx as nx

modules = [
    "Cmd Ctr", "Habitat", "Lab", 
    "Uplink", "ROps", "Power"
]

communication_links = [
    ("ROps", "Habitat"),
    ("Cmd Ctr", "Power"),
    ("Lab", "Cmd Ctr"),
    ("Uplink", "Lab"),
    ("Habitat", "ROps"),
    ("Power", "Uplink"),
    ("Cmd Ctr", "ROps"),
    ("Habitat", "Power")
]

G = nx.Graph()  # Changed DiGraph to Graph for undirected
G.add_nodes_from(modules)
G.add_edges_from(communication_links)

pos = nx.spring_layout(G, seed=42)

module_colors = {
    "Cmd Ctr": "tomato", 
    "Habitat": "lightsteelblue", 
    "Lab": "peachpuff",
    "Uplink": "mediumseagreen", 
    "ROps": "cornflowerblue", 
    "Power": "gold"
}
node_colors = [module_colors[module] for module in G.nodes]

edge_labels = {
    ("ROps", "Habitat"): "Energy",
    ("Cmd Ctr", "Power"): "Cmd",
    ("Lab", "Cmd Ctr"): "Research",
    ("Uplink", "Lab"): "Data",
    ("Habitat", "ROps"): "Logistics",
    ("Power", "Uplink"): "Info",
    ("Cmd Ctr", "ROps"): "Tasks",
    ("Habitat", "Power"): "Maint"
}

communication_quality = [6, 9, 8, 7, 5, 8, 4, 6]

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

axs[0].set_title("Mars Base Comms Network", fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color=node_colors, edgecolors='black', ax=axs[0])
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2, ax=axs[0])  # Removed arrowstyle and arrowsize
nx.draw_networkx_labels(G, pos, font_size=10, font_family="serif", font_weight='bold', ax=axs[0])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkblue', font_size=8, label_pos=0.3, ax=axs[0])
axs[0].legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=module)
             for module, color in module_colors.items()],
    title='Modules',
    loc='upper left'
)
axs[0].axis('off')

axs[1].barh(modules, communication_quality[:len(modules)], color=[module_colors[module] for module in modules])
axs[1].set_title("Comms Quality", fontsize=12, fontweight='bold')
axs[1].set_xlabel("Score")
axs[1].set_xlim(0, max(communication_quality) + 2)
axs[1].invert_yaxis()
axs[1].grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()