import matplotlib.pyplot as plt

meanings = [40, 20, 15, 15]
explode = (0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, _, autotexts = ax.pie(meanings, autopct='%1.1f%%', startangle=90,
                              colors=['#FF6347', '#FFD700', '#32CD32', '#8A2BE2'],
                              explode=explode, shadow=True, wedgeprops={'linestyle': '--', 'linewidth': 2})

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.show()