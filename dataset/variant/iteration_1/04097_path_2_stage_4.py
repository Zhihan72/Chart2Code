import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.DiGraph()

nodes = [
    'OpenAI', 'DeepMind', 'IBM', 'Microsoft', 'Google',
    'MIT', 'Stanford', 'Facebook', 'Alibaba DAMO',
    'Tencent', 'Baidu', 'NVIDIA'
]

G.add_nodes_from(nodes)

edges = [
    ('Google', 'Facebook'), ('OpenAI', 'Tencent'), ('DeepMind', 'OpenAI'),
    ('IBM', 'Baidu'), ('Microsoft', 'NVIDIA'), ('MIT', 'Google'),
    ('Stanford', 'Microsoft'), ('NVIDIA', 'OpenAI'), ('Facebook', 'MIT'),
    ('Alibaba DAMO', 'Tencent'), ('Tencent', 'IBM'), ('Baidu', 'Alibaba DAMO'),
    ('DeepMind', 'Google'), ('IBM', 'MIT'), ('Microsoft', 'Stanford')
]

G.add_edges_from(edges)

edge_weights = {edge: np.random.randint(1, 10) for edge in G.edges()}

colors = {
    'OpenAI': '#1f77b4', 'DeepMind': '#ff7f0e', 'IBM': '#2ca02c',
    'Microsoft': '#d62728', 'Google': '#9467bd', 'MIT': '#8c564b',
    'Stanford': '#e377c2', 'Facebook': '#7f7f7f', 'Alibaba DAMO': '#bcbd22',
    'Tencent': '#17becf', 'Baidu': '#aec7e8', 'NVIDIA': '#ff9896'
}

pos = nx.circular_layout(G)

fig, ax = plt.subplots(figsize=(10, 10))

# Randomly alter stylistic elements
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=2000,
                       node_color=[colors[node] for node in G.nodes],
                       edgecolors='black', alpha=0.9)  # Changed marker to hexagon
nx.draw_networkx_edges(G, pos, ax=ax,
                       edgelist=G.edges(),
                       width=[edge_weights[edge] for edge in G.edges],
                       edge_color='darkgray', style='dashed', arrowsize=20, arrowstyle='-|>')  # Changed line style to dashed
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold',
                        bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

edge_labels = {edge: str(weight) for edge, weight in edge_weights.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_color='red', font_size=8)

ax.set_title("AI Collaborations\nBetween AI Labs",
             fontsize=16, fontweight='bold', pad=20)
ax.grid(True)  # Added a grid
ax.spines['top'].set_visible(False)  # Modify border visibility by hiding the top spine
ax.spines['right'].set_visible(False)  # Modify border visibility by hiding the right spine
ax.axis('off')

plt.show()