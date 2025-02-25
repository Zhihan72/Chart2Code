import matplotlib.pyplot as plt

categories = [
    'Science Fiction', 'Fantasy', 'Mystery', 'Fiction', 
    'Biographies', 'Non-Fiction', 'Adventure', 'Historical Fiction'
]

distribution = [30, 20, 15, 15, 10, 10, 25, 5]

# Shuffle colors by manually changing the order
colors = [
    '#FFB6C1', '#66B2FF', '#90EE90', '#99FF99', 
    '#DA70D6', '#FFD700', '#FFA07A', '#FF9999'
]

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    distribution, 
    labels=categories, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=90,
    explode=(0, 0.1, 0, 0.05, 0.1, 0, 0.1, 0.1),
    wedgeprops=dict(width=0.3)
)

for text in texts:
    text.set_fontsize(14)

for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontsize(12)

ax.grid(which='both', linestyle='--', linewidth=0.5)
ax.set_title('Literary Genres in our New Collection', fontsize=18, style='italic', pad=15)
ax.legend(wedges, categories, loc='upper right', bbox_to_anchor=(0.9, 1), title="Genres")

plt.tight_layout()
plt.show()