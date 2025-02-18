import matplotlib.pyplot as plt
import networkx as nx

institutions = [
    "MIT", "Stanford", "Cambridge", "Tokyo", "Max Planck",
    "Caltech", "ETH Zurich", "Tsinghua", "Harvard", "Oxford",
    "Imperial", "Peking", "Berkeley", "Princeton", "EPFL"
]

collaborations = [
    ("MIT", "Stanford"), ("MIT", "Cambridge"), ("Stanford", "Caltech"),
    ("Cambridge", "Tokyo"), ("Cambridge", "Max Planck"), ("Tokyo", "ETH Zurich"),
    ("Max Planck", "ETH Zurich"), ("Caltech", "Harvard"), ("ETH Zurich", "Oxford"),
    ("Harvard", "Oxford"), ("Tsinghua", "MIT"), ("Tsinghua", "Cambridge"),
    ("Max Planck", "Harvard"), ("Oxford", "Tsinghua"),
    ("Imperial", "Peking"), ("Berkeley", "Stanford"), 
    ("Princeton", "Harvard"), ("EPFL", "ETH Zurich"), ("Berkeley", "MIT"),
    ("Imperial", "Cambridge"), ("Peking", "Tsinghua")
]

G = nx.Graph()
G.add_nodes_from(institutions)
G.add_edges_from(collaborations)

centrality = nx.degree_centrality(G)
node_sizes = [centrality[node] * 3000 + 1000 for node in G.nodes()]

node_colors = ['#4682B4', '#B22222', '#FF8C00', '#32CD32', '#DA70D6']
node_color = [node_colors[i % len(node_colors)] for i in range(len(institutions))]

plt.figure(figsize=(12, 9))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_color, alpha=0.75, linewidths=1.5, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color='magenta', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='medium', font_color='green')

plt.title("Quantum Computing Collaborations", fontsize=16, fontweight='bold', pad=20)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()