import matplotlib.pyplot as plt
import networkx as nx

# Age groups
age_groups = [
    'Children (5-12)', 
    'Teens (13-19)', 
    'Young Adults (20-29)', 
    'Adults (30-39)', 
    'Middle-aged (40-59)', 
    'Seniors (60+)'
]

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Average daily step counts for each age group over a week
step_counts = [
    [12000, 15000, 13000, 14000, 14500, 20000, 18000],  # Children
    [10000, 11000, 12000, 11500, 11000, 13500, 12500],  # Teens
    [9500, 10000, 10500, 11000, 10700, 12000, 11700],   # Young Adults
    [8000, 8500, 9000, 9500, 9000, 10000, 9500],        # Adults
    [7500, 7000, 7200, 7100, 7300, 8000, 7800],         # Middle-aged
    [5000, 5200, 5100, 4900, 4800, 6000, 5900]          # Seniors
]

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(age_groups + days)

# Add edges with step counts as weights
for age_idx, age_group in enumerate(age_groups):
    for day_idx, day in enumerate(days):
        weight = step_counts[age_idx][day_idx]
        G.add_edge(age_group, day, weight=weight)

# Plot the graph
pos = nx.spring_layout(G)  # Positioning the nodes using spring layout
edge_labels = {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)}

plt.figure(figsize=(14, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Undirected Graph of Average Daily Step Counts\nAmong Different Age Groups and Days", fontsize=16, fontweight='bold', pad=20)
plt.show()