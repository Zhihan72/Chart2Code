import matplotlib.pyplot as plt

cuisines = ['Warp Wine', 'Meteoric Stew', 'Quasar Quesadillas', 'Asteroid Salad', 
            'Zorg Tacos', 'Interstellar Ice Cream', 'Stellar Sushi', 
            'Galactic Burgers', 'Cosmic Pizza', 'Nebula Noodles']
percentages = [4, 7, 5, 6, 20, 5, 9, 11, 18, 15]
colors = ['#FF3380', '#33FFD1', '#BAFF33', '#D433FF', '#FF5733', 
          '#FFB833', '#FF33A1', '#FFD433', '#3357FF', '#33FF57']

fig, ax = plt.subplots(figsize=(10, 10))

wedges, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    startangle=90,
    labels=cuisines,
    autopct='%1.1f%%',
    shadow=True,
    explode=[0.05]*len(cuisines)
)

ax.axis('equal')

plt.title('Intergalactic Eating Habits - Survey of Cosmic Culinary Choices\nAcross the Universe', size=16, color='#673AB7', loc='center', pad=40)

plt.tight_layout()

plt.show()