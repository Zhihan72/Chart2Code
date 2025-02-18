import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    "Elven Forest", "Dwarven Mines", "Human Kingdom",
    "Orc Camp", "Wizard Tower", "Goblin Lair",
    "Dragon's Den", "Necromancer's Crypt"
]

# Manually altering the content within certain data groups
edges = {
    ("Elven Forest", "Dragon's Den"): {'relation': 'Ally', 'weight': 5},
    ("Dwarven Mines", "Orc Camp"): {'relation': 'Conflict', 'weight': 4},
    ("Human Kingdom", "Goblin Lair"): {'relation': 'Neutral', 'weight': 6},
    ("Wizard Tower", "Necromancer's Crypt"): {'relation': 'Conflict', 'weight': 3},
    ("Goblin Lair", "Dragon's Den"): {'relation': 'Neutral', 'weight': 4},
    ("Elven Forest", "Human Kingdom"): {'relation': 'Alliance', 'weight': 2},
    ("Necromancer's Crypt", "Dwarven Mines"): {'relation': 'Ally', 'weight': 5},
    ("Orc Camp", "Wizard Tower"): {'relation': 'Alliance', 'weight': 3}
}

G = nx.Graph()
G.add_nodes_from(nodes)
for (start, end), attrs in edges.items():
    G.add_edge(start, end, **attrs)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(14, 10))

consistent_color = '#1f77b4'

nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=consistent_color, edgecolors=consistent_color)

nx.draw_networkx_edges(G, pos, edgelist=edges.keys(), width=1.5, edge_color=consistent_color)

plt.axis('off')
plt.tight_layout()

plt.show()