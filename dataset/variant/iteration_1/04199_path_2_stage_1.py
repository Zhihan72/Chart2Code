import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

missions = {
    "Voyager 1": ["Solar System", "Jupiter", "Galileo"],
    "Voyager 2": ["Mariner 10", "Jupiter", "Galileo", "Juno", "Cassini"],
    "Cassini": ["Galileo", "Juno"],
    "Juno": ["Jupiter"],
    "New Horizons": ["Juno", "Solar System"],
    "Mariner 10": ["Solar System", "Juno"],
    "Galileo": ["Jupiter", "Cassini", "New Horizons"],
    "Rosetta": ["New Horizons"]
}

G = nx.Graph(missions)

node_sizes = [800 + 2500 * nx.degree_centrality(G)[node] for node in G.nodes()]

node_colors = {
    "Voyager 1": "#99ccff",
    "Voyager 2": "#ccff66",
    "Cassini": "#ff9900",
    "Juno": "#cc33ff",
    "New Horizons": "#ffcc99",
    "Mariner 10": "#66ff66",
    "Galileo": "#cc3333",
    "Rosetta": "#ff0099",
    'Solar System': "#336699",
    'Jupiter': "#663300",
}

colors = [node_colors[node] for node in G.nodes()]

pos = nx.shell_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=colors, edgecolors='grey', alpha=0.8, linewidths=2)

nx.draw_networkx_edges(G, pos, width=3, alpha=0.5, edge_color='purple', style='dashed')

nx.draw_networkx_labels(G, pos, font_size=9, font_family='monospace', font_weight='bold')

plt.title("Explorers of the Solar System", fontsize=16, fontweight='heavy')
plt.tight_layout()
plt.grid(True, which='both', linestyle='-.', linewidth=0.5)
plt.axis('on')

handles = [
    plt.Line2D([0], [0], marker='s', color='w', label='Voyager 1', markerfacecolor='#99ccff', markersize=12),
    plt.Line2D([0], [0], marker='^', color='w', label='Voyager 2', markerfacecolor='#ccff66', markersize=12),
    plt.Line2D([0], [0], marker='D', color='w', label='Cassini', markerfacecolor='#ff9900', markersize=12),
    plt.Line2D([0], [0], marker='v', color='w', label='Juno', markerfacecolor='#cc33ff', markersize=12),
    plt.Line2D([0], [0], marker='H', color='w', label='New Horizons', markerfacecolor='#ffcc99', markersize=12),
    plt.Line2D([0], [0], marker='p', color='w', label='Mariner 10', markerfacecolor='#66ff66', markersize=12),
    plt.Line2D([0], [0], marker='X', color='w', label='Galileo', markerfacecolor='#cc3333', markersize=12),
    plt.Line2D([0], [0], marker='*', color='w', label='Rosetta', markerfacecolor='#ff0099', markersize=12)
]
plt.legend(handles=handles, title="Spacecraft Missions", loc='lower left', fontsize=11, title_fontsize=13)

plt.show()