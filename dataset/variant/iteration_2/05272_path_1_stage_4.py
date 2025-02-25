import matplotlib.pyplot as plt
import networkx as nx

# Create a list of years as nodes
years = [1970, 1980, 1990, 2000, 2010, 2020]

# Data values that act as edges (anomalies connecting the years)
temperature_anomalies_polar = [(-0.3, 0.1), (0.1, 0.5), (0.5, 1.2), (1.2, 1.8), (1.8, 2.5)]
temperature_anomalies_temperate = [(-0.2, 0.2), (0.2, 0.6), (0.6, 1.0), (1.0, 1.4), (1.4, 1.9)]
temperature_anomalies_tropical = [(-0.1, 0.3), (0.3, 0.7), (0.7, 1.2), (1.2, 1.5), (1.5, 2.1)]
temperature_anomalies_desert = [(-0.5, 0.0), (0.0, 0.4), (0.4, 0.9), (0.9, 1.3), (1.3, 1.7)]

# Initialize graphs for each temperature zone
G_polar = nx.Graph()
G_temperate = nx.Graph()
G_tropical = nx.Graph()
G_desert = nx.Graph()

# Add nodes and edges to the graphs
G_polar.add_nodes_from(years)
G_temperate.add_nodes_from(years)
G_tropical.add_nodes_from(years)
G_desert.add_nodes_from(years)

# Add the edges between the nodes based on temperature anomalies
G_polar.add_edges_from([(years[i], years[i+1]) for i, _ in enumerate(temperature_anomalies_polar)])
G_temperate.add_edges_from([(years[i], years[i+1]) for i, _ in enumerate(temperature_anomalies_temperate)])
G_tropical.add_edges_from([(years[i], years[i+1]) for i, _ in enumerate(temperature_anomalies_tropical)])
G_desert.add_edges_from([(years[i], years[i+1]) for i, _ in enumerate(temperature_anomalies_desert)])

# Create the plot
fig, ax = plt.subplots(figsize=(7, 7))

# Draw graphs on the same plot
nx.draw(G_polar, pos=nx.spring_layout(G_polar), node_color='b', edge_color='b', with_labels=True, ax=ax, label='Polar')
nx.draw(G_temperate, pos=nx.spring_layout(G_temperate), node_color='g', edge_color='g', with_labels=True, ax=ax, label='Temperate')
nx.draw(G_tropical, pos=nx.spring_layout(G_tropical), node_color='r', edge_color='r', with_labels=True, ax=ax, label='Tropical')
nx.draw(G_desert, pos=nx.spring_layout(G_desert), node_color='y', edge_color='y', with_labels=True, ax=ax, label='Desert')

# Title and adjustments
plt.title("Undirected Graph of Temperature Zones", fontsize=16)
plt.suptitle("Climate Study: Temp in Zones", fontsize=18, fontweight='bold', y=0.95)
plt.legend(loc="upper left")
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()