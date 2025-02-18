import matplotlib.pyplot as plt
import networkx as nx

regions = ['Northland', 'Southland', 'Eastland', 'Westland', 'Central', 'Highland', 'Lowland']

# Populate demographic_data (not used in the graph but keeping demographics_labels for the loop)
demographics_labels = ['Children (<18)', 'Adults (18-64)', 'Seniors (65+)']
regional_connections = [
    ('Northland', 'Southland'),
    ('Southland', 'Eastland'),
    ('Eastland', 'Westland'),
    ('Westland', 'Central'),
    ('Central', 'Highland'),
    ('Highland', 'Lowland'),
    ('Lowland', 'Northland')
]

G = nx.Graph()

# Add nodes and edges based on the given connection pairs
G.add_nodes_from(regions)
G.add_edges_from(regional_connections)

fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Create a position layout for nodes (e.g., spring layout)
pos = nx.spring_layout(G, seed=42)

# Draw the graph for each subplot
nx.draw(G, pos, ax=ax[0], with_labels=True, node_color='lightblue', edge_color='grey', node_size=2000, font_weight='bold')
ax[0].set_title('Undirected Graph of Regions', fontsize=14, fontweight='bold')

nx.draw(G, pos, ax=ax[1], with_labels=True, node_color='lightgreen', edge_color='grey', node_size=2000, font_weight='bold')
ax[1].set_title('Regional Connections', fontsize=14, fontweight='bold')

fig.suptitle('Graph Representation of Regional and Demographic Distribution', fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()