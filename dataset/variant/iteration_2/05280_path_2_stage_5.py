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

G = nx.Graph()  # Changed this to create an undirected graph using nx.Graph
G.add_nodes_from(colonies)
for (colony1, colony2), frequency in routes.items():
    G.add_edge(colony1, colony2, weight=frequency)

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_shape='^', node_size=1800)
nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] * 2 for u, v in G.edges()],
    edge_color='purple',
    style='dotted'
)

plt.legend(["Colonies", "Routes"], loc='upper right')
plt.grid(visible=True)
plt.box(on=True)
plt.axis('off')
plt.tight_layout()
plt.show()