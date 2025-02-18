import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

regions = ["North America", "South America", "Europe", "Africa", "Asia", "Australia", "Antarctica"]

energy_exchanges = [
    ("North America", "South America", 7),
    ("North America", "Europe", 8),
    ("Europe", "Africa", 10),
    ("Africa", "Asia", 6),
    ("Asia", "Australia", 5),
    ("Australia", "Antarctica", 3),
    ("Antarctica", "South America", 4),
    ("Europe", "Asia", 9),
    ("North America", "Asia", 5),
    ("Europe", "Australia", 6),
]

annual_energy_production = {
    "North America": 150,
    "South America": 120,
    "Europe": 130,
    "Africa": 80,
    "Asia": 200,
    "Australia": 90,
    "Antarctica": 50
}

G = nx.Graph()
G.add_nodes_from(regions)
G.add_weighted_edges_from(energy_exchanges)

pos = nx.spring_layout(G, seed=42)

node_colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFD700', '#FFA07A', '#20B2AA', '#9370DB']
node_sizes = [annual_energy_production[region] * 10 for region in regions]

fig, axes = plt.subplots(1, 2, figsize=(18, 8))
plt.subplots_adjust(wspace=0.4)

# Plot 1: Bar Chart for Annual Renewable Energy Production
regions_list = list(annual_energy_production.keys())
energy_values = list(annual_energy_production.values())
axes[0].bar(regions_list, energy_values, color=node_colors, alpha=0.8)
axes[0].set_title("Annual Renewable Energy Production (in TW)", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Energy Production (TW)")
axes[0].set_xlabel("Regions")
axes[0].tick_params(axis='x', rotation=45)

# Plot 2: Network Graph
nx.draw_networkx_nodes(G, pos, ax=axes[1], node_size=node_sizes, node_color=node_colors, alpha=0.9)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, ax=axes[1], width=[0.5 * weight for weight in edge_weights.values()], alpha=0.7)
nx.draw_networkx_labels(G, pos, ax=axes[1], font_size=9, font_family='sans-serif', verticalalignment='bottom')
edge_labels = {(u, v): f"{d['weight']} TW" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, ax=axes[1], edge_labels=edge_labels, font_color='darkgreen', font_size=8)
axes[1].set_title("Futuristic Global Energy Collaborations\n2050", fontsize=12, fontweight='bold')
axes[1].axis('off')

plt.tight_layout()
plt.show()