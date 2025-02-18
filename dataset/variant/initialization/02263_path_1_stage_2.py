import matplotlib.pyplot as plt
import networkx as nx

social_media_platforms = ['Snapchat', 'Instagram', 'Facebook', 'LinkedIn', 'Twitter']
tech_brands = ['Microsoft', 'Apple', 'Google', 'Amazon']

edges = [
    ('Twitter', 'Google'),
    ('LinkedIn', 'Microsoft'),
    ('Apple', 'Twitter'),
    ('Instagram', 'Amazon'),
    ('Snapchat', 'Google'),
    ('Facebook', 'Microsoft'),
    ('Facebook', 'Apple'),
    ('Instagram', 'Facebook'),
]

G = nx.Graph()

for node in social_media_platforms:
    G.add_node(node, category='Networking Platforms')
for node in tech_brands:
    G.add_node(node, category='Tech Giants')

G.add_edges_from(edges)

node_colors = ['#1f78b4' if node[1]['category'] == 'Networking Platforms' else '#33a02c' for node in G.nodes(data=True)]
edge_styles = ['solid' if edge[0] in social_media_platforms and edge[1] in social_media_platforms else 'dashed' for edge in G.edges(data=True)]

fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=2500,
    font_size=10, font_weight='bold', edge_color='gray',
    style=edge_styles, width=2
)

plt.title("Connections in Networking\nand Tech Realm", fontsize=16, fontweight='bold', pad=20)

legend_labels = ['Networking Platforms', 'Tech Giants']
legend_colors = ['#1f78b4', '#33a02c']
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in legend_colors]

ax.legend(legend_handles, legend_labels, loc='upper right', title="Node Types", fontsize=11)

plt.tight_layout()
plt.show()