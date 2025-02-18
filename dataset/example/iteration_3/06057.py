import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Backstory:
# In the small town of Greenfield, an annual community festival full of activities and services is held. 
# We will visualize the interactions between different stalls at the festival.
# Each node represents a stall, and edges indicate interactions between the stalls.

# Define the nodes (festival stalls) with their activities
nodes = [
    "Food Stall", "Crafts Stall", "Games Stall",
    "Music Stage", "Storytelling Corner", "Info Booth",
    "Art Exhibition", "Eco Workshop", "Health Checkup"
]

# Define the edges (interactions) with weights (number of visitors moving between stalls)
edges = [
    ("Food Stall", "Crafts Stall", 30),
    ("Food Stall", "Games Stall", 25),
    ("Crafts Stall", "Art Exhibition", 20),
    ("Games Stall", "Music Stage", 50),
    ("Music Stage", "Storytelling Corner", 40),
    ("Storytelling Corner", "Info Booth", 10),
    ("Info Booth", "Eco Workshop", 15),
    ("Eco Workshop", "Health Checkup", 5),
    ("Food Stall", "Health Checkup", 8),
    ("Games Stall", "Crafts Stall", 12),
    ("Art Exhibition", "Eco Workshop", 18),
    ("Music Stage", "Food Stall", 22),
    ("Health Checkup", "Info Booth", 14)
]

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add nodes and edges to the graph
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# Calculate positions for the nodes using the spring layout
pos = nx.spring_layout(G, seed=42)

# Node colors based on types of activity
node_colors = []
activity_colors = {
    "Food": "salmon",
    "Crafts": "khaki",
    "Games": "lightblue",
    "Music": "lightgreen",
    "Storytelling": "orchid",
    "Info": "lightgrey",
    "Art": "peachpuff",
    "Eco": "aquamarine",
    "Health": "plum"
}
for node in G.nodes:
    for activity, color in activity_colors.items():
        if activity in node:
            node_colors.append(color)
            break

# Node size based on the degree (number of interactions)
node_sizes = [700 + 150 * G.degree(node) for node in G.nodes]

# Draw nodes with their corresponding size and color
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, edgecolors='black')

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='-|>', arrowsize=15, edge_color='grey')

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw edge labels with the number of interactions
edge_labels = {(u, v): f"{w} visitors" for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3)

# Set the title for the plot with line breaks for readability
plt.title("Greenfield Community Festival:\nVisitor Interactions Between Stalls", fontsize=14, fontweight='bold')

# Automatically adjust the layout for better presentation
plt.tight_layout()

# Remove axes for a cleaner look
plt.axis('off')

# Display the directed node chart
plt.show()