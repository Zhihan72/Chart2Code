# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

# Define AI teams (nodes) and projects they work on
teams = [
    "NLP Team", "Vision Team", "Robotics Team", 
    "Ethics Team", "Systems Team", "Security Team",
    "Data Team", "AI Research Team"
]
projects = [
    "Chatbot", "Face Recognition", "Self-driving Car", 
    "AI Ethics", "Cloud AI", "Secure AI",
    "Data Analysis", "Quantum Computing"
]

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(teams, type='team')
G.add_nodes_from(projects, type='project')

# Define edges showing AI teams' involvement in projects
edges = [
    ("NLP Team", "Chatbot"),
    ("NLP Team", "AI Ethics"),
    ("Vision Team", "Face Recognition"),
    ("Vision Team", "Self-driving Car"),
    ("Robotics Team", "Self-driving Car"),
    ("Robotics Team", "Cloud AI"),
    ("Ethics Team", "AI Ethics"),
    ("Systems Team", "Cloud AI"),
    ("Systems Team", "Secure AI"),
    ("Security Team", "Secure AI"),
    ("Data Team", "Data Analysis"),
    ("AI Research Team", "Quantum Computing"),
    ("Data Team", "Quantum Computing"),
    ("AI Research Team", "Data Analysis")
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions using a layout
pos = nx.shell_layout(G)

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Define node attributes
node_colors = ['cornflowerblue' if G.nodes[node]['type'] == 'team' else 'lightcoral' for node in G.nodes()]
node_sizes = [3000 if G.nodes[node]['type'] == 'team' else 4500 for node in G.nodes()]

# Draw nodes
nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=2, alpha=0.9
)

# Draw edges
nx.draw_networkx_edges(
    G, pos, edgelist=edges, width=2.0, alpha=0.6, edge_color='gray'
)

# Draw node labels
nx.draw_networkx_labels(
    G, pos, font_size=12, font_weight='bold'
)

# Create a title for the graph
ax.set_title(
    'Collaborations in Dataopolis\nAI Teams and Their Projects',
    fontsize=18, fontweight='bold', ha='center'
)

# Remove axis
ax.axis('off')

# Customize legend
team_patch = plt.Line2D(
    [0], [0], marker='o', color='w', label='AI Teams', markersize=10, markerfacecolor='cornflowerblue', markeredgecolor='black'
)
project_patch = plt.Line2D(
    [0], [0], marker='s', color='w', label='Projects', markersize=10, markerfacecolor='lightcoral', markeredgecolor='black'
)
edge_patch = plt.Line2D([0], [0], color='gray', lw=2, alpha=0.6, label='Collaboration')

plt.legend(
    handles=[team_patch, project_patch, edge_patch], loc='upper right', fontsize=11, title='Legend', title_fontsize=13
)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()