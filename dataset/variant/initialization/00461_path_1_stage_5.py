import matplotlib.pyplot as plt
import networkx as nx

# Shuffled and altered department names
departments = ['Finance', 'HR', 'Operations', 'R&D', 'Sales', 'Customer Support', 'Marketing']

# Corresponding shuffled communication matrix
communication_matrix = [
    [0, 5, 15, 10, 20, 12, 15],
    [5, 0, 5, 10, 5, 9, 5],
    [15, 5, 0, 8, 10, 15, 15],
    [10, 10, 8, 0, 5, 10, 15],
    [20, 5, 10, 5, 0, 12, 25],
    [12, 9, 15, 10, 12, 0, 7],
    [15, 5, 15, 15, 25, 7, 0]
]

G = nx.Graph()
G.add_nodes_from(departments)

for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if i < j and communication_matrix[i][j] > 0:
            G.add_edge(source, target, weight=communication_matrix[i][j])

pos = nx.spring_layout(G, k=0.3, iterations=50)

plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightgreen')

# Randomly altered labels - shuffled or altered names
nx.draw_networkx_labels(G, pos, labels={node: f"Dept-{n}" for n, node in enumerate(departments)}, 
                        font_size=12, font_color='black', font_weight='bold')

edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[edge[2]['weight'] * 0.1 for edge in edges])

plt.axis('off')
plt.tight_layout()
plt.show()