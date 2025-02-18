import matplotlib.pyplot as plt
import networkx as nx

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
north_region = [50, 60, 70, 85, 95, 105, 130, 145, 160, 180, 200]
south_region = [20, 25, 35, 50, 65, 75, 90, 100, 115, 130, 150]

# Create a graph object
G = nx.Graph()

# Add nodes
G.add_nodes_from(years)

# Add edges with weights corresponding to installations in each region
for i in range(len(years) - 1):
    G.add_edge(years[i], years[i + 1], weight=north_region[i])
    G.add_edge(years[i], years[i + 1], weight=south_region[i])

# Get positions for nodes in circular layout
pos = nx.circular_layout(G)

# Draw the graph with matplotlib
plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='cyan', font_size=10, font_weight='bold')

# Draw edge labels for the north region
edge_labels_north = {(years[i], years[i + 1]): f'N:{north_region[i]}' for i in range(len(years) - 1)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_north, label_pos=0.3, font_color='green', font_size=10)

# Draw edge labels for the south region
edge_labels_south = {(years[i], years[i + 1]): f'S:{south_region[i]}' for i in range(len(years) - 1)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels_south, label_pos=0.7, font_color='blue', font_size=10)

plt.title('Undirected Graph of WindCo Annual Wind Farm Installation Capacity (2010-2020)', fontsize=18, fontweight='bold')
plt.show()