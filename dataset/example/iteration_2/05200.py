import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes in the fantasy realm
nodes = [
    "Elven Forest", "Dwarven Mines", "Human Kingdom",
    "Orc Camp", "Wizard Tower", "Goblin Lair",
    "Dragon's Den", "Necromancer's Crypt"
]

# Define the directed edges representing alliances and conflicts
edges = {
    ("Elven Forest", "Human Kingdom"): {'relation': 'Alliance', 'weight': 5},
    ("Dwarven Mines", "Human Kingdom"): {'relation': 'Alliance', 'weight': 4},
    ("Human Kingdom", "Orc Camp"): {'relation': 'Conflict', 'weight': 6},
    ("Wizard Tower", "Elven Forest"): {'relation': 'Alliance', 'weight': 3},
    ("Goblin Lair", "Orc Camp"): {'relation': 'Ally', 'weight': 4},
    ("Dragon's Den", "Necromancer's Crypt"): {'relation': 'Neutral', 'weight': 2},
    ("Necromancer's Crypt", "Human Kingdom"): {'relation': 'Conflict', 'weight': 5},
    ("Human Kingdom", "Goblin Lair"): {'relation': 'Conflict', 'weight': 3}
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
for (start, end), attrs in edges.items():
    G.add_edge(start, end, **attrs)

# Define positions for each node using a circular layout
pos = nx.spring_layout(G, seed=42)

# Create the plot
plt.figure(figsize=(14, 10))

# Colors for different relations
colors = {
    'Alliance': 'green',
    'Conflict': 'red',
    'Ally': 'blue',
    'Neutral': 'grey'
}

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='#FFD700', edgecolors='black')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw edges and edge labels
for (start, end), attrs in edges.items():
    nx.draw_networkx_edges(G, pos, edgelist=[(start, end)], arrowstyle='->', arrowsize=20, width=2, edge_color=colors[attrs['relation']])
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(start, end): attrs['relation']}, font_color='black')

# Chart Title
plt.title("Interconnections and Conflicts in the Fantasy Realm\nStrategic Relations Among Various Diverse Forces", fontsize=16, fontweight='bold')

# Adjust layout to avoid text clipping
plt.axis('off')
plt.tight_layout()

# Show the plot
plt.show()