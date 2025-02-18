import matplotlib.pyplot as plt
import networkx as nx

# Updated departments list without 'HR'
departments = ['R&D', 'Marketing', 'Sales', 'Customer Support']
# Updated communication matrix without the 'HR' row and column
communication_matrix = [
    [0, 15, 20, 10],
    [10, 0, 25, 15],
    [5, 10, 0, 20],
    [5, 5, 15, 0]
]

G = nx.DiGraph()
G.add_nodes_from(departments)

for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if communication_matrix[i][j] > 0:
            G.add_edge(source, target, weight=communication_matrix[i][j])

pos = nx.spring_layout(G, k=0.3, iterations=50)
plt.figure(figsize=(12, 8))

# Reuse stylistic elements
line_styles = ['-', '--', '-.', ':']
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightpink']  # Adjusted colors due to fewer nodes

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=colors[0])

edges = G.edges(data=True)
nx.draw_networkx_edges(
    G, pos, edgelist=edges,
    width=[edge[2]['weight'] * 0.1 for edge in edges],
    arrowstyle='->', arrowsize=20,
    style=line_styles[1]
)

plt.axis('off')
plt.tight_layout()
plt.show()