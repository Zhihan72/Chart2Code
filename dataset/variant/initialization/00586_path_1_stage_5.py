import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    'Postmodernism', 'Minimalism', 'Futurism',
    'Frank Gehry', 'Mies van der Rohe', 'Tadao Ando', 'Bjarke Ingels'
]

edges = [
    ('Minimalism', 'Mies van der Rohe'),
    ('Futurism', 'Tadao Ando'),
    ('Postmodernism', 'Minimalism'),
    ('Mies van der Rohe', 'Postmodernism'),
    ('Futurism', 'Bjarke Ingels'),
    ('Postmodernism', 'Futurism'),
    ('Frank Gehry', 'Postmodernism')
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)

shuffled_node_colors = {
    'Minimalism': '#1F77B4',
    'Postmodernism': '#2CA02C',
    'Futurism': '#E377C2',
    'Frank Gehry': '#8C564B',
    'Mies van der Rohe': '#9467BD',
    'Tadao Ando': '#D62728',
    'Bjarke Ingels': '#FF7F0E'
}

node_sizes = {
    'Bjarke Ingels': 1200,
    'Minimalism': 1500,
    'Futurism': 1200,
    'Postmodernism': 1000,
    'Mies van der Rohe': 1000,
    'Tadao Ando': 1000,
    'Frank Gehry': 1000
}

node_shapes = {
    'Postmodernism': 's',
    'Minimalism': 'o',
    'Futurism': 'v',
    'Frank Gehry': 'p',
    'Bjarke Ingels': 'h',
    'Mies van der Rohe': '^',
    'Tadao Ando': 'D'
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

edge_styles = {
    ('Minimalism', 'Mies van der Rohe'): 'dashdot',
    ('Futurism', 'Tadao Ando'): 'solid',
    ('Postmodernism', 'Minimalism'): 'dotted',
    ('Mies van der Rohe', 'Postmodernism'): 'dashed',
    ('Futurism', 'Bjarke Ingels'): 'solid',
    ('Postmodernism', 'Futurism'): 'dashdot',
    ('Frank Gehry', 'Postmodernism'): 'dotted'
}

for edge in G.edges():
    style = edge_styles.get(edge, edge_styles.get((edge[1], edge[0])))
    nx.draw_networkx_edges(G, pos, edgelist=[edge], style=style, width=2, edge_color='gray')

nx.draw_networkx_labels(G, pos, font_size=9, font_family='sans-serif')

plt.axis('off')
plt.tight_layout()
plt.show()