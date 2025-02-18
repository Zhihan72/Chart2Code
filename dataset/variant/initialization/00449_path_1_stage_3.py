import matplotlib.pyplot as plt

flowers = ['Roses', 'Yellow Tulips', 'Lilies', 'Daisies', 'Lavenders']
meanings = [40, 20, 15, 15, 10]
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(meanings, labels=flowers, autopct='%1.1f%%', startangle=90,
                                  colors=['#FF6347', '#FFD700', '#32CD32', '#8A2BE2', '#20B2AA'],
                                  explode=explode, shadow=True, wedgeprops={'linestyle': '--', 'linewidth': 2})

# Create a 'donut' effect by drawing a white circle in the middle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

plt.title('The Language of Flowers:\nSymbolism in Floristry', fontsize=14, fontweight='bold')

plt.legend(wedges, flowers, loc='upper right', fontsize='small')

plt.show()