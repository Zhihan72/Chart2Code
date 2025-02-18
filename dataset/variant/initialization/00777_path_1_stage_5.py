import matplotlib.pyplot as plt

genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classical', 'Jazz', 'Country', 'Reggae', 'Blues', 'Latin']
user_distribution = [28, 18, 14, 10, 8, 6, 5, 3, 4, 4]

# Altered explode for 'Pop' and 'Hip-Hop'
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(user_distribution, explode=explode, startangle=90, shadow=False, 
        wedgeprops=dict(width=0.3, edgecolor='black'))

# Add grid for style variant
plt.grid(True)

# Modify marker type representation
plt.scatter([], [], marker='o', label='Round Marker', color='red') # using scatter for marker legend
plt.plot([], [], linestyle='-', label='Solid Line', color='blue') # using plot for line style legend

plt.legend(title='Legend')

plt.axis('equal')
plt.tight_layout()

plt.show()