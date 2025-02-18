import matplotlib.pyplot as plt
import numpy as np

# Adventure sports and their associated average adrenaline levels
sports = ["Skydiving", "Bungee Jumping", "White Water Rafting",
          "Rock Climbing", "Mountain Biking", "Paragliding"]
adrenaline_levels = [95, 90, 85, 80, 75, 70]

# Sort the adrenaline levels and sports accordingly
sorted_indices = np.argsort(adrenaline_levels)
sports = [sports[i] for i in sorted_indices]
adrenaline_levels = [adrenaline_levels[i] for i in sorted_indices]

plt.figure(figsize=(14, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(sports)))

# Create horizontal bars
bars = plt.barh(sports, adrenaline_levels, color=colors, edgecolor='black', height=0.6)

plt.gca().set_facecolor('#f0f0f0')
plt.gca().set_axisbelow(True)

plt.xlabel('Adrenaline Level (1-100)', fontsize=12, weight='bold')
plt.title('Thrill Factor: Adventure Sports Adrenaline Levels\nSurvey in Thrillville', 
          fontsize=16, fontweight='bold', loc='left')
plt.grid(axis='x', linestyle='--', alpha=0.5, color='gray')

for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width()} ⚡', va='center', ha='left', color='black', fontsize=11)

plt.yticks(fontsize=11)

plt.tight_layout()
plt.show()