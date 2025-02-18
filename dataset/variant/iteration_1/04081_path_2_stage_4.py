import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

regions = [
    "NA", "SA", "EU", "AF",
    "AS", "AU"
]

energy_exchanges = [
    ("NA", "SA", 7),
    ("NA", "EU", 8),
    ("EU", "AF", 10),
    ("AF", "AS", 6),
    ("AS", "AU", 5),
    ("EU", "AS", 9),
    ("NA", "AS", 5),
    ("EU", "AU", 6),
]

annual_energy_production = {
    "NA": 150,
    "SA": 120,
    "EU": 130,
    "AF": 80,
    "AS": 200,
    "AU": 90
}

G = nx.Graph()
G.add_nodes_from(regions)
G.add_weighted_edges_from(energy_exchanges)

pos = nx.spring_layout(G, seed=42)

# Shuffled colors list
node_colors = ['#FFD700', '#20B2AA', '#90EE90', '#FFA07A', '#ADD8E6', '#FFB6C1']
node_sizes = [annual_energy_production[region] * 10 for region in regions]

fig, axes = plt.subplots(1, 2, figsize=(18, 8))
plt.subplots_adjust(wspace=0.4)

nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=node_sizes, node_color=node_colors, alpha=0.9)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, ax=axes[0], width=[0.5 * weight for weight in edge_weights.values()], alpha=0.7)
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=9, font_family='sans-serif', verticalalignment='bottom')
edge_labels = {(u, v): f"{d['weight']} TW" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, ax=axes[0], edge_labels=edge_labels, font_color='darkgreen', font_size=8)
axes[0].axis('off')
axes[0].set_title("Energy Network")

regions_list = list(annual_energy_production.keys())
energy_values = list(annual_energy_production.values())
axes[1].bar(regions_list, energy_values, color=node_colors, alpha=0.8)
axes[1].set_ylabel("Prod. (TW)")
axes[1].set_xlabel("Cont.")
axes[1].set_title("Annual Energy Prod.")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()