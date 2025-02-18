import matplotlib.pyplot as plt
import networkx as nx

institutions = [
    'MIT Quantum Lab', 'Stanford AI Lab', 'Cambridge QI', 'Oxford Computing',
    'Caltech Research', 'Google AI Quantum', 'Microsoft Research',
    'Harvard Quantum Initiative', 'ETH Zurich'
]

collaborations = [
    ('MIT Quantum Lab', 'Stanford AI Lab'), ('MIT Quantum Lab', 'Google AI Quantum'),
    ('Stanford AI Lab', 'Cambridge QI'), ('Stanford AI Lab', 'Oxford Computing'),
    ('Stanford AI Lab', 'Microsoft Research'), ('Cambridge QI', 'Oxford Computing'),
    ('Cambridge QI', 'Caltech Research'), ('Oxford Computing', 'ETH Zurich'),
    ('Oxford Computing', 'Google AI Quantum'), ('Caltech Research', 'Microsoft Research'),
    ('Google AI Quantum', 'ETH Zurich'), ('Google AI Quantum', 'Harvard Quantum Initiative'),
    ('Microsoft Research', 'Harvard Quantum Initiative'), ('ETH Zurich', 'Harvard Quantum Initiative')
]

G = nx.DiGraph()
G.add_nodes_from(institutions)
G.add_edges_from(collaborations)

pos = nx.spring_layout(G, seed=24)

plt.figure(figsize=(14, 10))
node_sizes = [G.degree(node) * 400 for node in G.nodes]
node_colors = ['lightblue' if 'Quantum' in node or 'QI' in node else 'lightpink' for node in G.nodes]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.85, edgecolors='grey')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.8, edge_color='black', style='--', arrows=True, arrowstyle='->', arrowsize=15)

plt.legend(['Quantum Entities', 'Other Entities'], loc='upper right', borderpad=1)
plt.grid(True, linestyle=':', linewidth=0.5)
plt.xticks([])  # Remove x-tick labels
plt.yticks([])  # Remove y-tick labels
plt.box(True)

plt.tight_layout()
plt.show()