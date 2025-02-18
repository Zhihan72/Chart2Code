import matplotlib.pyplot as plt

creatures = ['Unicorns', 'Faeries', 'Phoenix', 'Mermaids', 'Goblins', 'Valkyries', 'Dragons', 'Minotaurs', 'Centaurs']
popularity = [30, 18, 14, 10, 7, 6, 2, 8, 5]

colors = ['#FF5733', '#FFC300', '#DAF7A6', '#900C3F', '#581845', '#C70039', '#900C3F', '#2ECC71', '#F39C12']
explode = [0.1 if creature == 'Unicorns' else 0 for creature in creatures]

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

plt.legend(wedges, creatures, title="Legendary Beasts", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.setp(autotexts, size=10, color="white", weight="bold")
plt.setp(texts, size=12)

plt.title('Fantasy World Inhabitants\' Top Choices in 2023', fontsize=14, fontweight='bold', pad=20)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()