import matplotlib.pyplot as plt
import networkx as nx

# Define a single color for all nodes
consistent_color = '#ff7f0e'  # Using a different color (e.g., orange)

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

for node in social_media + tech:
    G.add_node(node)

G.add_edges_from(edges)

# Apply the same color to all nodes
node_colors = [consistent_color] * len(G)

edge_styles = ['solid' if (edge[0] in social_media and edge[1] in social_media) else 'dashed' for edge in G.edges(data=True)]

fig, ax = plt.subplots(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=2500,
    font_size=10, font_weight='bold', edge_color='gray',
    style=edge_styles, width=2
)

plt.tight_layout()
plt.show()