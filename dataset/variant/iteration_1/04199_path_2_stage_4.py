import matplotlib.pyplot as plt
import networkx as nx

missions = {
    "Voyager 1": ["Solar Sys", "Jupiter", "Gal"],
    "Voyager 2": ["Mariner", "Jupiter", "Gal", "Juno", "Cassini"],
    "Cassini": ["Gal", "Juno"],
    "Juno": ["Jupiter"],
    "New Horizons": ["Juno", "Solar Sys"],
    "Mariner": ["Solar Sys", "Juno"],
    "Gal": ["Jupiter", "Cassini", "New Horizons"],
    "Rosetta": ["New Horizons"]
}

# Convert directed adjacency list to include reverse edges for undirected graph
undirected_edges = {(source, target) for source, targets in missions.items() for target in targets}
undirected_edges.update({(target, source) for source, target in undirected_edges})

G = nx.Graph(list(undirected_edges))

node_sizes = [800 + 2500 * nx.degree_centrality(G)[node] for node in G.nodes()]

node_colors = {
    "Voyager 1": "#1f77b4",
    "Voyager 2": "#ff7f0e",
    "Cassini": "#2ca02c",
    "Juno": "#d62728",
    "New Horizons": "#9467bd",
    "Mariner": "#8c564b",
    "Gal": "#e377c2",
    "Rosetta": "#7f7f7f",
    'Solar Sys': "#bcbd22",
    'Jupiter': "#17becf",
}

colors = [node_colors[node] for node in G.nodes()]

pos = nx.shell_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=colors, edgecolors='grey', alpha=0.8, linewidths=2)
nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color='purple', style='dashed')
nx.draw_networkx_labels(G, pos, font_size=9, font_family='monospace', font_weight='bold')

plt.title("Space Probes", fontsize=16, fontweight='heavy')
plt.tight_layout()
plt.grid(True, which='both', linestyle='-.', linewidth=0.5)
plt.axis('on')

handles = [
    plt.Line2D([0], [0], marker='s', color='w', label='V1', markerfacecolor='#1f77b4', markersize=12),
    plt.Line2D([0], [0], marker='^', color='w', label='V2', markerfacecolor='#ff7f0e', markersize=12),
    plt.Line2D([0], [0], marker='D', color='w', label='Cas', markerfacecolor='#2ca02c', markersize=12),
    plt.Line2D([0], [0], marker='v', color='w', label='Ju', markerfacecolor='#d62728', markersize=12),
    plt.Line2D([0], [0], marker='H', color='w', label='New Hz', markerfacecolor='#9467bd', markersize=12),
    plt.Line2D([0], [0], marker='p', color='w', label='Mariner', markerfacecolor='#8c564b', markersize=12),
    plt.Line2D([0], [0], marker='X', color='w', label='Gal', markerfacecolor='#e377c2', markersize=12),
    plt.Line2D([0], [0], marker='*', color='w', label='Rosetta', markerfacecolor='#7f7f7f', markersize=12)
]
plt.legend(handles=handles, title="Spacecraft", loc='lower left', fontsize=11, title_fontsize=13)

plt.show()