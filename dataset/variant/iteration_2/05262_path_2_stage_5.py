import matplotlib.pyplot as plt

categories = ['Fiction', 'Non-Fic', 'Sci-Fi', 'Fantasy', 'Bio']
distribution = [30, 20, 15, 15, 10]
new_colors = ['#4B0082', '#8A2BE2', '#7FFF00', '#FF4500', '#20B2AA']

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    distribution, 
    labels=categories, 
    colors=new_colors,
    autopct='%1.1f%%', 
    startangle=60,  
    wedgeprops={'width': 0.4, 'edgecolor': 'k'}
)

for text in texts:
    text.set_fontsize(14)
    text.set_fontweight('regular')

for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontsize(11)
    autotext.set_fontweight('regular')

ax.axis('equal')
ax.set_title('Book Genres - 2023', fontsize=18, fontweight='bold', pad=30)
ax.legend(wedges, categories, loc='upper right', bbox_to_anchor=(1, 1, 0.5, 0.5), title="Genres", fontsize='medium', title_fontsize='14')
plt.grid(visible=True)
plt.tight_layout()
plt.show()