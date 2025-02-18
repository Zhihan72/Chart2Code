import matplotlib.pyplot as plt

# Data for alien cuisines preferences
cuisines = ['Zorg Tacos', 'Nebula Noodles', 'Cosmic Pizza', 'Stellar Sushi', 'Galactic Burgers', 'Meteoric Stew']
percentages = [25, 18, 20, 10, 12, 8]

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    percentages,
    startangle=90,
    labels=cuisines,
    autopct='%1.1f%%',
    shadow=True,
    explode=[0.05]*len(cuisines)
)

ax.axis('equal')

# Title and legend
plt.title('Alien Taste Buds - A Survey on Alien Cuisine Preferences\nin the Galactic Community', size=16, color='#673AB7', loc='center', pad=40)
ax.legend(wedges, cuisines, title='Cuisines', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12, title_fontsize=14)

# Customizing the autotext labels
for autotext in autotexts:
    autotext.set_color('#455A64')
    autotext.set_fontsize(12)
    autotext.set_weight('bold')

plt.tight_layout()

# Display the chart
plt.show()