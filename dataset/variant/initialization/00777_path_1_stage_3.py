import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classical', 'Jazz', 'Country', 'Reggae', 'Blues', 'Latin']
user_distribution = [28, 18, 14, 10, 8, 6, 5, 3, 4, 4]

single_color = ['#66b3ff']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(user_distribution, explode=explode, colors=single_color * len(genres), startangle=140, shadow=True, wedgeprops=dict(edgecolor='w'))

plt.axis('equal')

plt.tight_layout()

plt.show()