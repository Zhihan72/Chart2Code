import matplotlib.pyplot as plt

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

colors = ['#ffd700', '#daa520', '#adff2f', '#7fff00', '#f08080']

def plot_creature_pie_chart(data, creature, snacks, colors):
    fig, ax = plt.subplots(figsize=(7, 7))
    
    ax.pie(
        data,
        labels=None,
        autopct=None,
        startangle=140,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='none'),
        pctdistance=0.85
    )
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set(aspect="equal", title="")
    
    plt.show()

for creature, data in data.items():
    plot_creature_pie_chart(data, creature, snacks, colors)