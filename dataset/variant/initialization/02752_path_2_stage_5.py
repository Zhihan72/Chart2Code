import matplotlib.pyplot as plt

# Adding two more user categories (G and H) to the data series
user_percentages = [22, 18, 25, 15, 10, 10, 6, 4]

# Adding colors for the new categories
colors = ['#FF5733', '#33FFBD', '#335BFF', '#F5FF33', '#9333FF', '#FF3380', '#33FF57', '#FF33F6']

plt.figure(figsize=(10, 7))
plt.pie(
    user_percentages,
    colors=colors,
    startangle=200,
    autopct='%1.1f%%',
    explode=[0.05, 0, 0.1, 0, 0.15, 0, 0.05, 0.1],  # Adding explode for G and H
    labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],  # Updated labels to include G and H
    shadow=True
)

plt.axis('equal')
plt.legend(title="User Distribution", loc="upper left", bbox_to_anchor=(1, 0.5))
plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()