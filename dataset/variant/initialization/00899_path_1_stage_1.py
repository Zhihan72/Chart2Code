import matplotlib.pyplot as plt
import networkx as nx

institutions = [
    'MIT Quantum Lab', 'Stanford AI Lab', 'Cambridge QI', 'Oxford Computing',
    'Caltech Research', 'IBM Q System', 'Google AI Quantum', 'Microsoft Research',
    'Harvard Quantum Initiative', 'ETH Zurich'
]

collaborations = [
    ('MIT Quantum Lab', 'Stanford AI Lab'), ('MIT Quantum Lab', 'IBM Q System'),
    ('MIT Quantum Lab', 'Google AI Quantum'), ('Stanford AI Lab', 'Cambridge QI'),
    ('Stanford AI Lab', 'Oxford Computing'), ('Stanford AI Lab', 'Microsoft Research'),
    ('Cambridge QI', 'Oxford Computing'), ('Cambridge QI', 'Caltech Research'),
    ('Cambridge QI', 'IBM Q System'), ('Oxford Computing', 'ETH Zurich'),
    ('Oxford Computing', 'Google AI Quantum'), ('Caltech Research', 'IBM Q System'),
    ('Caltech Research', 'Microsoft Research'), ('Google AI Quantum', 'ETH Zurich'),
    ('Google AI Quantum', 'Harvard Quantum Initiative'), ('Microsoft Research', 'Harvard Quantum Initiative'),
    ('ETH Zurich', 'Harvard Quantum Initiative')
]

G = nx.Graph()
G.add_nodes_from(institutions)
G.add_edges_from(collaborations)

pos = nx.spring_layout(G, seed=24)

plt.figure(figsize=(14, 10))
node_sizes = [G.degree(node) * 300 for node in G.nodes]

# Shuffle the colors by swapping 'lightblue' with 'lightgreen'
node_colors = ['lightgreen' if 'Quantum' in node or 'QI' in node else 'lightblue' for node in G.nodes]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, edge_color='gray', style='solid')
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title('Collaborative Network in Quantum Computing Research', fontsize=16, fontweight='bold')
plt.annotate('Nodes: Research Institutions | Edges: Collaborative Projects\nNode size based on collaboration count', 
             xy=(0.5, -0.1), xycoords='axes fraction', ha='center', fontsize=10, color='darkslategray')

plt.tight_layout()
plt.axis('off')
plt.show()