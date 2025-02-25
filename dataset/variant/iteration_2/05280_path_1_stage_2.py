import matplotlib.pyplot as plt
import networkx as nx

colonies = ['Alpha Terra', 'Beta Centauri', 'Gamma Orion', 'Delta Vortex', 'Epsilon Blade', 'Zeta Haven']

# Routes with altered transport frequencies
routes = {
    ('Alpha Terra', 'Beta Centauri'): 4,  # Altered
    ('Alpha Terra', 'Gamma Orion'): 1,   # Altered
    ('Beta Centauri', 'Delta Vortex'): 3,  # Altered
    ('Gamma Orion', 'Epsilon Blade'): 2,  # Altered
    ('Delta Vortex', 'Epsilon Blade'): 5,
    ('Epsilon Blade', 'Zeta Haven'): 1,  # Altered
    ('Zeta Haven', 'Alpha Terra'): 4,  # Altered
    ('Beta Centauri', 'Gamma Orion'): 3   # Altered
}

G = nx.Graph()
G.add_nodes_from(colonies)
for (colony1, colony2), frequency in routes.items():
    G.add_edge(colony1, colony2, weight=frequency)

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=24)

nx.draw_networkx_nodes(G, pos, node_color='cyan', node_size=1800)
nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] for u, v in G.edges()],
    edge_color='grey'
)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_family='sans-serif')

plt.title('Galactic Transportation Network\nConnecting the Space Colonies', fontsize=18, fontweight='bold')

plt.text(1.1, 0.85, 'Transport Frequency', fontsize=12, ha='right')
plt.plot([], [], color='grey', linewidth=1, label='1-2 transports/week')
plt.plot([], [], color='grey', linewidth=3, label='3-4 transports/week')
plt.plot([], [], color='grey', linewidth=5, label='5+ transports/week')
plt.legend(title='Frequency', bbox_to_anchor=(1.15, 1))

plt.axis('off')
plt.tight_layout()
plt.show()