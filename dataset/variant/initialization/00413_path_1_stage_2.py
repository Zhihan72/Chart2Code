import matplotlib.pyplot as plt
import numpy as np

sports = ["Skydiving", "Bungee", "Rafting", "Climbing", "Biking", "Paragliding"]
adrenaline_levels = [95, 90, 85, 80, 75, 70]

sorted_indices = np.argsort(adrenaline_levels)
sports = [sports[i] for i in sorted_indices]
adrenaline_levels = [adrenaline_levels[i] for i in sorted_indices]

plt.figure(figsize=(14, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(sports)))

bars = plt.barh(sports, adrenaline_levels, color=colors, edgecolor='black', height=0.6)

plt.gca().set_facecolor('#f0f0f0')
plt.gca().set_axisbelow(True)

plt.xlabel('Adrenaline', fontsize=12, weight='bold')
plt.title('Adven. Sports Adrenaline', fontsize=16, fontweight='bold', loc='left')
plt.grid(axis='x', linestyle='--', alpha=0.5, color='gray')

for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width()} ⚡', va='center', ha='left', color='black', fontsize=11)

plt.yticks(fontsize=11)

plt.tight_layout()
plt.show()