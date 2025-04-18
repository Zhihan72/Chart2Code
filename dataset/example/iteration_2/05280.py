import matplotlib.pyplot as plt
import networkx as nx

# Backstory: Galactic Transportation Network that connects various colonies in a futuristic space setting

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
nx.draw_networkx_nodes(G, pos, node_color='cyan', node_size=1800,)

# Draw edges with different widths based on transport frequency
edges = nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] for u, v in G.edges()],
    edge_color='grey'
)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_family='sans-serif',)

# Title and legend
plt.title('Galactic Transportation Network\nConnecting the Space Colonies', fontsize=18, fontweight='bold')

# Create a legend for edge widths (custom legend for aesthetics)
plt.text(1.1, 0.85, 'Transport Frequency', fontsize=12, ha='right')
plt.plot([], [], color='grey', linewidth=1, label='1-2 transports/week')
plt.plot([], [], color='grey', linewidth=3, label='3-4 transports/week')
plt.plot([], [], color='grey', linewidth=5, label='5+ transports/week')
plt.legend(title='Frequency', bbox_to_anchor=(1.15, 1))

# Adjust layout
plt.axis('off')
plt.tight_layout()

# Display the plot
plt.show()