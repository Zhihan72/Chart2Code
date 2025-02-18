import matplotlib.pyplot as plt
import numpy as np

sports = ["Skydiving", "Bungee", "Rafting", "Climbing", "Biking", "Paragliding"]
adrenaline_levels = [95, 90, 85, 80, 75, 70]

sorted_indices = np.argsort(adrenaline_levels)
sports = [sports[i] for i in sorted_indices]
adrenaline_levels = [adrenaline_levels[i] for i in sorted_indices]

plt.figure(figsize=(14, 8))
# Use a single color for all bars
single_color = 'blue'
bars = plt.barh(sports, adrenaline_levels, color=single_color, edgecolor='black', height=0.6)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

plt.xlabel('Adrenaline', fontsize=12, weight='bold')
plt.title('Adven. Sports Adrenaline', fontsize=16, fontweight='bold', loc='left')

for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width()} ⚡', va='center', ha='left', color='black', fontsize=11)

plt.yticks(fontsize=11)

plt.tight_layout()
plt.show()