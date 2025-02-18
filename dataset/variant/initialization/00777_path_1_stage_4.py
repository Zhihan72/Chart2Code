import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classical', 'Jazz', 'Country', 'Reggae', 'Blues', 'Latin']
user_distribution = [28, 18, 14, 10, 8, 6, 5, 3, 4, 4]

# Explode slice corresponding to 'Pop'
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(user_distribution, explode=explode, startangle=140, shadow=True, 
        wedgeprops=dict(width=0.3, edgecolor='w'))

plt.axis('equal')
plt.tight_layout()

plt.show()