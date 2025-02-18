import matplotlib.pyplot as plt

# Data for alien cuisines preferences (original plus additional)
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
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=1),
    shadow=True,
    explode=[0.05]*len(cuisines)
)

centre_circle = plt.Circle((0, 0), 0.6, fc='white', edgecolor='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title('Alien Taste Buds - A Survey on Alien Cuisine Preferences\nin the Galactic Community', size=16, color='#673AB7', loc='center', pad=40)
ax.legend(wedges, cuisines, title='Cuisines', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12, title_fontsize=14)

for autotext in autotexts:
    autotext.set_color('#455A64')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

plt.text(0, 0, 'Galactic\nSurvey\n2023', ha='center', va='center', fontsize=14, fontweight='bold', color='#673AB7')

plt.tight_layout()

plt.show()