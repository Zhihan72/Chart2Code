import matplotlib.pyplot as plt

# Data for works and their translations
works = [
    "Pinocchio", "The Adventures of Huckleberry Finn", "Alice in Wonderland", 
    "The Little Prince", "Don Quixote", "The Bible", "Harry Potter Series",
    "Moby Dick", "War and Peace", "The Odyssey", "To Kill a Mockingbird"
]

translations = [260, 275, 150, 300, 250, 335, 350, 120, 200, 180, 220]

fig, ax = plt.subplots(figsize=(12, 8))

# Vertical bar chart
bars = ax.bar(works, translations, color='skyblue', alpha=0.7)

ax.set_title("Insights into Global Linguistic Diversity:\nUnveiling Translation Giants", 
             fontsize=15, fontweight='bold', pad=10)
ax.set_ylabel('Number of Translations', fontsize=13)
ax.set_xlabel('Literary Works', fontsize=13, labelpad=8)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'{int(bar.get_height())}', 
            ha='center', va='bottom', fontsize=10)

ax.tick_params(axis='x', labelrotation=45, labelsize=10)
ax.set_ylim(0, max(translations) + 40)

ax.yaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()