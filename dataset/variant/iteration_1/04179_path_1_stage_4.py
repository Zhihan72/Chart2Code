import matplotlib.pyplot as plt
import networkx as nx

teams = ["NLP", "Vision", "Robotics", "Systems", "Security"]
projects = ["Chatbot", "Face Rec", "Self-drive", "Cloud AI", "Secure AI"]

G = nx.DiGraph()

G.add_nodes_from(teams, type='team')
G.add_nodes_from(projects, type='project')

edges = [
    ("NLP", "Chatbot"),
    ("Vision", "Face Rec"),
    ("Vision", "Self-drive"),
    ("Robotics", "Self-drive"),
    ("Robotics", "Cloud AI"),
    ("Systems", "Cloud AI"),
    ("Systems", "Secure AI"),
    ("Security", "Secure AI")
]

G.add_edges_from(edges)

pos = nx.shell_layout(G)

fig, ax = plt.subplots(figsize=(14, 10))

node_colors = ['lightcoral' if G.nodes[node]['type'] == 'team' else 'cornflowerblue' for node in G.nodes()]
node_sizes = [3000 if G.nodes[node]['type'] == 'team' else 4500 for node in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black', linewidths=2, alpha=0.9)

nx.draw_networkx_edges(G, pos, edgelist=edges, arrows=True, arrowstyle='-|>', arrowsize=20, width=2.0, edge_color='gray', alpha=0.6)

nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

ax.set_title('Dataopolis AI Teams & Projects', fontsize=18, fontweight='bold', ha='center')

ax.axis('off')

team_patch = plt.Line2D([0], [0], marker='o', color='w', label='Teams', markersize=10, markerfacecolor='lightcoral', markeredgecolor='black')
project_patch = plt.Line2D([0], [0], marker='s', color='w', label='Projects', markersize=10, markerfacecolor='cornflowerblue', markeredgecolor='black')
edge_patch = plt.Line2D([0], [0], linestyle='-', color='gray', lw=2, alpha=0.6, label='Collab')

plt.legend(handles=[team_patch, project_patch, edge_patch], loc='upper right', fontsize=11, title='Legend', title_fontsize=13)

plt.tight_layout()
plt.show()