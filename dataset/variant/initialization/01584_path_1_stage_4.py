import matplotlib.pyplot as plt
import numpy as np

# Original data series
popularity1 = [15, 15, 25, 7, 10, 8, 20]
# Additional made-up data series
popularity2 = [18, 10, 22, 5, 11, 9, 25]

# Colors for each data series
color1 = 'skyblue'
color2 = 'lightgreen'

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the first data series (inner ring)
wedges1, texts1, autotexts1 = ax.pie(
    popularity1, 
    colors=[color1] * len(popularity1),  
    autopct=lambda p: f'{p:.1f}%', 
    startangle=120,
    pctdistance=0.8, 
    radius=1.0,
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

# Plot the second data series (outer ring)
wedges2, texts2, autotexts2 = ax.pie(
    popularity2, 
    colors=[color2] * len(popularity2),  
    autopct=lambda p: f'{p:.1f}%', 
    startangle=120,
    pctdistance=0.85, 
    radius=1.3,
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

# Draw a center circle to transform pie to doughnut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()