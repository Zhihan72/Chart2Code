import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib as mpl

cities = [
    "Sun City", "Moon Valley", "Star Town", "Comet Ridge", 
    "Eclipse Bay", "Meteor Plains", "Nebula Hill", "Galaxy Hamlet", "Aurora Village"
]

trade_routes = [
    ("Sun City", "Moon Valley", 75), ("Moon Valley", "Star Town", 65), 
    ("Star Town", "Comet Ridge", 50), ("Comet Ridge", "Eclipse Bay", 40), 
    ("Eclipse Bay", "Meteor Plains", 55), ("Meteor Plains", "Nebula Hill", 35), 
    ("Nebula Hill", "Galaxy Hamlet", 45), ("Galaxy Hamlet", "Aurora Village", 30), 
    ("Aurora Village", "Sun City", 60), ("Sun City", "Meteor Plains", 50), 
    ("Moon Valley", "Eclipse Bay", 35), ("Comet Ridge", "Nebula Hill", 50), 
    ("Star Town", "Aurora Village", 40)
]

G = nx.Graph()
G.add_nodes_from(cities)
G.add_weighted_edges_from(trade_routes)

fig, ax = plt.subplots(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=1300, node_color='lightgreen', alpha=0.8, edgecolors='grey', ax=ax)

# Draw the edges
edges_weights = [weight for (_, _, weight) in trade_routes]
nx.draw_networkx_edges(G, pos, edgelist=trade_routes, edge_color=edges_weights, 
                       edge_cmap=plt.cm.coolwarm, style='dashed', width=3, ax=ax)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='heavy', verticalalignment='bottom', ax=ax)

# Draw edge labels for weights
edge_labels = {(u, v): f"{w}" for u, v, w in trade_routes}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple', font_size=7, ax=ax)

# Create a ScalarMappable and add a colorbar
sm = mpl.cm.ScalarMappable(cmap=plt.cm.coolwarm, norm=plt.Normalize(vmin=min(edges_weights), vmax=max(edges_weights)))
sm.set_array([])
plt.colorbar(sm, label="Trade Volume Intensity", ax=ax)

# Add title
plt.title("Trade Routes of Solaris Kingdom:\nAn Ancient Trading Network", fontsize=17, fontweight='bold', color='darkred')
plt.grid(visible=True, which='both', color='lightgrey', linestyle='--')
plt.tight_layout()
plt.show()