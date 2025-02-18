import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'Dragon', 'Phoenix', 'Unicorn', 'Griffin', 'Mermaid',
    'Sword of Light', 'Phoenix Feather', 'Unicorn Horn',
    'Griffin Claw', 'Mermaid Scale',
    'Fairy', 'Pegasus', 'Troll',
    'Magic Wand', 'Pegasus Feather', 'Troll Stone'
]

edges = [
    ('Dragon', 'Sword of Light'),
    ('Dragon', 'Griffin Claw'),
    ('Phoenix', 'Phoenix Feather'),
    ('Phoenix', 'Sword of Light'),
    ('Unicorn', 'Unicorn Horn'),
    ('Griffin', 'Griffin Claw'),
    ('Mermaid', 'Mermaid Scale'),
    ('Mermaid', 'Unicorn Horn'),
    ('Phoenix', 'Mermaid Scale'),
    ('Fairy', 'Magic Wand'),
    ('Fairy', 'Phoenix Feather'),
    ('Pegasus', 'Pegasus Feather'),
    ('Pegasus', 'Magic Wand'),
    ('Troll', 'Troll Stone'),
    ('Troll', 'Griffin Claw')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Use a single color 'skyblue' for all nodes
node_color = 'skyblue'
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_color, edgecolors='black', linewidths=1.5)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='darkgrey')

plt.axis('off')
plt.tight_layout()
plt.show()