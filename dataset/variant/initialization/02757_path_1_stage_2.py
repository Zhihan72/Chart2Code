import matplotlib.pyplot as plt

projects = ['Mars Col.', 'Ast. Min.', 'Tel. Dev.', 'Lunar Res.', 'Exo. Disc.']
budget_allocations = [30, 25, 20, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(budget_allocations, 
                                   labels=projects, 
                                   colors=colors, 
                                   autopct='%1.1f%%',
                                   startangle=90, 
                                   pctdistance=0.85,
                                   wedgeprops=dict(width=0.3),
                                   explode=(0.05, 0, 0, 0, 0))

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  
plt.show()