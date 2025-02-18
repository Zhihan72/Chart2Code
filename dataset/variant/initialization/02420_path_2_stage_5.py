import matplotlib.pyplot as plt
import numpy as np

regions = ['South America', 'Europe', 'North America', 'Asia', 'Africa']
sandwich_types = ['Grilled Sandwich', 'Cuban Delight', 'Classic Club', 'Toasty BLT', 'PB&J Special']

popularity = np.array([
    [20, 10, 15, 30, 25],  
    [15, 20, 25, 20, 20],  
    [25, 30, 20, 15, 10],  
    [10, 15, 30, 25, 20],
    [18, 22, 28, 16, 24]   # Made-up data for Africa
])

colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2']

fig, ax = plt.subplots(figsize=(12, 8))

total_width = 0.8
bar_width = total_width / len(sandwich_types)

for idx, (sandwich, color) in enumerate(zip(sandwich_types, colors)):
    ax.bar(np.arange(len(regions)) + idx * bar_width, popularity[:, idx], 
           width=bar_width, color=color, label=sandwich, alpha=0.8)

ax.set_title("Worldwide Fascination with Sandwiches:\nGrouped Insights of Area Taste", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Preference Rate (%)", fontsize=12)
ax.set_xlabel("Continents", fontsize=12)

ax.set_xticks(np.arange(len(regions)) + total_width / 2 - bar_width / 2)
ax.set_xticklabels(regions, rotation=45, ha='right')
ax.legend(title="Kinds of Sandwich", bbox_to_anchor=(0.5, 1.15), loc='upper center')
plt.tight_layout()
plt.show()