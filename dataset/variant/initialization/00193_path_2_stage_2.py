import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Define academic disciplines as nodes
disciplines = [
    "Computer Science", "Mathematics", "Physics", 
    "Biology", "Chemistry", "Economics", 
    "Psychology", "Philosophy"
]

G.add_nodes_from(disciplines)

# Define the undirected edges with weights
edges_with_weights = [
    ("Computer Science", "Mathematics", 8),
    ("Mathematics", "Physics", 9),
    ("Physics", "Chemistry", 6),
    ("Biology", "Chemistry", 5),
    ("Biology", "Psychology", 7),
    ("Psychology", "Philosophy", 4),
    ("Economics", "Psychology", 3),
    ("Philosophy", "Economics", 2),
    ("Physics", "Biology", 4),
    ("Computer Science", "Physics", 6),
    ("Chemistry", "Biology", 3)
]

G.add_weighted_edges_from(edges_with_weights)

# Define positions using a shell layout
pos = nx.shell_layout(G)

# Draw nodes with color and shape
node_sizes = [600 * G.degree(n) for n in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightblue', alpha=0.8, node_shape='s')

# Draw undirected edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), 
                       alpha=0.6, edge_color='green', style='dashed')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='normal', verticalalignment='bottom', font_family='serif')

# Set plot title
plt.title('Interdisciplinary Connections of Knowledge', fontsize=16, weight='bold', loc='left', color='darkred')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Remove axis
plt.axis('on')
plt.tight_layout()

# Display the plot
plt.show()