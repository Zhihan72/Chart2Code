import matplotlib.pyplot as plt
import networkx as nx

departments = ['R&D', 'Marketing', 'Sales', 'HR', 'Customer Support', 'Finance', 'Operations']
communication_matrix = [
    [0, 15, 20, 5, 10, 12, 8],
    [10, 0, 25, 5, 15, 15, 10],
    [5, 10, 0, 5, 20, 10, 5],
    [10, 5, 5, 0, 15, 6, 9],
    [5, 5, 15, 10, 0, 7, 12],
    [10, 15, 20, 8, 5, 0, 15],
    [5, 10, 10, 5, 15, 15, 0]
]

G = nx.Graph()
G.add_nodes_from(departments)

for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if i < j and communication_matrix[i][j] > 0:
            G.add_edge(source, target, weight=communication_matrix[i][j])

pos = nx.spring_layout(G, k=0.3, iterations=50)

plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='skyblue')
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[edge[2]['weight'] * 0.1 for edge in edges])

plt.axis('off')
plt.tight_layout()
plt.show()