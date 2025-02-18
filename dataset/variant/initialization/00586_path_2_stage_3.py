import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

nodes = [
    'Modernism', 'Deconstructivism',
    'Frank Lloyd Wright', 'Le Corbusier', 'Zaha Hadid', 'Rem Koolhaas'
]

edges = [
    ('Modernism', 'Deconstructivism'),
    ('Frank Lloyd Wright', 'Modernism'),
    ('Le Corbusier', 'Modernism'),
    ('Zaha Hadid', 'Deconstructivism'),
    ('Rem Koolhaas', 'Deconstructivism')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

node_colors = {
    'Modernism': '#1F77B4',
    'Deconstructivism': '#D62728',
    'Frank Lloyd Wright': '#9467BD',
    'Le Corbusier': '#8C564B',
    'Zaha Hadid': '#FF7F0E',
    'Rem Koolhaas': '#E377C2'
}

node_sizes = {
    'Modernism': 1500,
    'Deconstructivism': 1200,
    'Frank Lloyd Wright': 1000,
    'Le Corbusier': 1000,
    'Zaha Hadid': 1000,
    'Rem Koolhaas': 1000
}

node_shapes = {
    'Modernism': 'o',
    'Deconstructivism': 'v',
    'Frank Lloyd Wright': 'p',
    'Le Corbusier': 'h',
    'Zaha Hadid': 'D',
    'Rem Koolhaas': '^'
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
    ('Modernism', 'Deconstructivism'): 'dashed',
    ('Frank Lloyd Wright', 'Modernism'): 'dotted',
    ('Le Corbusier', 'Modernism'): 'dashdot',
    ('Zaha Hadid', 'Deconstructivism'): 'dashed',
    ('Rem Koolhaas', 'Deconstructivism'): 'dotted'
}

for edge in G.edges():
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[edge],
        style=edge_styles.get(edge, 'solid'),
        width=2,
        edge_color='gray'
    )

nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')

plt.title(
    "Influences in Modern Architecture\nMapping Styles and Architects",
    fontsize=14, fontweight='bold'
)

handles = [mpatches.Patch(color=node_colors[node], label=node) for node in node_colors]
plt.legend(handles=handles, loc='upper left', bbox_to_anchor=(1, 1))

plt.axis('off')
plt.tight_layout()

plt.show()