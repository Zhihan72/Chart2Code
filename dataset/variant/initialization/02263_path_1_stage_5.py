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

# Shuffle the assigned colors for the data group
# Swapped the colors for 'Networking Platforms' and 'Tech Giants'
node_colors = ['#33a02c' if node[1]['category'] == 'Networking Platforms' else '#1f78b4' for node in G.nodes(data=True)]

fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos, with_labels=True, node_color=node_colors, node_size=2000,
    font_size=9, font_weight='normal', edge_color='black', width=1.5,
)

plt.title("Networking & Tech Connections", fontsize=14, fontweight='normal', pad=15)

# Update legend colors accordingly
legend_labels = ['Networking', 'Tech']
legend_colors = ['#33a02c', '#1f78b4']
legend_handles = [plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=color, markersize=8) for color in legend_colors]

ax.legend(legend_handles, legend_labels, loc='lower left', title="Categories", fontsize=10)

plt.tight_layout()
plt.show()