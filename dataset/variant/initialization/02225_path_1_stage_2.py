import matplotlib.pyplot as plt

energy_share = [33, 25, 20, 12, 5, 3, 2]
colors = ['#2ca02c', '#8c564b', '#aec7e8', '#ffcc00', '#1f77b4', '#9467bd', '#ff7f0e']

explode = (0.1, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
wedges, _, autotexts = plt.pie(
    energy_share, 
    explode=explode, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops={'edgecolor': 'black'}, 
    shadow=True
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()