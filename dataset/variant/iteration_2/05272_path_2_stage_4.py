import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Prepare data points for connecting nodes for each subplot
temperature_anomalies_graph_data = [
    ('1970', '1980'),
    ('1980', '1990'),
    ('1990', '2000'),
    ('2000', '2010'),
    ('2010', '2020'),
]

co2_emissions_graph_data = [
    ('1970', '1980'),
    ('1980', '1990'),
    ('1990', '2000'),
    ('2000', '2010'),
    ('2010', '2020'),
]

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Temperature anomalies graph plot
G_temp = nx.Graph()
G_temp.add_edges_from(temperature_anomalies_graph_data)
nx.draw(G_temp, with_labels=True, node_color='cyan', ax=axes[0])
axes[0].set_title("Temperature Changes (1970-2020)", fontsize=15)

# CO2 emissions graph plot
G_co2 = nx.Graph()
G_co2.add_edges_from(co2_emissions_graph_data)
nx.draw(G_co2, with_labels=True, node_color='brown', ax=axes[1])
axes[1].set_title("CO2 Emissions (1970-2020)", fontsize=15)

plt.suptitle("Arctic & Mid-latitudes: Climate Change Overview", fontsize=17, fontweight='bold', color='purple', y=0.96)
plt.tight_layout(rect=[0, 0, 1, 0.94])

plt.show()