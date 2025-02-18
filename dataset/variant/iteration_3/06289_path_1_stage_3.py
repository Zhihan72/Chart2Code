import matplotlib.pyplot as plt
import networkx as nx

departments = [
    "Security Operations", "Threat Intelligence", "Incident Response",
    "Vulnerability Management", "Penetration Testing", "Governance", "Compliance", "Forensics"
]
data_capacity = [200, 150, 180, 90, 80, 70, 60, 100]

data_transfer = [
    ("Security Operations", "Threat Intelligence", 120),
    ("Security Operations", "Incident Response", 100),
    ("Threat Intelligence", "Vulnerability Management", 80),
    ("Incident Response", "Forensics", 70),
    ("Incident Response", "Penetration Testing", 65),
    ("Vulnerability Management", "Penetration Testing", 50),
    ("Governance", "Compliance", 75),
    ("Compliance", "Forensics", 40),
    ("Forensics", "Governance", 55)
]

G = nx.Graph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(data_transfer)

pos = nx.spring_layout(G, seed=42)

# New set of colors for nodes
node_colors = ['#FF5733', '#33FF57', '#3357FF', '#F39C12', '#8E44AD', '#2ECC71', '#E74C3C', '#3498DB']
node_sizes = [size * 10 for size in data_capacity]

fig, ax = plt.subplots(figsize=(14, 8))

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.8, edgecolors='black')
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[0.05 * weight for weight in edge_weights.values()], alpha=0.7)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='darkblue')

edge_labels = {(u, v): f"{d['weight']} TB" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green', font_size=9)

ax.axis('off')
plt.tight_layout()
plt.show()