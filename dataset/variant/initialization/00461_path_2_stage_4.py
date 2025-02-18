import matplotlib.pyplot as plt
import networkx as nx

departments = ['R&D', 'Marketing', 'Sales', 'Customer Support']
communication_matrix = [
    [0, 15, 20, 10],
    [10, 0, 25, 15],
    [5, 10, 0, 20],
    [5, 5, 15, 0]
]

G = nx.Graph()  # Changed to nx.Graph for an undirected graph
G.add_nodes_from(departments)

for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if i < j and communication_matrix[i][j] + communication_matrix[j][i] > 0:  # Ensure each edge is only counted once
            total_weight = communication_matrix[i][j] + communication_matrix[j][i]
            G.add_edge(source, target, weight=total_weight)

pos = nx.spring_layout(G, k=0.3, iterations=50)
plt.figure(figsize=(12, 8))

colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightpink']

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=colors[0])

edges = G.edges(data=True)
nx.draw_networkx_edges(
    G, pos, edgelist=edges,
    width=[edge[2]['weight'] * 0.1 for edge in edges],
    style='--'  # Retained the linestyle
)

plt.axis('off')
plt.tight_layout()
plt.show()