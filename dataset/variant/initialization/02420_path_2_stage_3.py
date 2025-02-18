import matplotlib.pyplot as plt
import numpy as np

regions = ['South America', 'Europe', 'North America', 'Asia']
sandwich_types = ['Grilled Sandwich', 'Cuban Delight', 'Classic Club', 'Toasty BLT', 'PB&J Special']

popularity = np.array([
    [20, 10, 15, 30, 25],  
    [15, 20, 25, 20, 20],  
    [25, 30, 20, 15, 10],  
    [10, 15, 30, 25, 20]   
])

# New set of colors
colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#8A2BE2']  # New color codes for each type
line_styles = ['-', '--', '-.', ':', '-']
markers = ['o', 's', 'D', '^', 'v']

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(regions))

for idx, (sandwich, color, line_style, marker) in enumerate(zip(sandwich_types, colors, line_styles, markers)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8)
    ax.plot(regions, bottom + popularity[:, idx]/2, line_style, marker=marker, color='black')
    bottom += popularity[:, idx]

ax.set_title("Worldwide Fascination with Sandwiches:\nStacked Insights of Area Taste", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Preference Rate (%)", fontsize=12)
ax.set_xlabel("Continents", fontsize=12)

plt.xticks(rotation=45, ha='right')
ax.legend(title="Kinds of Sandwich", bbox_to_anchor=(0.5, 1.15), loc='upper center')
plt.tight_layout()
plt.show()