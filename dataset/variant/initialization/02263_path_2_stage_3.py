import matplotlib.pyplot as plt
import networkx as nx

# Groups and connections
social_media = ['Snap', 'FB', 'Twit', 'Insta', 'Link']
tech = ['Appl', 'MS', 'Goog', 'Amzn']

edges = [
    ('Snap', 'FB'),
    ('Snap', 'MS'),
    ('FB', 'Amzn'),
    ('Twit', 'Goog'),
    ('Insta', 'Goog'),
    ('Link', 'MS'),
    ('Amzn', 'Twit'),
    ('Appl', 'Snap'),
]

G = nx.Graph()

for node in social_media:
    G.add_node(node, category='SM')
for node in tech:
    G.add_node(node, category='Tech')

G.add_edges_from(edges)

node_colors = ['#1f78b4' if node[1]['category'] == 'SM' else '#33a02c' for node in G.nodes(data=True)]

edge_styles = ['solid' if (edge[0] in social_media and edge[1] in social_media) else 'dashed' for edge in G.edges(data=True)]

fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=2500,
    font_size=10, font_weight='bold', edge_color='gray',
    style=edge_styles, width=2
)

plt.title("Connections in SM & Tech", fontsize=16, fontweight='bold', pad=20)

legend_labels = ['SM', 'Tech']
legend_colors = ['#1f78b4', '#33a02c']
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in legend_colors]

ax.legend(legend_handles, legend_labels, loc='upper right', title="Categories", fontsize=11)

plt.tight_layout()
plt.show()