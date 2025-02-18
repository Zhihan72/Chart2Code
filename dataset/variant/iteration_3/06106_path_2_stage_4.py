import matplotlib.pyplot as plt
import networkx as nx

age_groups = ['Teens (13-19)', 'Young Adults (20-35)', 'Adults (36-50)', 'Seniors (51+)']
data_by_age_group = {
    'Teens (13-19)': [25, 15, 10, 30, 10, 10],
    'Young Adults (20-35)': [10, 20, 20, 30, 10, 10],
    'Adults (36-50)': [15, 10, 25, 15, 20, 15],
    'Seniors (51+)':[25, 10, 5, 10, 10, 40]
}

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

for i, (_, preferences) in enumerate(data_by_age_group.items()):
    ax = axs[i // 2][i % 2]
    
    # Create an undirected graph
    G = nx.Graph()
    
    # Add nodes (each node represents an index of the preference list)
    nodes = range(len(preferences))
    G.add_nodes_from(nodes)

    # Add edges according to the preference data, assuming similar indices indicate a connection
    for j in nodes:
        for k in range(j + 1, len(preferences)):  # Only connect nodes without direction (undirected)
            if preferences[j] > 0 and preferences[k] > 0:
                G.add_edge(j, k, weight=(preferences[j] + preferences[k]) / 2)
    
    # We draw the undirected graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='#ffcc99', edge_color='#66b3ff', node_size=500)

plt.tight_layout()
plt.show()