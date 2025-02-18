import matplotlib.pyplot as plt
import networkx as nx

# Departments in the company
departments = ['R&D', 'Marketing', 'Sales', 'HR', 'Customer Support', 'Finance', 'Operations']

# Communication Intensity Matrix
communication_matrix = [
    [0, 15, 20, 5, 10, 12, 8],   # R&D to others
    [10, 0, 25, 5, 15, 15, 10],  # Marketing to others
    [5, 10, 0, 5, 20, 10, 5],    # Sales to others
    [10, 5, 5, 0, 15, 6, 9],     # HR to others
    [5, 5, 15, 10, 0, 7, 12],    # Customer Support to others
    [10, 15, 20, 8, 5, 0, 15],   # Finance to others
    [5, 10, 10, 5, 15, 15, 0]    # Operations to others
]

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(departments)

for i, source in enumerate(departments):
    for j, target in enumerate(departments):
        if communication_matrix[i][j] > 0:
            G.add_edge(source, target, weight=communication_matrix[i][j])

pos = nx.spring_layout(G, k=0.3, iterations=50)

plt.figure(figsize=(14, 10))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='skyblue')
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_weight='bold')

edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[edge[2]['weight'] * 0.1 for edge in edges], arrowstyle='->', arrowsize=20)

edge_labels = {(source, target): f'{attr["weight"]}' for source, target, attr in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3)

plt.title('Communication Flow in\nGlobeTech Solutions', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()