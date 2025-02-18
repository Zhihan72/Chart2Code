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

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

# Shuffling node colors manually
shuffled_node_colors = {
    'Modernism': '#1F77B4',          # Assigned Brutalism's color
    'Brutalism': '#2CA02C',          # Assigned Deconstructivism's color
    'Deconstructivism': '#E377C2',   # Assigned Rem Koolhaas's color
    'Frank Lloyd Wright': '#8C564B', # Assigned Zaha Hadid's color
    'Le Corbusier': '#D62728',       # Assigned Frank Lloyd Wright's color
    'Zaha Hadid': '#FF7F0E',         # Assigned Modernism's color
    'Rem Koolhaas': '#9467BD'        # Assigned Le Corbusier's color
}

node_sizes = { 'Modernism': 1500, 'Brutalism': 1200, 'Deconstructivism': 1200,
               'Frank Lloyd Wright': 1000, 'Le Corbusier': 1000, 
               'Zaha Hadid': 1000, 'Rem Koolhaas': 1000 }
node_shapes = { 'Modernism': 'o', 'Brutalism': 's', 'Deconstructivism': 'v', 
                'Frank Lloyd Wright': 'p', 'Le Corbusier': 'h', 
                'Zaha Hadid': 'D', 'Rem Koolhaas': '^' }

for node in G.nodes():
    nx.draw_networkx_nodes(
        G, pos,
        nodelist=[node],
        node_size=node_sizes[node],
        node_color=shuffled_node_colors[node],
        edgecolors='black',
        node_shape=node_shapes[node]
    )

edge_styles = {
    ('Modernism', 'Brutalism'): 'solid',
    ('Modernism', 'Deconstructivism'): 'dashed',
    ('Modernism', 'Frank Lloyd Wright'): 'dotted',
    ('Modernism', 'Le Corbusier'): 'dashdot',
    ('Brutalism', 'Le Corbusier'): 'solid',
    ('Deconstructivism', 'Zaha Hadid'): 'dashed',
    ('Deconstructivism', 'Rem Koolhaas'): 'dotted'
}

for edge in G.edges():
    nx.draw_networkx_edges(
        G, pos,
        edgelist=[edge],
        style=edge_styles.get((edge[1], edge[0]), edge_styles[edge]),
        width=2,
        edge_color='gray'
    )

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