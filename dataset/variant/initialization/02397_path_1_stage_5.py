import matplotlib.pyplot as plt
import networkx as nx

features = [
    "Playg.", "Picnic", "Fount.", "Path", 
    "Dog PK", "Garden", "Amphi.", "Rest.", "Food",
    "Bridge", "Lake", "Sports", "Monument"
]

connections = [
    ("Playg.", "Picnic"),
    ("Picnic", "Garden"),
    ("Garden", "Fount."),
    ("Fount.", "Path"),
    ("Path", "Amphi."),
    ("Amphi.", "Rest."),
    ("Rest.", "Food"),
    ("Food", "Dog PK"),
    ("Dog PK", "Playg."),
    ("Bridge", "Lake"),
    ("Lake", "Playg."),
    ("Lake", "Sports"),
    ("Sports", "Monument"),
    ("Monument", "Garden"),
    ("Bridge", "Monument")
]

G = nx.DiGraph()
G.add_nodes_from(features)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)

node_colors = ['#ff4500', '#4169e1', '#32cd32', '#ff1493', '#ffd700', '#20b2aa', '#ff00ff', '#00ced1', '#ff6347',
               '#8b00ff', '#00ff7f', '#4682b4', '#daa520']
node_sizes = [1200, 1000, 800, 1100, 900, 950, 1050, 850, 800, 900, 1100, 1000, 950]

plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,
        font_size=10, font_weight='bold', edge_color='gray', style='dashed', width=2.5, alpha=0.8, arrows=True)

plt.title(
    'Park Features Network with Additional Groups (Directed)',
    fontsize=16, fontweight='bold', pad=20
)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(['Legend: Example'], loc='upper right', fontsize=10, frameon=True, edgecolor='black')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_linewidth(1.5)

plt.axis('on')  # Changed to have axis visible for the grid
plt.tight_layout()
plt.show()