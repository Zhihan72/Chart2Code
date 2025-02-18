import matplotlib.pyplot as plt
import numpy as np

works = [
    "Pinocchio",
    "The Little Prince",
    "The Bible",
    "Harry Potter Series",
    "Don Quixote",
    "Alice in Wonderland",
    "The Adventures of Huckleberry Finn"
]

translations = [260, 300, 335, 350, 250, 150, 275]

fig, ax = plt.subplots(figsize=(12, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(works)))

bars = ax.barh(works, translations, color=colors, height=0.6, alpha=0.85)

ax.set_title("Explore: Languages of Global Literary Masterpieces", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Total Languages Count', fontsize=12)
ax.set_ylabel('Works of Literature', fontsize=12)

for bar in bars:
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{int(bar.get_width())}', 
            va='center', ha='left', fontsize=11)

ax.tick_params(axis='y', labelsize=10, pad=10)
ax.set_xlim(0, max(translations) + 50)
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()