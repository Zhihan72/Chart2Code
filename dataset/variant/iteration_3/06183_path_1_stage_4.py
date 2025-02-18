import matplotlib.pyplot as plt
import networkx as nx

nodes_1 = list(range(2010, 2022))
edges_1 = [(2010, 2011), (2011, 2012), (2012, 2013), (2013, 2014), (2014, 2015),
           (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021)]

nodes_2 = list(range(2022, 2033))
edges_2 = [(2022, 2023), (2023, 2024), (2024, 2025), (2025, 2026), (2026, 2027),
           (2027, 2028), (2028, 2029), (2029, 2030), (2030, 2031), (2031, 2032)]

G = nx.Graph()
G.add_nodes_from(nodes_1)
G.add_edges_from(edges_1)
G.add_nodes_from(nodes_2)
G.add_edges_from(edges_2)

pos = nx.spring_layout(G)

plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=700,
        node_color=['lightblue' if node in nodes_1 else 'lightgreen' for node in G.nodes()],
        font_size=10)
plt.show()