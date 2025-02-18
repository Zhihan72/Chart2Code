import matplotlib.pyplot as plt

# Define art movements and their corresponding color usage percentages
art_movements = ['Baroque', 'Contemporary Art', 'Renaissance', 'Romanticism', 'Impressionism']
color_usage = [25, 15, 20, 18, 22]

# Colors associated with each art movement
colors = ['#8B0000', '#4682B4', '#003366', '#FFD700', '#FFE4B5']

# Create a standard pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
                                  startangle=140, colors=colors, shadow=True,
                                  explode=(0.05, 0.05, 0.05, 0.05, 0.05))

# Customize autotexts
plt.setp(autotexts, size=9, weight='bold', color='white')

# Title with altered look
plt.title("Emotional Hues:\nShuffling Preferences of Color", fontsize=15, fontweight='bold')

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Legend with altered context
ax.legend(wedges, [f'{movement}: {color} tones' for movement, color in zip(art_movements, ['Deep', 'Bold', 'Rich', 'Vibrant', 'Pastel'])],
          title="Art Movements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()