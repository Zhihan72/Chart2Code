import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Backstory: Exploration of energy collaboration among different regions in a futuristic world, where regions share renewable energy resources.
regions = [
    "North America", "South America", "Europe", "Africa",
    "Asia", "Australia", "Antarctica"
]

# Define the collaborations with weights representing energy exchange capacity (in terawatts)
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

# Annual renewable energy production in terawatts
annual_energy_production = {
    "North America": 150,
    "South America": 120,
    "Europe": 130,
    "Africa": 80,
    "Asia": 200,
    "Australia": 90,
    "Antarctica": 50
}

# Create an undirected graph
G = nx.Graph()
G.add_nodes_from(regions)
G.add_weighted_edges_from(energy_exchanges)

# Define positions using spring layout
pos = nx.spring_layout(G, seed=42)

# Node attributes
node_colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFD700', '#FFA07A', '#20B2AA', '#9370DB']
node_sizes = [annual_energy_production[region] * 10 for region in regions]

# Set up subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))
plt.subplots_adjust(wspace=0.4)

# Plot 1: Network Graph
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=node_sizes, node_color=node_colors, alpha=0.9)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, ax=axes[0], width=[0.5 * weight for weight in edge_weights.values()], alpha=0.7)
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=9, font_family='sans-serif', verticalalignment='bottom')
edge_labels = {(u, v): f"{d['weight']} TW" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, ax=axes[0], edge_labels=edge_labels, font_color='darkgreen', font_size=8)
axes[0].set_title("Futuristic Global Energy Collaborations\n2050", fontsize=12, fontweight='bold')
axes[0].axis('off')

# Plot 2: Bar Chart for Annual Renewable Energy Production
regions_list = list(annual_energy_production.keys())
energy_values = list(annual_energy_production.values())
axes[1].bar(regions_list, energy_values, color=node_colors, alpha=0.8)
axes[1].set_title("Annual Renewable Energy Production (in TW)", fontsize=12, fontweight='bold')
axes[1].set_ylabel("Energy Production (TW)")
axes[1].set_xlabel("Regions")
axes[1].tick_params(axis='x', rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()