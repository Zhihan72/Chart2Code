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

pos = nx.circular_layout(G)

fig, ax = plt.subplots(figsize=(14, 10))

node_colors = ['lightsalmon' if G.nodes[node]['type'] == 'team' else 'royalblue' for node in G.nodes()]
node_sizes = [3500 if G.nodes[node]['type'] == 'team' else 4000 for node in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='gray', linewidths=3, alpha=0.8, node_shape='d')

nx.draw_networkx_edges(G, pos, edgelist=edges, arrows=True, arrowstyle='->', arrowsize=15, width=3.5, edge_color='dimgray', alpha=0.7, style='dashed')

nx.draw_networkx_labels(G, pos, font_size=13, font_weight='normal')

ax.set_title('Dataopolis AI Teams & Projects', fontsize=18, fontweight='normal', ha='center')

team_patch = plt.Line2D([0], [0], marker='d', color='w', label='Teams', markersize=11, markerfacecolor='lightsalmon', markeredgecolor='gray')
project_patch = plt.Line2D([0], [0], marker='s', color='w', label='Projects', markersize=11, markerfacecolor='royalblue', markeredgecolor='gray')
edge_patch = plt.Line2D([0], [0], linestyle='--', color='dimgray', lw=3.5, alpha=0.7, label='Collab')

plt.legend(handles=[team_patch, project_patch, edge_patch], loc='lower left', fontsize=11, title='Legend', title_fontsize=13, frameon=False)

plt.tight_layout()
plt.show()