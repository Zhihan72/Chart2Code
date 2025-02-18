import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Create a graph representing the innovation and knowledge sharing network in the AI research realm
G = nx.DiGraph()

# Define the AI research labs and organizations as nodes
nodes = [
    'OpenAI', 'DeepMind', 'IBM Watson', 'Microsoft Research', 'Google AI',
    'MIT AI Lab', 'Stanford AI', 'Facebook AI', 'Alibaba DAMO Academy',
    'Tencent AI Lab', 'Baidu AI', 'NVIDIA AI Lab'
]

G.add_nodes_from(nodes)

# Define the edges representing the collaborative and knowledge-sharing connections
edges = [
    ('OpenAI', 'MIT AI Lab'), ('DeepMind', 'Google AI'), ('IBM Watson', 'Microsoft Research'),
    ('Microsoft Research', 'Facebook AI'), ('Google AI', 'Stanford AI'),
    ('MIT AI Lab', 'Stanford AI'), ('Stanford AI', 'NVIDIA AI Lab'), ('Facebook AI', 'MIT AI Lab'),
    ('Alibaba DAMO Academy', 'Tencent AI Lab'), ('Tencent AI Lab', 'Baidu AI'),
    ('Baidu AI', 'Alibaba DAMO Academy'), ('NVIDIA AI Lab', 'OpenAI'),
    ('NVIDIA AI Lab', 'IBM Watson'), ('DeepMind', 'OpenAI'), ('IBM Watson', 'Tencent AI Lab')
]

G.add_edges_from(edges)

# Assign random weights to the edges representing the strength of collaboration
edge_weights = {edge: np.random.randint(1, 10) for edge in G.edges()}

# Define node colors representing different research fields within AI
colors = {
    'OpenAI': '#1f77b4', 'DeepMind': '#ff7f0e', 'IBM Watson': '#2ca02c',
    'Microsoft Research': '#d62728', 'Google AI': '#9467bd', 'MIT AI Lab': '#8c564b',
    'Stanford AI': '#e377c2', 'Facebook AI': '#7f7f7f', 'Alibaba DAMO Academy': '#bcbd22',
    'Tencent AI Lab': '#17becf', 'Baidu AI': '#aec7e8', 'NVIDIA AI Lab': '#ff9896'
}

# Choose a circular layout for better visualization
pos = nx.circular_layout(G)

# Create subplots for different visual representations
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# Plot the directed network graph on the first subplot
nx.draw_networkx_nodes(G, pos, ax=axes[0], node_size=2000,
                       node_color=[colors[node] for node in G.nodes],
                       edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, ax=axes[0],
                       edgelist=G.edges(),
                       width=[edge_weights[edge] for edge in G.edges],
                       edge_color='darkgray', arrowsize=20, arrowstyle='-|>')
nx.draw_networkx_labels(G, pos, ax=axes[0], font_size=10, font_weight='bold',
                        bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

# Annotate edge weights in the graph
edge_labels = {edge: str(weight) for edge, weight in edge_weights.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=axes[0], font_color='red', font_size=8)

axes[0].set_title("AI Research Collaboration Network\n"
                  "Strength of Collaborations between Leading AI Labs",
                  fontsize=16, fontweight='bold', pad=20)
axes[0].axis('off')

# Generate data for a bar chart showing institution collaboration strength
node_labels = list(G.nodes)
collaboration_strength = [sum(edge_weights[(u, v)] for u, v in G.edges(node)) for node in G.nodes]
bar_colors = [colors[node] for node in node_labels]

axes[1].barh(node_labels, collaboration_strength, color=bar_colors)
axes[1].set_title("Collaborative Strength Among AI Labs\n"
                  "Total Collaboration Strength per AI Lab",
                  fontsize=16, fontweight='bold', pad=20)
axes[1].set_xlabel('Total Collaboration Strength', fontsize=14)
axes[1].set_ylabel('AI Labs', fontsize=14)
axes[1].invert_yaxis()  # Invert y-axis for better readability

# Automatically adjust the layout for better spacing
plt.tight_layout()
plt.show()