import matplotlib.pyplot as plt

creatures = ['Elves', 'Fairies', 'Dwarves', 'Wizards', 'Trolls', 'Dragons']
snacks = ['Pixie Dust Doughnuts', 'Enchanted Apples', 'Mystic Muffins', 'Spellbound Scones', 'Charismatic Chews']

data = {
    'Elves': [20, 20, 20, 20, 20],
    'Fairies': [30, 10, 40, 5, 15],
    'Dwarves': [25, 25, 10, 20, 20],
    'Wizards': [10, 30, 30, 20, 10],
    'Trolls': [35, 5, 25, 15, 20],
    'Dragons': [5, 50, 20, 15, 10]
}

single_color = ['#daa520']

def plot_creature_donut_chart(data, creature, snacks, single_color):
    fig, ax = plt.subplots(figsize=(7, 7))

    ax.pie(
        data,
        labels=snacks,
        autopct='%1.1f%%',
        startangle=140,
        colors=single_color * len(snacks),
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        pctdistance=0.85,
        textprops=dict(size=10)
    )

    ax.set(aspect="equal", title=f"{creature} Snack Preferences")
    ax.legend(title="Magical Snacks", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.tight_layout()
    plt.show()

for creature, data in data.items():
    plot_creature_donut_chart(data, creature, snacks, single_color)