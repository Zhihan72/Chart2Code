import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Solar System Spacecraft Missions since 1970
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
# Creating the undirected graph
G = nx.Graph(missions)

# Calculate node sizes based on degree centrality with a base size
node_sizes = [1000 + 2000 * nx.degree_centrality(G)[node] for node in G.nodes()]

# Assign colors to nodes based on their mission type
node_colors = {
    "Voyager 1": "#ffcc00",
    "Voyager 2": "#66c2a5",
    "Cassini": "#fc8d62",
    "Juno": "#8da0cb",
    "New Horizons": "#e78ac3",
    "Mariner 10": "#a6d854",
    "Galileo": "#ffd92f",
    "Rosetta": "#ff9999",
    'Solar System': "#80cb00",
    'Jupiter': "#ff0033",
}

# Extract colors for each node in the graph
colors = [node_colors[node] for node in G.nodes()]

# Define positions for the nodes using a spring layout
pos = nx.spring_layout(G, seed=42)

# Draw nodes with varying size and assigned color
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=colors, edgecolors='black', alpha=0.9)

# Draw edges with a fixed thickness
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='lightblue')

# Draw labels with careful positioning
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Title and layout adjustments
plt.title("Explorers of the Solar System:\nSpacecraft Missions since 1970", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.axis('off')  # Turn off the axis for clearer visualization

# Custom legend
handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Voyager 1', markerfacecolor='#ffcc00', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Voyager 2', markerfacecolor='#66c2a5', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Cassini', markerfacecolor='#fc8d62', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Juno', markerfacecolor='#8da0cb', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='New Horizons', markerfacecolor='#e78ac3', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Mariner 10', markerfacecolor='#a6d854', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Galileo', markerfacecolor='#ffd92f', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Rosetta', markerfacecolor='#ff9999', markersize=10)
]
plt.legend(handles=handles, title="Spacecraft Missions", loc='upper right', fontsize=10, title_fontsize=12)

# Display the plot
plt.show()