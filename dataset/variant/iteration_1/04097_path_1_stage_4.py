import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = [
    'OpenAI', 'DeepMind', 'IBM', 'Microsoft', 'Google AI',
    'MIT', 'Stanford', 'Facebook', 'Alibaba DAMO',
    'Tencent', 'Baidu', 'NVIDIA'
]

G.add_nodes_from(nodes)

edges = [
    ('OpenAI', 'MIT'), ('DeepMind', 'Google AI'), ('IBM', 'Microsoft'),
    ('Microsoft', 'Facebook'), ('Google AI', 'Stanford'),
    ('MIT', 'Stanford'), ('Stanford', 'NVIDIA'), ('Facebook', 'MIT'),
    ('Alibaba DAMO', 'Tencent'), ('Tencent', 'Baidu'),
    ('Baidu', 'Alibaba DAMO'), ('NVIDIA', 'OpenAI'),
    ('NVIDIA', 'IBM'), ('DeepMind', 'OpenAI'), ('IBM', 'Tencent')
]

G.add_edges_from(edges)

edge_weights = {tuple(sorted(edge)): (i+1) for i, edge in enumerate(G.edges())}

colors = {
    'OpenAI': '#1f77b4', 'DeepMind': '#ff7f0e', 'IBM': '#2ca02c',
    'Microsoft': '#d62728', 'Google AI': '#9467bd', 'MIT': '#8c564b',
    'Stanford': '#e377c2', 'Facebook': '#7f7f7f', 'Alibaba DAMO': '#bcbd22',
    'Tencent': '#17becf', 'Baidu': '#aec7e8', 'NVIDIA': '#ff9896'
}

pos = nx.circular_layout(G)

plt.figure(figsize=(10, 10))

nx.draw_networkx_nodes(
    G, pos, node_size=2000,
    node_color=[colors[node] for node in G.nodes],
    edgecolors='black', alpha=0.9
)
nx.draw_networkx_edges(
    G, pos, edgelist=G.edges(),
    width=[edge_weights[tuple(sorted(edge))] for edge in G.edges()],
    edge_color='darkgray'
)
nx.draw_networkx_labels(
    G, pos, font_size=10, font_weight='bold'
)

plt.axis('off')
plt.tight_layout()
plt.show()