import matplotlib.pyplot as plt
import numpy as np

# Art movements and shuffled color usage percentages to alter content
art_movements = ['Renaissance', 'Baroque', 'Romanticism', 'Impressionism', 'Contemporary Art']
color_usage = [22, 18, 25, 15, 20]  # Preserved sum is 100, but content is shuffled

# Colors associated with each art movement
colors = ['#003366', '#8B0000', '#FFD700', '#FFE4B5', '#4682B4']

# Create the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
                                  startangle=140, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3), shadow=True, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

# Customize autotexts
plt.setp(autotexts, size=9, weight='bold', color='white')

# Title
plt.title("The Palette of Emotions:\nColor Preferences Across Art Movements", fontsize=15, fontweight='bold')

# Draw a circle at the center
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio for circular pie
ax.axis('equal')

# Legend
ax.legend(wedges, [f'{movement}: {color} tones' for movement, color in zip(art_movements, ['Rich', 'Deep', 'Vibrant', 'Pastel', 'Bold'])],
          title="Art Movements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()