import matplotlib.pyplot as plt

flowers = ['Roses', 'Yellow Tulips', 'Lilies', 'Daisies', 'Lavenders']
meanings = [40, 20, 15, 15, 10]
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(meanings, labels=flowers, autopct='%1.1f%%', startangle=90,
       colors=['#FF6347', '#FFD700', '#32CD32', '#8A2BE2', '#20B2AA'], 
       explode=explode, shadow=True, wedgeprops={'linestyle': '--', 'linewidth': 2})

ax.axis('equal')

plt.title('The Language of Flowers:\nSymbolism in Floristry', fontsize=14, fontweight='bold')

plt.grid(visible=True, linestyle=':', linewidth=1)

plt.legend(loc='upper right', fontsize='small')

plt.show()