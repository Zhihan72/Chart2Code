import matplotlib.pyplot as plt
import networkx as nx

# First series: nodes are years from 2010 to 2021
nodes_1 = list(range(2010, 2022))
edges_1 = [(2010, 2011), (2011, 2012), (2012, 2013), (2013, 2014), (2014, 2015),
           (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]

# Second series: nodes are years from 2022 to 2032
nodes_2 = list(range(2022, 2033))
edges_2 = [(2022, 2023), (2023, 2024), (2024, 2025), (2025, 2026), (2026, 2027),
           (2027, 2028), (2028, 2029), (2029, 2030), (2030, 2031), (2031, 2032)]

# Initialize an undirected graph
G = nx.Graph()

# Add nodes and edges for the first series
G.add_nodes_from(nodes_1)
G.add_edges_from(edges_1)

# Add nodes and edges for the second series
G.add_nodes_from(nodes_2)
G.add_edges_from(edges_2)

# Plot the graph
pos = nx.spring_layout(G)  # Positions for all nodes

plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=700, 
        node_color=['lightblue' if node in nodes_1 else 'lightgreen' for node in G.nodes()],
        font_size=10, font_weight='bold')

# Titles and labels
plt.title('Undirected Graph of Years with Additional Series', fontsize=16, fontweight='bold')

# Show the plot
plt.show()