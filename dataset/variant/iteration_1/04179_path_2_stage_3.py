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

G = nx.Graph()

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

pos = nx.shell_layout(G)

fig, ax = plt.subplots(figsize=(14, 10))

# Manually shuffling the color assignment
node_colors = ['lightcoral' if G.nodes[node]['type'] == 'team' else 'cornflowerblue' for node in G.nodes()]
node_sizes = [3000 if G.nodes[node]['type'] == 'team' else 4500 for node in G.nodes()]

nx.draw_networkx_nodes(
    G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=2, alpha=0.9
)

nx.draw_networkx_edges(
    G, pos, edgelist=edges, width=2.0, alpha=0.6, edge_color='gray'
)

nx.draw_networkx_labels(
    G, pos, font_size=12, font_weight='bold'
)

ax.set_title(
    'Collaborations in Dataopolis\nAI Teams and Their Projects',
    fontsize=18, fontweight='bold', ha='center'
)

ax.axis('off')

plt.show()