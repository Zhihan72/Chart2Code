import matplotlib.pyplot as plt
import networkx as nx

features = [
    "Pathway", "Lunch Area", "Waterfall", "Jogging Track", 
    "Pet Zone", "Greenery", "Stage", "Washrooms", "Snack Spot"
]

connections = [
    ("Greenery", "Pet Zone"),
    ("Pathway", "Waterfall"),
    ("Washrooms", "Jogging Track"),
    ("Pet Zone", "Snack Spot"),
    ("Stage", "Greenery"),
    ("Lunch Area", "Washrooms"),
    ("Waterfall", "Stage"),
    ("Snack Spot", "Pathway"),
    ("Jogging Track", "Lunch Area")
]

G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=24)

node_colors = ['#ff6347', '#1e90ff', '#9acd32', '#dda0dd', '#f4a460', '#ffeb3b', '#adff2f', '#ff69b4', '#8b4513']
node_sizes = [1000, 850, 1200, 900, 1050, 950, 800, 1100, 800]

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=-0.2', arrowstyle='<|-', arrowsize=20, edge_color='gray', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=9, font_color='navy', font_family='sans-serif')

plt.title(
    'Dynamic Grid of Recreational Area Elements',
    fontsize=14, fontweight='light', color='teal', pad=25
)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axis('on')
plt.tight_layout()
plt.show()