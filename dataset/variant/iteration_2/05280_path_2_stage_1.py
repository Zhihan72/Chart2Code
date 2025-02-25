import matplotlib.pyplot as plt
import networkx as nx

# Define space colonies
colonies = ['Alpha Terra', 'Beta Centauri', 'Gamma Orion', 'Delta Vortex', 'Epsilon Blade', 'Zeta Haven']

# Define transportation routes (edges) between colonies with frequency of transports
routes = {
    ('Alpha Terra', 'Beta Centauri'): 3,
    ('Alpha Terra', 'Gamma Orion'): 2,
    ('Beta Centauri', 'Delta Vortex'): 4,
    ('Gamma Orion', 'Epsilon Blade'): 1,
    ('Delta Vortex', 'Epsilon Blade'): 5,
    ('Epsilon Blade', 'Zeta Haven'): 2,
    ('Zeta Haven', 'Alpha Terra'): 3,
    ('Beta Centauri', 'Gamma Orion'): 4,
}

# Create a graph using NetworkX
G = nx.Graph()

# Add nodes with colonies
G.add_nodes_from(colonies)

# Add edges with transport frequencies
for (colony1, colony2), frequency in routes.items():
    G.add_edge(colony1, colony2, weight=frequency)

# Draw the graph using Matplotlib
plt.figure(figsize=(12, 10))

# Position the nodes using a spring layout
pos = nx.spring_layout(G, seed=24)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='cyan', node_size=1800)

# Draw edges with different widths based on transport frequency
nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] for u, v in G.edges()],
    edge_color='grey'
)

# Adjust layout
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()