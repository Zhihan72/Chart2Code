import matplotlib.pyplot as plt
import numpy as np

works = [
    "The Little Prince",
    "Pinocchio",
    "The Adventures of Huckleberry Finn",
    "Harry Potter Series",
    "Alice in Wonderland",
    "Don Quixote",
    "The Bible"
]

translations = [300, 260, 275, 350, 150, 250, 335]

fig, ax = plt.subplots(figsize=(12, 8))
colors = plt.cm.plasma(np.linspace(0, 1, len(works)))

bars = ax.barh(works, translations, color=colors, height=0.5, alpha=0.7)

line_styles = ['-', '--', '-.', ':']
marker_types = ['o', 's', 'D', 'v', '^', '<', '>']
ax.set_prop_cycle('linestyle', line_styles)

ax.set_title("The World's Most Translated Literary Works:\nA Glimpse into Multilingualism", 
             fontsize=15, fontweight='bold', pad=10)
ax.set_xlabel('Translation Count', fontsize=13)
ax.set_ylabel('Works', fontsize=13)

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