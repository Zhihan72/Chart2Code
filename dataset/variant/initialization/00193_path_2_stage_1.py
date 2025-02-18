import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
DG = nx.DiGraph()

# Define academic disciplines as nodes
disciplines = [
    "Computer Science", "Mathematics", "Physics", 
    "Biology", "Chemistry", "Economics", 
    "Psychology", "Philosophy"
]

DG.add_nodes_from(disciplines)

# Define the directed edges with weights
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

DG.add_weighted_edges_from(edges_with_weights)

# Define positions using a shell layout
pos = nx.shell_layout(DG)

# Draw nodes with altered color and shape
node_sizes = [600 * DG.out_degree(n) for n in DG.nodes()]
nx.draw_networkx_nodes(DG, pos, node_size=node_sizes, node_color='lightblue', alpha=0.8, node_shape='s')

# Draw directed edges with different line style based on node pair
nx.draw_networkx_edges(DG, pos, edgelist=DG.edges(), 
                       alpha=0.6, edge_color='green', style='dashed', arrows=True, arrowsize=15)

# Draw labels with different font properties
nx.draw_networkx_labels(DG, pos, font_size=12, font_weight='normal', verticalalignment='bottom', font_family='serif')

# Set plot title with different style
plt.title('Interdisciplinary Flow of Knowledge', fontsize=16, weight='bold', loc='left', color='darkred')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Remove axis
plt.axis('on')
plt.tight_layout()

# Display the plot
plt.show()