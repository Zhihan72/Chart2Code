import matplotlib.pyplot as plt
import networkx as nx

# Create an undirected graph
G = nx.Graph()

# Add nodes (representing each year)
years = range(2010, 2021)
G.add_nodes_from(years)

# Add edges with weights (using stock prices, each connected to the next year for simplicity)
apple_stock_prices = [150, 50, 250, 200, 30, 250, 450, 120, 90, 400, 350]
google_stock_prices = [450, 500, 250, 700, 1000, 900, 350, 600, 300, 800, 400]
amazon_stock_prices = [1100, 1500, 250, 600, 200, 2000, 900, 1000, 400, 800, 700]

# Ensuring we interpret these as a graph with specific relations:
for i in range(1, len(years)):
    G.add_edge(years[i-1], years[i], weight=apple_stock_prices[i])
    G.add_edge(years[i-1], years[i], weight=google_stock_prices[i])
    G.add_edge(years[i-1], years[i], weight=amazon_stock_prices[i])

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='#FFC300', node_size=700, font_size=9)

# Edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title('Undirected Graph of Stock Prices Over Years', fontsize=16, fontweight='bold')
plt.show()