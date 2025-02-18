import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
sectors = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
elements_discovered = np.array([35, 20, 15, 18, 12])
colors = ['#1E90FF', '#FF69B4', '#32CD32', '#FFD700', '#8A2BE2']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    elements_discovered,
    labels=sectors,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='w'),
    explode=(0.1, 0, 0, 0, 0.2)  # Highlight Alpha and Epsilon sectors
)

# Draw circle for donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Style labels
plt.setp(autotexts, size=12, weight="bold", color="black")
plt.setp(texts, size=12, color="darkblue")

# Show the plot
plt.show()