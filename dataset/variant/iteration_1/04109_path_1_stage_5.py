import matplotlib.pyplot as plt

creatures = ['Elves', 'Fae', 'Dwarfs', 'Wiz', 'Trolls', 'Drgs', 'Goblins', 'Mermaids']

data = {
    'Elves': [40, 20, 15, 10, 15],
    'Fae': [25, 40, 10, 20, 5],
    'Dwarfs': [30, 10, 30, 20, 10],
    'Wiz': [20, 25, 20, 25, 10],
    'Trolls': [10, 15, 35, 5, 35],
    'Drgs': [20, 5, 10, 15, 50],
    'Goblins': [15, 25, 20, 30, 10],
    'Mermaids': [10, 35, 20, 15, 20]
}

single_color = ['#00aced']

def plot_creature_donut_chart(data, creature, single_color):
    fig, ax = plt.subplots(figsize=(7, 7))
    
    ax.pie(
        data,
        labels=None,
        startangle=140,
        colors=single_color,
        wedgeprops=dict(width=0.3, edgecolor='none')
    )
  
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    
    ax.set(aspect="equal", title=f'{creature}')
    
    plt.show()

for creature, data in data.items():
    plot_creature_donut_chart(data, creature, single_color)