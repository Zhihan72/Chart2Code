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

# New color set applied to nodes
new_colors = {
    'OpenAI': '#e41a1c', 'DeepMind': '#377eb8', 'IBM': '#4daf4a',
    'Microsoft': '#984ea3', 'Google': '#ff7f00', 'MIT': '#ffff33',
    'Stanford': '#a65628', 'Facebook': '#f781bf', 'Alibaba DAMO': '#999999',
    'Tencent': '#fdb462', 'Baidu': '#b3de69', 'NVIDIA': '#fccde5'
}

pos = nx.circular_layout(G)

fig, ax = plt.subplots(figsize=(10, 10))

nx.draw_networkx_nodes(G, pos, ax=ax, node_size=2000,
                       node_color=[new_colors[node] for node in G.nodes],
                       edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, ax=ax,
                       edgelist=G.edges(),
                       width=[edge_weights[edge] for edge in G.edges],
                       edge_color='darkgray', style='dashed', arrowsize=20, arrowstyle='-|>')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold',
                        bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

edge_labels = {edge: str(weight) for edge, weight in edge_weights.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_color='red', font_size=8)

ax.set_title("AI Collaborations\nBetween AI Labs",
             fontsize=16, fontweight='bold', pad=20)
ax.grid(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.axis('off')

plt.show()