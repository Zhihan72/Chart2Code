import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Define nodes
age_groups = ["Teens", "20s", "30s", "40s", "Seniors"]

# Add nodes
G.add_nodes_from(age_groups)

# Define arbitrary edges
edges = [("Teens", "20s"), ("20s", "30s"), ("30s", "40s"), ("40s", "Seniors"), ("Teens", "Seniors")]

# Add edges
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(8, 8))
nx.draw(G, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='grey')

plt.title('Undirected Graph Chart: Age Groups Connectivity', fontsize=16, fontweight='bold')

plt.show()