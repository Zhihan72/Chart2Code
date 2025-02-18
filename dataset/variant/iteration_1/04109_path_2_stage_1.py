import matplotlib.pyplot as plt
import numpy as np

creatures = ['Elves', 'Fairies', 'Dwarves', 'Wizards', 'Trolls', 'Dragons']
snacks = ['Pixie Dust Doughnuts', 'Enchanted Apples', 'Mystic Muffins', 'Spellbound Scones', 'Charismatic Chews']

data = {
    'Elves': [40, 20, 15, 10, 15],
    'Fairies': [25, 40, 10, 20, 5],
    'Dwarves': [30, 10, 30, 20, 10],
    'Wizards': [20, 25, 20, 25, 10],
    'Trolls': [10, 15, 35, 5, 35],
    'Dragons': [20, 5, 10, 15, 50]
}

# Single color for all pie chart wedges
single_color = ['#daa520']  # Example: using '#daa520' (Golden Rod)

def plot_creature_pie_chart(data, creature, snacks, single_color):
    fig, ax = plt.subplots(figsize=(7, 7))
    
    wedges, texts, autotexts = ax.pie(
        data,
        labels=snacks,
        autopct='%1.1f%%',
        startangle=140,
        colors=single_color * len(snacks),  # Apply the single color across all wedges
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        pctdistance=0.85,
        textprops=dict(size=10)
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set(aspect="equal", title=f"{creature} Snack Preferences")
    ax.legend(wedges, snacks, title="Magical Snacks", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.show()

# Plot data for each type of creature
for creature, data in data.items():
    plot_creature_pie_chart(data, creature, snacks, single_color)