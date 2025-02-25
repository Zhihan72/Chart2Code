import matplotlib.pyplot as plt

categories = ['Fiction', 'Non-Fic', 'Sci-Fi', 'Fantasy', 'Bio']
distribution = [30, 20, 15, 15, 10]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700', '#FFB6C1']

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    distribution, 
    labels=categories, 
    colors=colors,
    autopct='%1.1f%%', 
    startangle=90,
    wedgeprops={'width': 0.3, 'edgecolor': 'w'}
)

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

ax.axis('equal')
ax.set_title('Book Genres - 2023', fontsize=16, fontweight='bold', pad=20)
ax.legend(wedges, categories, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), title="Genres", fontsize='small', title_fontsize='13')
plt.tight_layout()
plt.show()