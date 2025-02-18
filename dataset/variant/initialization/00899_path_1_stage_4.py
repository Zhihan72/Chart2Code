import matplotlib.pyplot as plt
import networkx as nx

institutions = [
    'MIT Quantum Lab', 'Stanford AI Lab', 'Cambridge QI', 'Oxford Computing',
    'Caltech Research', 'IBM Q System', 'Google AI Quantum', 'Microsoft Research',
    'Harvard Quantum Initiative', 'ETH Zurich'
]

collaborations = [
    ('Caltech Research', 'MIT Quantum Lab'), ('Google AI Quantum', 'IBM Q System'),
    ('Harvard Quantum Initiative', 'Google AI Quantum'), ('Stanford AI Lab', 'Caltech Research'),
    ('Oxford Computing', 'Harvard Quantum Initiative'), ('Microsoft Research', 'Stanford AI Lab'),
    ('Cambridge QI', 'Microsoft Research'), ('ETH Zurich', 'Cambridge QI'),
    ('IBM Q System', 'Stanford AI Lab'), ('Oxford Computing', 'MIT Quantum Lab'),
    ('Caltech Research', 'Stanford AI Lab'), ('MIT Quantum Lab', 'Harvard Quantum Initiative'),
    ('Google AI Quantum', 'Cambridge QI'), ('Microsoft Research', 'ETH Zurich'),
    ('Oxford Computing', 'IBM Q System'), ('IBM Q System', 'ETH Zurich'),
    ('Stanford AI Lab', 'Harvard Quantum Initiative')
]

G = nx.Graph()
G.add_nodes_from(institutions)
G.add_edges_from(collaborations)

pos = nx.spring_layout(G, seed=24)

plt.figure(figsize=(14, 10))
node_sizes = [G.degree(node) * 300 for node in G.nodes]
node_colors = ['lightgreen' if 'Quantum' in node or 'QI' in node else 'lightblue' for node in G.nodes]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, edge_color='gray', style='solid')

plt.axis('off')
plt.show()