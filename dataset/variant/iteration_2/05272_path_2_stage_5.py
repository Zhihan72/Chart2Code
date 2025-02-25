import matplotlib.pyplot as plt
import networkx as nx

temperature_anomalies_graph_data = [
    ('1970', '1980'),
    ('1980', '1990'),
    ('1990', '2000'),
    ('2000', '2010'),
    ('2010', '2020'),
]

fig, ax = plt.subplots(figsize=(7, 7))

# Temperature anomalies graph plot
G_temp = nx.Graph()
G_temp.add_edges_from(temperature_anomalies_graph_data)
nx.draw(G_temp, with_labels=True, node_color='cyan', ax=ax)
ax.set_title("Temperature Changes (1970-2020)", fontsize=15)

plt.suptitle("Arctic & Mid-latitudes: Climate Change Overview", fontsize=17, fontweight='bold', color='purple', y=0.96)
plt.tight_layout(rect=[0, 0, 1, 0.94])

plt.show()