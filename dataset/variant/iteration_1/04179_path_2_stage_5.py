import matplotlib.pyplot as plt
import networkx as nx

teams = [
    "NLP Team", "Vision Team", "Robotics Team", 
    "Ethics Team", "Systems Team", "Security Team",
    "Data Team", "AI Research Team"
]
projects = [
    "Chatbot", "Face Recognition", "Self-driving Car", 
    "AI Ethics", "Cloud AI", "Secure AI",
    "Data Analysis", "Quantum Computing"
]

# Create a directed graph instead of an undirected graph
G = nx.DiGraph()

G.add_nodes_from(teams, type='team')
G.add_nodes_from(projects, type='project')

edges = [
    ("NLP Team", "Chatbot"),
    ("NLP Team", "AI Ethics"),
    ("Vision Team", "Face Recognition"),
    ("Vision Team", "Self-driving Car"),
    ("Robotics Team", "Self-driving Car"),
    ("Robotics Team", "Cloud AI"),
    ("Ethics Team", "AI Ethics"),
    ("Systems Team", "Cloud AI"),
    ("Systems Team", "Secure AI"),
    ("Security Team", "Secure AI"),
    ("Data Team", "Data Analysis"),
    ("AI Research Team", "Quantum Computing"),
    ("Data Team", "Quantum Computing"),
    ("AI Research Team", "Data Analysis")
]

G.add_edges_from(edges)

# Use shell_layout but it should still work correctly for a directed graph
pos = nx.shell_layout(G)

fig, ax = plt.subplots(figsize=(14, 10))

node_colors = ['lightcoral' if G.nodes[node]['type'] == 'team' else 'cornflowerblue' for node in G.nodes()]
node_sizes = [3000 if G.nodes[node]['type'] == 'team' else 4500 for node in G.nodes()]

nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=2, alpha=0.9
)

# Use draw_networkx_edges method with arrows option enabled
nx.draw_networkx_edges(
    G, pos, edgelist=edges, width=2.0, alpha=0.6, edge_color='gray', arrows=True
)

nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

ax.axis('off')
plt.show()