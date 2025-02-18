import matplotlib.pyplot as plt
import networkx as nx

age_groups = [
    'Children (5-12)', 
    'Teens (13-19)', 
    'Young Adults (20-29)', 
    'Adults (30-39)', 
    'Middle-aged (40-59)', 
    'Seniors (60+)'
]

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

step_counts = [
    [12000, 15000, 13000, 14000, 14500, 20000, 18000],
    [10000, 11000, 12000, 11500, 11000, 13500, 12500],
    [9500, 10000, 10500, 11000, 10700, 12000, 11700],
    [8000, 8500, 9000, 9500, 9000, 10000, 9500],
    [7500, 7000, 7200, 7100, 7300, 8000, 7800],
    [5000, 5200, 5100, 4900, 4800, 6000, 5900]
]

G = nx.Graph()
G.add_nodes_from(age_groups + days)

for age_idx, age_group in enumerate(age_groups):
    for day_idx, day in enumerate(days):
        weight = step_counts[age_idx][day_idx]
        G.add_edge(age_group, day, weight=weight)

pos = nx.circular_layout(G)
edge_labels = {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)}

plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=1800, node_color='lavender', font_size=9, font_color='darkblue')
nx.draw_networkx_edges(G, pos, width=2, edge_color='darkgreen', style='dashed')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='purple', font_size=8)

plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
plt.xticks([])
plt.yticks([])
plt.title("Average Daily Step Counts Across Age Groups and Days", fontsize=15, fontweight='normal', pad=15)

plt.show()