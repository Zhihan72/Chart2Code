import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# A fictional survey was conducted among enchanted creatures residing in a magical forest
# to determine their favorite types of magical snacks. The survey results provide
# insight into the distribution of snack preferences among these magical beings.

# Data Preparation:
creatures = ['Elves', 'Fairies', 'Dwarves', 'Wizards', 'Trolls', 'Dragons']
snacks = ['Pixie Dust Doughnuts', 'Enchanted Apples', 'Mystic Muffins', 'Spellbound Scones', 'Charismatic Chews']

# Survey results
data = {
    'Elves': [40, 20, 15, 10, 15],
    'Fairies': [25, 40, 10, 20, 5],
    'Dwarves': [30, 10, 30, 20, 10],
    'Wizards': [20, 25, 20, 25, 10],
    'Trolls': [10, 15, 35, 5, 35],
    'Dragons': [20, 5, 10, 15, 50]
}

# Colors for the pie chart
colors = ['#ffd700', '#daa520', '#adff2f', '#7fff00', '#f08080']

# Function to plot individual creature's pie chart
def plot_creature_pie_chart(data, creature, snacks, colors):
    fig, ax = plt.subplots(figsize=(7, 7))
    
    # Pie chart settings
    wedges, texts, autotexts = ax.pie(
        data,
        labels=snacks,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        pctdistance=0.85,
        textprops=dict(size=10)
    )
    
    # Draw a white circle at the center to create a donut look
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    # Add a title and ensure the pie is circular
    ax.set(aspect="equal", title=f"{creature} Snack Preferences")
    
    # Add a legend
    ax.legend(wedges, snacks, title="Magical Snacks", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    # Adjust layout
    plt.tight_layout()

    # Show plot
    plt.show()

# Plot data for each type of creature
for creature, data in data.items():
    plot_creature_pie_chart(data, creature, snacks, colors)