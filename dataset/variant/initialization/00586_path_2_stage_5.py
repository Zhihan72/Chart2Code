import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

nodes = [
    'Innovations', 'Revolutions',
    'G. Wright', 'C. Breuer', 'H. Gehry', 'F. Libeskind'
]

edges = [
    ('Innovations', 'Revolutions'),
    ('G. Wright', 'Innovations'),
    ('C. Breuer', 'Innovations'),
    ('H. Gehry', 'Revolutions'),
    ('F. Libeskind', 'Revolutions')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

node_colors = {
    'Innovations': '#1F77B4',
    'Revolutions': '#D62728',
    'G. Wright': '#9467BD',
    'C. Breuer': '#8C564B',
    'H. Gehry': '#FF7F0E',
    'F. Libeskind': '#E377C2'
}

node_sizes = {
    'Innovations': 1500,
    'Revolutions': 1200,
    'G. Wright': 1000,
    'C. Breuer': 1000,
    'H. Gehry': 1000,
    'F. Libeskind': 1000
}

node_shapes = {
    'Innovations': 'v',
    'Revolutions': 'o',
    'G. Wright': '^',
    'C. Breuer': 'D',
    'H. Gehry': 'p',
    'F. Libeskind': 'h'
}

for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=node_colors[node],
        edgecolors='black',
        node_shape=node_shapes[node]
    )

edge_styles = {
    ('Innovations', 'Revolutions'): 'dashdot',
    ('G. Wright', 'Innovations'): 'dashed',
    ('C. Breuer', 'Innovations'): 'solid',
    ('H. Gehry', 'Revolutions'): 'dotted',
    ('F. Libeskind', 'Revolutions'): 'dashdot'
}

for edge in G.edges():
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[edge],
        style=edge_styles.get(edge, 'dotted'),
        width=2,
        edge_color='gray'
    )

nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')

plt.title(
    "Evolutions in Contemporary Design\nConnecting Movements and Innovators",
    fontsize=14, fontweight='bold'
)

handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='lower right')

plt.grid(True, linestyle='--', linewidth=0.5)
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.tight_layout()

plt.show()