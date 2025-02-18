import matplotlib.pyplot as plt

creatures = ['Dragons', 'Phoenix', 'Unicorns', 'Mermaids', 'Centaurs', 'Valkyries', 'Minotaurs']
popularity = [20, 12, 35, 8, 7, 3, 15] 

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33', '#A133FF', '#33FFE2']
explode = [0, 0, 0.2, 0, 0, 0, 0]

plt.figure(figsize=(10, 10))
wedges, autotexts = plt.pie(
    popularity, 
    explode=explode, 
    startangle=140, 
    colors=colors, 
    pctdistance=0.80, 
    wedgeprops={'edgecolor': 'grey', 'linestyle': '--', 'linewidth': 1.5}
)

centre_circle = plt.Circle((0, 0), 0.60, fc='white', alpha=0.8)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.setp(autotexts, size=11, color="black")

plt.tight_layout()

plt.show()