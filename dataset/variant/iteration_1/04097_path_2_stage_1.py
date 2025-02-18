import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.DiGraph()

nodes = [
    'OpenAI', 'DeepMind', 'IBM Watson', 'Microsoft Research', 'Google AI',
    'MIT AI Lab', 'Stanford AI', 'Facebook AI', 'Alibaba DAMO Academy',
    'Tencent AI Lab', 'Baidu AI', 'NVIDIA AI Lab'
]

G.add_nodes_from(nodes)

edges = [
    ('OpenAI', 'MIT AI Lab'), ('DeepMind', 'Google AI'), ('IBM Watson', 'Microsoft Research'),
    ('Microsoft Research', 'Facebook AI'), ('Google AI', 'Stanford AI'),
    ('MIT AI Lab', 'Stanford AI'), ('Stanford AI', 'NVIDIA AI Lab'), ('Facebook AI', 'MIT AI Lab'),
    ('Alibaba DAMO Academy', 'Tencent AI Lab'), ('Tencent AI Lab', 'Baidu AI'),
    ('Baidu AI', 'Alibaba DAMO Academy'), ('NVIDIA AI Lab', 'OpenAI'),
    ('NVIDIA AI Lab', 'IBM Watson'), ('DeepMind', 'OpenAI'), ('IBM Watson', 'Tencent AI Lab')
]

G.add_edges_from(edges)

edge_weights = {edge: np.random.randint(1, 10) for edge in G.edges()}

colors = {
    'OpenAI': '#1f77b4', 'DeepMind': '#ff7f0e', 'IBM Watson': '#2ca02c',
    'Microsoft Research': '#d62728', 'Google AI': '#9467bd', 'MIT AI Lab': '#8c564b',
    'Stanford AI': '#e377c2', 'Facebook AI': '#7f7f7f', 'Alibaba DAMO Academy': '#bcbd22',
    'Tencent AI Lab': '#17becf', 'Baidu AI': '#aec7e8', 'NVIDIA AI Lab': '#ff9896'
}

pos = nx.circular_layout(G)

fig, ax = plt.subplots(figsize=(10, 10))

nx.draw_networkx_nodes(G, pos, ax=ax, node_size=2000,
                       node_color=[colors[node] for node in G.nodes],
                       edgecolors='black', alpha=0.9)
nx.draw_networkx_edges(G, pos, ax=ax,
                       edgelist=G.edges(),
                       width=[edge_weights[edge] for edge in G.edges],
                       edge_color='darkgray', arrowsize=20, arrowstyle='-|>')
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10, font_weight='bold',
                        bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

edge_labels = {edge: str(weight) for edge, weight in edge_weights.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_color='red', font_size=8)

ax.set_title("AI Research Collaboration Network\n"
             "Strength of Collaborations between Leading AI Labs",
             fontsize=16, fontweight='bold', pad=20)
ax.axis('off')

plt.show()