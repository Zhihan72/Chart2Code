import matplotlib.pyplot as plt
import networkx as nx

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

G = nx.DiGraph()
G.add_nodes_from(regions)
G.add_weighted_edges_from(energy_exchanges)

pos = nx.spring_layout(G, seed=42)

# Random style alterations
node_colors = ['#4682B4', '#32CD32', '#FF6347', '#FFDAB9', '#8A2BE2', '#1E90FF', '#FF4500']
node_sizes = [annual_energy_production[region] * 15 for region in regions] # Changed multiplier for sizes

fig, axes = plt.subplots(1, 2, figsize=(18, 8))
plt.subplots_adjust(wspace=0.4)

# Plot 1: Bar Chart
regions_list = list(annual_energy_production.keys())
energy_values = list(annual_energy_production.values())
axes[0].bar(regions_list, energy_values, color=node_colors, alpha=0.6)
axes[0].tick_params(axis='x', labelrotation=45) # Added label rotation

# Plot 2: Directed Network Graph
nx.draw_networkx_nodes(G, pos, ax=axes[1], node_size=node_sizes, node_color=node_colors, alpha=0.8)
edge_weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, ax=axes[1], arrowstyle='-|>', arrowsize=25, width=[0.4 * weight for weight in edge_weights.values()], style='dotted') # Changed arrowstyle, arrowsize, and style
axes[1].grid(True) # Added grid
axes[1].spines['top'].set_visible(False) # Removed top border
axes[1].spines['right'].set_visible(False) # Removed right border

plt.tight_layout()
plt.show()