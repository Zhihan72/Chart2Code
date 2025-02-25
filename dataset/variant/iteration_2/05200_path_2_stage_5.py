import matplotlib.pyplot as plt
import networkx as nx

nodes = [
    "Elven", "Dwarves", "Humans",
    "Orcs", "Wizards", "Goblins",
    "Dragon", "Necromancer", "Giants",
    "Faeries", "Trolls"
]

edges = {
    ("Elven", "Humans"): {'relation': 'Allied', 'weight': 5},
    ("Dwarves", "Humans"): {'relation': 'Allied', 'weight': 4},
    ("Humans", "Orcs"): {'relation': 'Conflict', 'weight': 6},
    ("Wizards", "Elven"): {'relation': 'Allied', 'weight': 3},
    ("Goblins", "Orcs"): {'relation': 'Ally', 'weight': 4},
    ("Dragon", "Necromancer"): {'relation': 'Neutral', 'weight': 2},
    ("Necromancer", "Humans"): {'relation': 'Conflict', 'weight': 5},
    ("Humans", "Goblins"): {'relation': 'Conflict', 'weight': 3},
    ("Giants", "Trolls"): {'relation': 'Allied', 'weight': 7},
    ("Faeries", "Giants"): {'relation': 'Neutral', 'weight': 3},
    ("Faeries", "Wizards"): {'relation': 'Ally', 'weight': 5}
}

G = nx.Graph()  # Changed from nx.DiGraph() to nx.Graph() for undirected edges
G.add_nodes_from(nodes)
for (start, end), attrs in edges.items():
    G.add_edge(start, end, **attrs)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(14, 10))

colors = {
    'Allied': '#32CD32',   # LimeGreen
    'Conflict': '#DC143C', # Crimson
    'Ally': '#1E90FF',     # DodgerBlue
    'Neutral': '#A9A9A9'   # DarkGray
}

nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='#BDB76B', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

for (start, end), attrs in edges.items():
    nx.draw_networkx_edges(G, pos, edgelist=[(start, end)], width=2, edge_color=colors[attrs['relation']])
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(start, end): attrs['relation']}, font_color='black')

plt.title("Fantasy Realm Relations", fontsize=16, fontweight='bold')

plt.axis('off')
plt.tight_layout()

plt.show()