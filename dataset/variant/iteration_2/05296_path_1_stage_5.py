import matplotlib.pyplot as plt
import networkx as nx

age_groups = [
    'Youths (10-22)', 
    'Gen Z (23-28)', 
    'Millennials (29-38)', 
    'Gen X (39-53)', 
    'Boomers (54-70)', 
    'Elders (71+)'
]

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

step_counts = [
    [13000, 15500, 14500, 12500, 14000, 20500, 19000],
    [11200, 9000, 13500, 12800, 12500, 14000, 13200],
    [10000, 9600, 11000, 11800, 11000, 12500, 12000],
    [8500, 9000, 9400, 10000, 9500, 10700, 9800],
    [7600, 7200, 7500, 7300, 7400, 8100, 7900],
    [5200, 5300, 5000, 4950, 4900, 6050, 6000]
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
nx.draw(G, pos, with_labels=True, node_size=1800, node_color='skyblue', font_size=9, font_color='black')
nx.draw_networkx_edges(G, pos, width=2, edge_color='darkgreen', style='dotted')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
plt.xticks([])
plt.yticks([])
plt.title("Exploring Steps Count Based on Age Ranges and Weekdays", fontsize=15, fontweight='normal', pad=15)

plt.show()