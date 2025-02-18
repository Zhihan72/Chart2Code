import matplotlib.pyplot as plt
import networkx as nx

nodes = list(range(2010, 2033))
edges = [
    (2010, 2011), (2011, 2012), (2012, 2013), (2013, 2014), (2014, 2015),
    (2015, 2016), (2016, 2017), (2017, 2018), (2018, 2019), (2019, 2020),
    (2020, 2021), (2022, 2023), (2023, 2024), (2024, 2025), (2025, 2026),
    (2026, 2027), (2027, 2028), (2028, 2029), (2029, 2030), (2030, 2031),
    (2031, 2032)
]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G)

plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10)
plt.show()