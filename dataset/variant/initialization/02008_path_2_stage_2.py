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

bars = ax.bar(works, translations, color=colors, alpha=0.85)

ax.set_title("Explore: Languages of Global Literary Masterpieces", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Works of Literature', fontsize=12)
ax.set_ylabel('Total Languages Count', fontsize=12)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'{int(bar.get_height())}', 
            va='bottom', ha='center', fontsize=11)

ax.tick_params(axis='x', rotation=45, labelsize=10, pad=10)
ax.set_ylim(0, max(translations) + 50)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()