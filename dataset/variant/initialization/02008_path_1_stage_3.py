import matplotlib.pyplot as plt
import numpy as np

works = [
    "Pinocchio",
    "The Adventures of Huckleberry Finn",
    "Alice in Wonderland",
    "The Little Prince",
    "Don Quixote",
    "The Bible",
    "Harry Potter Series"
]

translations = [260, 275, 150, 300, 250, 335, 350]

fig, ax = plt.subplots(figsize=(12, 8))

# Set a single color for all bars
single_color = 'skyblue'
bars = ax.barh(works, translations, color=single_color, height=0.5, alpha=0.7)

ax.set_title("Insights into Global Linguistic Diversity:\nUnveiling Translation Giants", 
             fontsize=15, fontweight='bold', pad=10)
ax.set_xlabel('Number of Translations', fontsize=13)
ax.set_ylabel('Literary Works', fontsize=13)

for bar in bars:
    ax.text(bar.get_width() - 30, bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', 
            va='center', ha='right', fontsize=10)

ax.tick_params(axis='y', labelsize=11, pad=8)
ax.set_xlim(0, max(translations) + 40)

ax.xaxis.grid(True, linestyle=':', which='major', color='blue', alpha=0.3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()