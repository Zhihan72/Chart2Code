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

G = nx.DiGraph()  # Change to directed graph
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
axes[0].tick_params(axis='x', labelbottom=False)

# Plot 2: Directed Network Graph
nx.draw_networkx_nodes(G, pos, ax=axes[1], node_size=node_sizes, node_color=node_colors, alpha=0.9)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, ax=axes[1], arrowstyle='->', arrowsize=20, width=[0.5 * weight for weight in edge_weights.values()], alpha=0.7)
axes[1].axis('off')

plt.tight_layout()
plt.show()