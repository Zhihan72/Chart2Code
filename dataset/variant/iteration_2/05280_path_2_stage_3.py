import matplotlib.pyplot as plt
import networkx as nx

colonies = ['Alpha Terra', 'Beta Centauri', 'Gamma Orion', 'Epsilon Blade', 'Zeta Haven']

routes = {
    ('Alpha Terra', 'Beta Centauri'): 3,
    ('Alpha Terra', 'Gamma Orion'): 2,
    ('Gamma Orion', 'Epsilon Blade'): 1,
    ('Epsilon Blade', 'Zeta Haven'): 2,
    ('Zeta Haven', 'Alpha Terra'): 3,
    ('Beta Centauri', 'Gamma Orion'): 4,
}

G = nx.Graph()
G.add_nodes_from(colonies)
for (colony1, colony2), frequency in routes.items():
    G.add_edge(colony1, colony2, weight=frequency)

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)

# Randomized styling changes
nx.draw_networkx_nodes(G, pos, node_color='orange', node_shape='^', node_size=1800)
nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] * 2 for u, v in G.edges()],
    edge_color='green',
    style='dotted'
)

# Adding legend
plt.legend(["Colonies", "Routes"], loc='upper right')

# Turn on grid
plt.grid(visible=True)

# Random border settings
plt.box(on=True)

# Removed axis
plt.axis('off')
plt.tight_layout()
plt.show()