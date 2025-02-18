import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib as mpl

# Define the cities as nodes and the trade routes as directed edges with weights.
cities = [
    "Sun City", "Moon Valley", "Star Town", "Comet Ridge", 
    "Eclipse Bay", "Meteor Plains", "Nebula Hill", "Galaxy Hamlet", "Aurora Village"
]

# Define connections (trade routes) with weights indicating trade volume
trade_routes = [
    ("Sun City", "Moon Valley", 75), ("Moon Valley", "Star Town", 65), 
    ("Star Town", "Comet Ridge", 50), ("Comet Ridge", "Eclipse Bay", 40), 
    ("Eclipse Bay", "Meteor Plains", 55), ("Meteor Plains", "Nebula Hill", 35), 
    ("Nebula Hill", "Galaxy Hamlet", 45), ("Galaxy Hamlet", "Aurora Village", 30), 
    ("Aurora Village", "Sun City", 60), ("Sun City", "Meteor Plains", 50), 
    ("Moon Valley", "Eclipse Bay", 35), ("Comet Ridge", "Nebula Hill", 50), 
    ("Star Town", "Aurora Village", 40)
]

# Create the directed graph
G = nx.DiGraph()
G.add_nodes_from(cities)
G.add_weighted_edges_from(trade_routes)

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)

# Draw the nodes with customization
nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='skyblue', alpha=0.9, edgecolors='k', ax=ax)

# Draw the edges with weights
edges_weights = [weight for (_, _, weight) in trade_routes]
nx.draw_networkx_edges(G, pos, edgelist=trade_routes, arrowstyle='-|>', arrowsize=15, edge_color=edges_weights, 
                       edge_cmap=plt.cm.viridis, width=2, ax=ax)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='center', ax=ax)

# Draw edge labels for weights
edge_labels = {(u, v): f"{w}" for u, v, w in trade_routes}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=9, ax=ax)

# Create a ScalarMappable and add a colorbar
sm = mpl.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(edges_weights), vmax=max(edges_weights)))
sm.set_array([])
plt.colorbar(sm, label="Trade Volume Intensity", ax=ax)

# Add title
plt.title("Trade Routes of Solaris Kingdom:\nAn Ancient Trading Network", fontsize=16, fontweight='bold')
plt.axis('off')

# Adjust layout to prevent overlap and ensure clarity
plt.tight_layout()
plt.show()