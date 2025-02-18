import matplotlib.pyplot as plt
import networkx as nx

departments = [
    "SecOps", "Threat Intel", "IR", 
    "VulMgmt", "Pentest", "Gov", 
    "Comp", "Forensics", "DataAnal", "RiskMgmt"
]
data_capacity = [200, 150, 180, 90, 80, 70, 60, 100, 130, 110]

data_transfer = [
    ("SecOps", "Threat Intel", 120),
    ("SecOps", "IR", 100),
    ("Threat Intel", "VulMgmt", 80),
    ("IR", "Forensics", 70),
    ("IR", "Pentest", 65),
    ("VulMgmt", "Pentest", 50),
    ("Gov", "Comp", 75),
    ("Comp", "Forensics", 40),
    ("Forensics", "Gov", 55),
    ("DataAnal", "RiskMgmt", 95),
    ("RiskMgmt", "SecOps", 85),
    ("DataAnal", "IR", 60)
]

G = nx.Graph()
G.add_nodes_from(departments)
G.add_weighted_edges_from(data_transfer)

pos = nx.kamada_kawai_layout(G)

# Manually shuffled colors
node_colors = ['#7B1FA2', '#0288D1', '#009688', '#C2185B', '#FBC02D', 
               '#D32F2F', '#1976D2', '#FF5722', '#388E3C', '#8E24AA']
node_sizes = [size * 12 for size in data_capacity]

fig, ax = plt.subplots(figsize=(14, 8))

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.7, edgecolors='gray')
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[0.03 * weight for weight in edge_weights.values()], alpha=0.9, style='dotted')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='light', font_color='purple')

edge_labels = {(u, v): f"{d['weight']} TB" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='orange', font_size=9)

plt.title("CyberGuard Network - Data Flow\nMonthly Transfers", fontsize=16, fontweight='regular', color='darkslategray', pad=15)
ax.axis('on')
ax.grid(True)

plt.tight_layout()
plt.show()