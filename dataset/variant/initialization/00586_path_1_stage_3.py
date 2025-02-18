import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

nodes = [
    'Modernism', 'Brutalism', 'Deconstructivism',
    'Frank Lloyd Wright', 'Le Corbusier', 'Zaha Hadid', 'Rem Koolhaas'
]

# Manually shuffled edge pairs without using random library
edges = [
    ('Brutalism', 'Le Corbusier'),
    ('Deconstructivism', 'Zaha Hadid'),
    ('Modernism', 'Brutalism'),
    ('Le Corbusier', 'Modernism'),
    ('Deconstructivism', 'Rem Koolhaas'),
    ('Modernism', 'Deconstructivism'),
    ('Frank Lloyd Wright', 'Modernism')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

# Node colors have been shuffled within their group
shuffled_node_colors = {
    'Brutalism': '#1F77B4',
    'Modernism': '#2CA02C',
    'Deconstructivism': '#E377C2',
    'Frank Lloyd Wright': '#8C564B',
    'Le Corbusier': '#9467BD',  # swapped with one below
    'Zaha Hadid': '#D62728',    # swapped with one above
    'Rem Koolhaas': '#FF7F0E'
}

node_sizes = {
    'Rem Koolhaas': 1200, 
    'Brutalism': 1500,  # shuffled within their group
    'Deconstructivism': 1200,
    'Modernism': 1000,
    'Le Corbusier': 1000,
    'Zaha Hadid': 1000,
    'Frank Lloyd Wright': 1000
}

node_shapes = {
    'Modernism': 's',  # shuffled
    'Brutalism': 'o',  # shuffled
    'Deconstructivism': 'v', 
    'Frank Lloyd Wright': 'p', 
    'Rem Koolhaas': 'h',  # swapped with one below
    'Le Corbusier': '^',  # swapped with one above
    'Zaha Hadid': 'D'
}

for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=shuffled_node_colors[node],
        edgecolors='black',
        node_shape=node_shapes[node]
    )

# Alteration of edge styles within the defined group
edge_styles = {
    ('Brutalism', 'Le Corbusier'): 'dashdot',
    ('Deconstructivism', 'Zaha Hadid'): 'solid',
    ('Modernism', 'Brutalism'): 'dotted',
    ('Le Corbusier', 'Modernism'): 'dashed',
    ('Deconstructivism', 'Rem Koolhaas'): 'solid',
    ('Modernism', 'Deconstructivism'): 'dashdot',
    ('Frank Lloyd Wright', 'Modernism'): 'dotted'
}

for edge in G.edges():
    style = edge_styles.get(edge, edge_styles.get((edge[1], edge[0])))
    nx.draw_networkx_edges(G, pos, edgelist=[edge], style=style, width=2, edge_color='gray')

nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')

plt.title(
    "Influences in Modern Architecture\nMapping Styles and Architects",
    fontsize=14, fontweight='bold'
)

handles = [mpatches.Patch(color=shuffled_node_colors[node], label=node) for node in shuffled_node_colors]
plt.legend(handles=handles, loc='upper left', bbox_to_anchor=(1, 1))

plt.axis('off')
plt.tight_layout()
plt.show()