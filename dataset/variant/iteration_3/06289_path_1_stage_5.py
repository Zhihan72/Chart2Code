import matplotlib.pyplot as plt
import networkx as nx

# Shortened list of departments
departments = [
    "Sec Ops", "Threat Intel", "Incident Resp", "Vuln Mgmt",
    "Pentest", "Compliance", "Forensics"
]

# Shortened data capacities
data_capacity = [200, 150, 180, 90, 80, 60, 100]

# Shortened data transfer
data_transfer = [
    ("Sec Ops", "Threat Intel", 120),
    ("Sec Ops", "Incident Resp", 100),
    ("Threat Intel", "Vuln Mgmt", 80),
    ("Incident Resp", "Forensics", 70),
    ("Incident Resp", "Pentest", 65),
    ("Vuln Mgmt", "Pentest", 50),
    ("Compliance", "Forensics", 40)
]

G = nx.Graph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(data_transfer)

pos = nx.spring_layout(G, seed=42)

node_colors = ['#FF5733', '#33FF57', '#3357FF', '#F39C12', '#8E44AD', '#2ECC71', '#E74C3C']
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