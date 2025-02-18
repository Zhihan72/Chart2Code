import matplotlib.pyplot as plt

creatures = ['Unicorns', 'Faeries', 'Phoenix', 'Mermaids', 'Goblins', 'Valkyries', 'Dragons', 'Minotaurs', 'Centaurs']
popularity = [30, 18, 14, 10, 7, 6, 2, 8, 5]
colors = ['#1E90FF', '#FF69B4', '#32CD32', '#FFD700', '#FF4500', '#9400D3', '#2E8B57', '#8B0000', '#46C2CB']
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

# Adding a white circle at the center to transform pie into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()