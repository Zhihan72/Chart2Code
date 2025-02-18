import matplotlib.pyplot as plt
import networkx as nx

colonies = ['Alpha Terra', 'Beta Centauri', 'Gamma Orion', 'Delta Vortex', 'Epsilon Blade', 'Zeta Haven']

routes = {
    ('Alpha Terra', 'Beta Centauri'): 4,
    ('Alpha Terra', 'Gamma Orion'): 1,
    ('Beta Centauri', 'Delta Vortex'): 3,
    ('Gamma Orion', 'Epsilon Blade'): 2,
    ('Delta Vortex', 'Epsilon Blade'): 5,
    ('Epsilon Blade', 'Zeta Haven'): 1,
    ('Zeta Haven', 'Alpha Terra'): 4,
    ('Beta Centauri', 'Gamma Orion'): 3
}

G = nx.Graph()
G.add_nodes_from(colonies)
for (colony1, colony2), frequency in routes.items():
    G.add_edge(colony1, colony2, weight=frequency)

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=24)

# Change node shape and edge styles
nx.draw_networkx_nodes(G, pos, node_color='coral', node_size=1800, node_shape='s')  # Square nodes
nx.draw_networkx_edges(
    G, pos,
    width=[G[u][v]['weight'] for u, v in G.edges()],
    edge_color='purple',
    style='dashed'  # Dashed lines
)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', font_family='sans-serif')

plt.title('Interstellar Trade Routes\nLinking Cosmic Settlements', fontsize=18, fontweight='bold')

plt.text(1.1, 0.85, 'Frequency of Connections', fontsize=12, ha='right')
plt.plot([], [], color='purple', linestyle='dashed', linewidth=1, label='Up to 2 trips/week')
plt.plot([], [], color='purple', linestyle='dashed', linewidth=3, label='3 or 4 trips/week')
plt.plot([], [], color='purple', linestyle='dashed', linewidth=5, label='Over 5 trips/week')
plt.legend(title='Transport Load', bbox_to_anchor=(1.15, 0.5))  # Adjusted legend position

plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.axis('on')
plt.tight_layout()
plt.show()