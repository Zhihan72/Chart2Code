import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import matplotlib as mpl

cities = [
    "Aurora Meadow", "Eclipse Valley", "Starlight Haven", 
    "Lunar Ridge", "Comet Flatlands", "Quasar Hill", 
    "Nebula Nook", "Galaxy Glade"
]

trade_routes = [
    ("Aurora Meadow", "Eclipse Valley", 65), ("Eclipse Valley", "Starlight Haven", 75), 
    ("Lunar Ridge", "Comet Flatlands", 55), ("Comet Flatlands", "Quasar Hill", 30), 
    ("Quasar Hill", "Nebula Nook", 45), ("Nebula Nook", "Galaxy Glade", 35), 
    ("Galaxy Glade", "Aurora Meadow", 50), ("Aurora Meadow", "Comet Flatlands", 60), 
    ("Eclipse Valley", "Lunar Ridge", 40), ("Starlight Haven", "Galaxy Glade", 35)
]

G = nx.Graph()
G.add_nodes_from(cities)
G.add_weighted_edges_from(trade_routes)

fig, ax = plt.subplots(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=1300, node_color='lightyellow', alpha=0.8, edgecolors='grey', ax=ax)

edges_weights = [weight for (_, _, weight) in trade_routes]
nx.draw_networkx_edges(G, pos, edgelist=trade_routes, edge_color=edges_weights, 
                       edge_cmap=plt.cm.coolwarm, style='dashed', width=3, ax=ax)

nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', verticalalignment='bottom', ax=ax)

edge_labels = {(u, v): f"{w}" for u, v, w in trade_routes}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='orange', font_size=7, ax=ax)

sm = mpl.cm.ScalarMappable(cmap=plt.cm.coolwarm, norm=plt.Normalize(vmin=min(edges_weights), vmax=max(edges_weights)))
sm.set_array([])
plt.colorbar(sm, label="Intensity of Trade Volume", ax=ax)

plt.title("Solaris Dominion's Commerce Pathways:\nAntique Trade Web", fontsize=17, fontweight='bold', color='brown')
plt.grid(visible=True, which='both', color='lightgrey', linestyle='--')
plt.tight_layout()
plt.show()