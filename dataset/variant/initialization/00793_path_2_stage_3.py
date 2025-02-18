import matplotlib.pyplot as plt

# Define art movements and their corresponding color usage percentages
art_movements = ['Baroque', 'Contemporary Art', 'Renaissance', 'Romanticism', 'Impressionism']
color_usage = [25, 15, 20, 18, 22]
colors = ['#8B0000', '#4682B4', '#003366', '#FFD700', '#FFE4B5']

# Create a pie chart without stylistic elements
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%',
       startangle=140, colors=colors, explode=(0.05, 0.05, 0.05, 0.05, 0.05))

# Title without altered look
plt.title("Emotional Hues: Shuffling Preferences of Color", fontsize=15)

# Ensure the pie is drawn as a circle
ax.axis('equal')  

# Display the plot
plt.show()