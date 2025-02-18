import matplotlib.pyplot as plt
import networkx as nx

# Include additional institutions in the network
institutions = [
    "MIT", "Stanford", "Cambridge", "Tokyo Univ", "Max Planck",
    "Caltech", "ETH Zurich", "Tsinghua", "Harvard", "Oxford",
    "Imperial College", "Peking Univ", "UC Berkeley", "Princeton", "EPFL"
]

# Extend collaborations with made-up data series
collaborations = [
    ("MIT", "Stanford"), ("MIT", "Cambridge"), ("Stanford", "Caltech"),
    ("Cambridge", "Tokyo Univ"), ("Cambridge", "Max Planck"), ("Tokyo Univ", "ETH Zurich"),
    ("Max Planck", "ETH Zurich"), ("Caltech", "Harvard"), ("ETH Zurich", "Oxford"),
    ("Harvard", "Oxford"), ("Tsinghua", "MIT"), ("Tsinghua", "Cambridge"),
    ("Max Planck", "Harvard"), ("Oxford", "Tsinghua"),
    ("Imperial College", "Peking Univ"), ("UC Berkeley", "Stanford"), 
    ("Princeton", "Harvard"), ("EPFL", "ETH Zurich"), ("UC Berkeley", "MIT"),
    ("Imperial College", "Cambridge"), ("Peking Univ", "Tsinghua")
]

G = nx.Graph()
G.add_nodes_from(institutions)
G.add_edges_from(collaborations)

centrality = nx.degree_centrality(G)
node_sizes = [centrality[node] * 3000 + 1000 for node in G.nodes()]

node_color = '#4682B4'

plt.figure(figsize=(12, 9))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_color, alpha=0.9)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', font_color='darkblue')

plt.title("Quantum Computing Collaborations:\nGlobal Research Network", fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()