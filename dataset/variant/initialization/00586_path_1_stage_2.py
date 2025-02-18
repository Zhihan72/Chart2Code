import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

nodes = [
    'Modernism', 'Brutalism', 'Deconstructivism',
    'Frank Lloyd Wright', 'Le Corbusier', 'Zaha Hadid', 'Rem Koolhaas'
]

edges = [
    ('Modernism', 'Brutalism'),
    ('Modernism', 'Deconstructivism'),
    ('Frank Lloyd Wright', 'Modernism'),
    ('Le Corbusier', 'Modernism'),
    ('Le Corbusier', 'Brutalism'),
    ('Zaha Hadid', 'Deconstructivism'),
    ('Rem Koolhaas', 'Deconstructivism')
]

G = nx.Graph()  # Changed from DiGraph to Graph to make it undirected
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

# Node colors are manually assigned
shuffled_node_colors = {
    'Modernism': '#1F77B4', 
    'Brutalism': '#2CA02C',
    'Deconstructivism': '#E377C2',
    'Frank Lloyd Wright': '#8C564B',
    'Le Corbusier': '#D62728',
    'Zaha Hadid': '#FF7F0E',
    'Rem Koolhaas': '#9467BD'
}

node_sizes = {
    'Modernism': 1500, 'Brutalism': 1200, 'Deconstructivism': 1200,
    'Frank Lloyd Wright': 1000, 'Le Corbusier': 1000, 
    'Zaha Hadid': 1000, 'Rem Koolhaas': 1000
}

node_shapes = {
    'Modernism': 'o', 'Brutalism': 's', 'Deconstructivism': 'v', 
    'Frank Lloyd Wright': 'p', 'Le Corbusier': 'h', 
    'Zaha Hadid': 'D', 'Rem Koolhaas': '^'
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

# Edge styles get adjusted only based on the key since the graph is undirected
edge_styles = {
    ('Modernism', 'Brutalism'): 'solid',
    ('Modernism', 'Deconstructivism'): 'dashed',
    ('Frank Lloyd Wright', 'Modernism'): 'dotted',
    ('Le Corbusier', 'Modernism'): 'dashdot',
    ('Brutalism', 'Le Corbusier'): 'solid',
    ('Deconstructivism', 'Zaha Hadid'): 'dashed',
    ('Deconstructivism', 'Rem Koolhaas'): 'dotted'
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