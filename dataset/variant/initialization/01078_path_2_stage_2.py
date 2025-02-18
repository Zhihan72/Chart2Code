import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'Griffin', 'Sword of Light', 'Dragon', 'Mermaid', 'Mermaid Scale',
    'Unicorn Horn', 'Phoenix', 'Phoenix Feather', 'Unicorn', 'Griffin Claw'
]

edges = [
    ('Mermaid', 'Sword of Light'),
    ('Griffin', 'Phoenix Feather'),
    ('Phoenix', 'Griffin Claw'),
    ('Dragon', 'Mermaid Scale'),
    ('Unicorn', 'Unicorn Horn'),
    ('Dragon', 'Mermaid'),
    ('Phoenix', 'Phoenix Feather'),
    ('Griffin', 'Mermaid Scale'), 
    ('Mermaid', 'Phoenix')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

node_colors = ['lightgreen' if ' ' in node else 'skyblue' for node in nodes]

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='darkgrey')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

plt.axis('off')
plt.show()