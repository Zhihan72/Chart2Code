import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
edges = [(2010, 2011), (2011, 2012), (2012, 2013), (2013, 2014), 
         (2014, 2015), (2015, 2016), (2016, 2017), (2017, 2018), 
         (2018, 2019), (2019, 2020)]

G.add_nodes_from(years)
G.add_edges_from(edges)

plt.figure(figsize=(12, 8))
nx.draw(
    G, 
    with_labels=True, 
    node_color='lightgreen', 
    node_size=1000, 
    font_size=12, 
    font_color='navy', 
    edge_color='orange',
    style='dashed',
    linewidths=2, 
    font_weight='bold'
)

plt.title("Creative Graph of Years", fontsize=20, fontweight='bold', color='purple')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()