import matplotlib.pyplot as plt
import networkx as nx

# Define the graph data: nodes are years, edges represent connections (relation is not relevant)
nodes = list(range(2010, 2021))
edges = [(2010, 2011), (2011, 2012), (2012, 2013), (2013, 2014), (2014, 2015),
         (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]

# Initialize an undirected graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Plot the graph
pos = nx.spring_layout(G)  # Positions for all nodes

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')

# Titles and labels
plt.title('Undirected Graph of Years', fontsize=16, fontweight='bold')

# Show the plot
plt.show()