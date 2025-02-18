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
    pctdistance=0.85
)

plt.setp(autotexts, size=10, color="white", weight="bold")
plt.setp(texts, size=12)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()