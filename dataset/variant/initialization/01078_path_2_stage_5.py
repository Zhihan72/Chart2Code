import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'Unicorn Horn', 'Sword of Light', 'Phoenix', 'Mermaid',
    'Griffin Claw', 'Unicorn', 'Mermaid Scale', 'Dragon',
    'Griffin', 'Phoenix Feather'
]

edges = [
    ('Griffin', 'Mermaid Scale'),
    ('Dragon', 'Mermaid Scale'),
    ('Phoenix', 'Griffin Claw'),
    ('Mermaid', 'Sword of Light'),
    ('Phoenix', 'Phoenix Feather'),
    ('Griffin', 'Phoenix Feather'),
    ('Unicorn', 'Unicorn Horn'),
    ('Dragon', 'Mermaid'),
    ('Mermaid', 'Phoenix')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightcoral', edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='darkgrey')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

plt.title('Mythical Creatures and Artifacts')
plt.axis('off')
plt.show()