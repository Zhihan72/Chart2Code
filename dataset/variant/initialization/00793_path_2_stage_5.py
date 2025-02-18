import matplotlib.pyplot as plt

# Original data
art_movements = ['Baroque', 'Contemporary Art', 'Renaissance', 'Romanticism', 'Impressionism']

# Randomly altered content within the original structure
color_usage = [22, 20, 15, 25, 18]
shuffled_colors = ['#4682B4', '#8B0000', '#FFD700', '#003366', '#FFE4B5']

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
       startangle=140, colors=shuffled_colors, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

plt.title("Emotional Hues: Shuffling Preferences of Color", fontsize=15)
ax.axis('equal')  
plt.show()