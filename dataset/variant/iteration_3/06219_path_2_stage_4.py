import matplotlib.pyplot as plt

cuisines = ['Zorg Tacos', 'Nebula Noodles', 'Cosmic Pizza', 'Stellar Sushi', 
            'Galactic Burgers', 'Meteoric Stew', 'Asteroid Salad', 
            'Interstellar Ice Cream', 'Quasar Quesadillas', 'Warp Wine']
percentages = [20, 15, 18, 9, 11, 7, 6, 5, 5, 4]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD433', 
          '#33FFD1', '#D433FF', '#FFB833', '#BAFF33', '#FF3380']

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

plt.title('Alien Taste Buds - A Survey on Alien Cuisine Preferences\nin the Galactic Community', size=16, color='#673AB7', loc='center', pad=40)

plt.tight_layout()

plt.show()