import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    "Elven Forest", "Dwarven Mines", "Human Kingdom",
    "Orc Camp", "Wizard Tower", "Goblin Lair",
    "Dragon's Den", "Necromancer's Crypt"
]

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

G = nx.DiGraph()
G.add_nodes_from(nodes)
for (start, end), attrs in edges.items():
    G.add_edge(start, end, **attrs)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(14, 10))

colors = {
    'Alliance': 'green',
    'Conflict': 'red',
    'Ally': 'blue',
    'Neutral': 'grey'
}

# Randomly altered node parameters
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='#FFE4B5', edgecolors='blue')

# Randomly altered labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color='purple', font_weight='light')

# Randomly altered edges and edge labels
for (start, end), attrs in edges.items():
    nx.draw_networkx_edges(G, pos, edgelist=[(start, end)], arrowstyle='-|>', arrowsize=15, width=1.5, edge_color=colors[attrs['relation']])
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(start, end): attrs['relation']}, font_color='orange')

# Randomly altered chart title
plt.title("Fantasy Realm Political Map\nShifting Alliances and Conflicts", fontsize=14, fontweight='normal')

# Removed border and added grid
plt.grid(True) 

plt.axis('off')
plt.tight_layout()

plt.show()