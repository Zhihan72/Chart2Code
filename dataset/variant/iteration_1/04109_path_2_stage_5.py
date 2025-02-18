import matplotlib.pyplot as plt

data = {
    'Elves': [20, 20, 20, 20, 20],
    'Fairies': [30, 10, 40, 5, 15],
    'Dwarves': [25, 25, 10, 20, 20],
    'Wizards': [10, 30, 30, 20, 10],
    'Trolls': [35, 5, 25, 15, 20],
    'Dragons': [5, 50, 20, 15, 10]
}

single_color = ['#daa520', '#8A2BE2', '#FF4500', '#008000', '#4682B4']

def plot_creature_donut_chart(data, colors):
    fig, ax = plt.subplots(figsize=(7, 7))

    ax.pie(
        data,
        labels=None,
        autopct=None,
        startangle=90,
        colors=colors,
        wedgeprops=dict(width=0.4, edgecolor='gray', linestyle='--', linewidth=1),
        explode=(0, 0.1, 0, 0, 0.1)
    )

    ax.set(aspect="equal")
    plt.tight_layout()
    plt.show()

for creature, data in data.items():
    plot_creature_donut_chart(data, single_color)