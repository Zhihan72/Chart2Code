import matplotlib.pyplot as plt

# Mythological creatures and their popularity percentages:
creatures = ['Dragons', 'Phoenix', 'Unicorns', 'Mermaids', 'Centaurs', 'Valkyries', 'Minotaurs', 'Goblins', 'Faeries']
popularity = [30, 18, 14, 10, 7, 6, 2, 8, 5]

# Colors for each creature
colors = ['#FF5733', '#FFC300', '#DAF7A6', '#900C3F', '#581845', '#C70039', '#900C3F', '#2ECC71', '#F39C12']

# Highlight the top favorite creature (Dragons) by separating it slightly
explode = [0.1 if creature == 'Dragons' else 0 for creature in creatures]

# Create the main pie chart showcasing the popularity of mythological creatures
plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    popularity, 
    explode=explode, 
    labels=creatures, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops={'edgecolor': 'black'}, 
    shadow=True
)

# Customize the legend to place it outside the pie chart
plt.legend(wedges, creatures, title="Mythological Creatures", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Customize the text properties for better readability
plt.setp(autotexts, size=10, color="white", weight="bold")
plt.setp(texts, size=12)

# Add a title to the chart
plt.title('Mysteria City Residents’ Favorite Mythological Creatures in 2023', fontsize=14, fontweight='bold', pad=20)

# Draw a circle at the center of pie to convert it into a doughnut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure the layout is tidy to avoid overlapping
plt.tight_layout()

# Display the chart
plt.show()