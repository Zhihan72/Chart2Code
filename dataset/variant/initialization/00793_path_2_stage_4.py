import matplotlib.pyplot as plt

art_movements = ['Baroque', 'Contemporary Art', 'Renaissance', 'Romanticism', 'Impressionism']
color_usage = [25, 15, 20, 18, 22]
shuffled_colors = ['#FFE4B5', '#4682B4', '#FFD700', '#8B0000', '#003366']

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
       startangle=140, colors=shuffled_colors, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

plt.title("Emotional Hues: Shuffling Preferences of Color", fontsize=15)
ax.axis('equal')  
plt.show()