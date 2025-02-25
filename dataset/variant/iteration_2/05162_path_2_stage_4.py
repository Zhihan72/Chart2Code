import matplotlib.pyplot as plt
import networkx as nx

# Define a simple undirected graph
G = nx.Graph()

# Adding nodes (years)
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# Create edges (which could be seen as connections between these years)
edges = [(2010, 2011), (2011, 2012), (2012, 2013), (2013, 2014), 
         (2014, 2015), (2015, 2016), (2016, 2017), (2017, 2018), 
         (2018, 2019), (2019, 2020)]

# Add nodes and edges to the graph
G.add_nodes_from(years)
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=15, edge_color='gray')

plt.title("Undirected Graph of Years", fontsize=18)
plt.show()