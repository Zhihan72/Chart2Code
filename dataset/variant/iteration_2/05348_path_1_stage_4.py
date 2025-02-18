import matplotlib.pyplot as plt

# Data Preparation with manually shuffled popularities
creatures = ['Dragons', 'Phoenix', 'Unicorns', 'Mermaids', 'Centaurs', 'Valkyries', 'Minotaurs']
popularity = [20, 12, 35, 8, 7, 3, 15]  # Reordered popularity values

# Altering colors and markers for each data group
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33', '#A133FF', '#33FFE2']
explode = [0, 0, 0.2, 0, 0, 0, 0]  # Highlight 'Unicorns' differently

plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    popularity, 
    explode=explode, 
    labels=creatures, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.80, 
    wedgeprops={'edgecolor': 'grey', 'linestyle': '--', 'linewidth': 1.5}
)

# Adding a semi-transparent center circle
centre_circle = plt.Circle((0, 0), 0.60, fc='white', alpha=0.8)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Legend settings
plt.legend(wedges, creatures, title="Mythical Creatures", loc="upper right", fontsize=9, frameon=True, shadow=True)

# Customize text properties
plt.setp(autotexts, size=11, color="black")
plt.setp(texts, size=11, style='italic')

# Add a title
plt.title('Favorite Mythological Creatures in 2023', fontsize=16, style='italic', pad=15)

# Ensure the layout is tidy
plt.tight_layout()

plt.show()