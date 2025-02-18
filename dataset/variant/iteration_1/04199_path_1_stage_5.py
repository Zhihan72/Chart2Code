import matplotlib.pyplot as plt
import networkx as nx

missions = {
    "Voyager 1": ["Solar System", "Jupiter", "Galileo"],
    "Voyager 2": ["Mariner 10", "Jupiter", "Galileo", "Juno", "Cassini"],
    "Cassini": ["Galileo", "Juno"],
    "Juno": ["Jupiter"],
    "New Horizons": ["Juno", "Solar System"],
    "Mariner 10": ["Solar System", "Juno"],
    "Galileo": ["Jupiter", "Cassini", "New Horizons"],
    "Rosetta": ["New Horizons"],
    "Mission X": ["Mariner 10", "Galileo"],
    "Mission Y": ["Voyager 1", "Juno"]
}

# Create an undirected graph
G = nx.Graph()

# Add edges to the graph
for mission, targets in missions.items():
    for target in targets:
        G.add_edge(mission, target)

node_sizes = [1000 + 2000 * nx.degree_centrality(G)[node] for node in G.nodes()]

# Apply a single color for all nodes
single_color = "#3498db"

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=single_color, edgecolors=None)

nx.draw_networkx_edges(G, pos, width=2, edge_color='lightblue')

plt.axis('off')

plt.show()