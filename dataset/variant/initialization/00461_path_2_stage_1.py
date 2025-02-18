import matplotlib.pyplot as plt
import networkx as nx

departments = ['R&D', 'Marketing', 'Sales', 'HR', 'Customer Support']
communication_matrix = [
    [0, 15, 20, 5, 10],
    [10, 0, 25, 5, 15],
    [5, 10, 0, 5, 20],
    [10, 5, 5, 0, 15],
    [5, 5, 15, 10, 0]
]

G = nx.DiGraph()
G.add_nodes_from(departments)

for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if communication_matrix[i][j] > 0:
            G.add_edge(source, target, weight=communication_matrix[i][j])

pos = nx.spring_layout(G, k=0.3, iterations=50)
plt.figure(figsize=(12, 8))

# Randomly alter stylistic elements
line_styles = ['-', '--', '-.', ':']
marker_styles = ['o', 's', '^', 'p', '*']
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink']

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=colors[0])
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

edges = G.edges(data=True)
nx.draw_networkx_edges(
    G, pos, edgelist=edges,
    width=[edge[2]['weight'] * 0.1 for edge in edges],
    arrowstyle='->', arrowsize=20,
    style=line_styles[1]
)

edge_labels = {(source, target): f'{attr["weight"]}' for source, target, attr in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)

plt.title('Communication Flow in\nGlobeTech Solutions', fontsize=16, fontweight='bold', pad=20)
plt.grid(True, linestyle=line_styles[2])  # Add grid with random line style

plt.axis('off')
plt.tight_layout()
plt.show()