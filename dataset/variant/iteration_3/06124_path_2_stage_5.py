import matplotlib.pyplot as plt
import networkx as nx

age_groups = ["Children", "Teens", "20s", "30s", "40s", "50+", "60+", "Middle-aged"]
data_pairs = [
    (0, 20), (5, 30), (10, 55), (7, 40), (18, 30), (23, 60), (60, 30), (78, 83)
]

# Initialize the graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(age_groups)

# Add edges based on conditions, here simplistically by their endpoints
for (start, end) in data_pairs:
    # Using age group directly here for simplicity, with a trivial condition
    for i, usage in enumerate([start, end]):
        if usage in data_pairs[i]:
            G.add_edge(age_groups[i % len(age_groups)], age_groups[(i+1) % len(age_groups)])

# Create the plot
plt.figure(figsize=(10, 7))
nx.draw(G, with_labels=True, node_color="skyblue", font_weight="bold", node_size=2000, font_size=10)
plt.title('Undirected Graph: Age Groups Internet Usage')
plt.show()