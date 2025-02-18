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
    "Rosetta": ["New Horizons"]
}

G = nx.Graph(missions)

node_sizes = [1000 + 2000 * nx.degree_centrality(G)[node] for node in G.nodes()]

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

colors = [node_colors[node] for node in G.nodes()]

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=colors, edgecolors=None)

nx.draw_networkx_edges(G, pos, width=2, edge_color='lightblue')

plt.axis('off')

plt.show()