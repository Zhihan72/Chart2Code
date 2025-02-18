import matplotlib.pyplot as plt
import numpy as np

# Data for alien cuisines preferences
cuisines = ['Zorg Tacos', 'Nebula Noodles', 'Cosmic Pizza', 'Stellar Sushi', 'Galactic Burgers', 'Meteoric Stew']  # Removed 'Asteroid Salad'
percentages = [25, 18, 20, 10, 12, 8]  # Removed the percentage for 'Asteroid Salad'

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 10))

wedges, texts, autotexts = ax.pie(
    percentages,
    colors=['#54C7E8'],
    startangle=90,
    labels=cuisines,
    autopct='%1.1f%%',
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=1),
    shadow=True,
    explode=[0.05]*len(cuisines)
)

# Adding a circle in the middle to create a donut shape
centre_circle = plt.Circle((0, 0), 0.6, fc='white', edgecolor='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

# Title and legend
plt.title('Alien Taste Buds - A Survey on Alien Cuisine Preferences\nin the Galactic Community', size=16, color='#673AB7', loc='center', pad=40)
ax.legend(wedges, cuisines, title='Cuisines', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12, title_fontsize=14)

# Customizing the autotext labels
for autotext in autotexts:
    autotext.set_color('#455A64')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

# Adding central text within the donut
plt.text(0, 0, 'Galactic\nSurvey\n2023', ha='center', va='center', fontsize=14, fontweight='bold', color='#673AB7')

plt.tight_layout()

# Display the chart
plt.show()