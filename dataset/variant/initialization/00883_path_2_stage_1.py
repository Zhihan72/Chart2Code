import matplotlib.pyplot as plt
import numpy as np

# Define the art movements
art_movements = ['Impressionism', 'Cubism', 'Art Deco', 'Minimalism', 'Surrealism']

# Influence levels for each art movement (across the same design styles)
influence_matrix = np.array([
    [7, 5, 3, 4, 6],  # Impressionism
    [6, 8, 2, 5, 7],  # Cubism
    [4, 7, 5, 3, 6],  # Art Deco
    [3, 4, 9, 8, 5],  # Minimalism
    [5, 6, 4, 7, 8],  # Surrealism
])

design_styles = ['Futurism', 'Bauhaus', 'Brutalism', 'Eco Design', 'Postmodernism']

# Calculate average influence level for each art movement across all design styles
avg_influence = np.mean(influence_matrix, axis=1)

# Plotting the horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))

bar = ax.barh(art_movements, avg_influence, color='skyblue')

# Title and labels
ax.set_title("Average Influence of Art Movements\non Modern Design Styles", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Average Influence Level", fontsize=12, labelpad=20)
ax.set_ylabel("Historical Art Movements", fontsize=12, labelpad=20)

# Adding value labels on the bars
for rect in bar:
    width = rect.get_width()
    ax.annotate(f'{width:.1f}',
                xy=(width, rect.get_y() + rect.get_height() / 2),
                xytext=(3, 0),  # 3 points horizontal offset
                textcoords="offset points",
                ha='left', va='center', fontsize=12, color='darkred')

# Show the plot
plt.show()