import matplotlib.pyplot as plt
import numpy as np

regions = ['South America', 'Europe', 'North America', 'Asia']
sandwich_types = ['Grilled Sandwich', 'Cuban Delight', 'Classic Club', 'Toasty BLT', 'PB&J Special']

popularity = np.array([
    [20, 10, 15, 30, 25],  # South America
    [15, 20, 25, 20, 20],  # Europe
    [25, 30, 20, 15, 10],  # North America
    [10, 15, 30, 25, 20]   # Asia
])

# Shuffled colors, line styles and markers
colors = ['#32CD32', '#9400D3', '#FFD700', '#4682B4', '#FF6347']
line_styles = ['-', '--', '-.', ':', '-']  # Introduced line styles for visual variation
markers = ['o', 's', 'D', '^', 'v']  # Different markers for each type

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(regions))

# Randomly styled bars and plots
for idx, (sandwich, color, line_style, marker) in enumerate(zip(sandwich_types, colors, line_styles, markers)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8)
    ax.plot(regions, bottom + popularity[:, idx]/2, line_style, marker=marker, color='black')  # Added plot line in the middle of each bar
    bottom += popularity[:, idx]

ax.set_title("Worldwide Fascination with Sandwiches:\nStacked Insights of Area Taste", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Preference Rate (%)", fontsize=12)
ax.set_xlabel("Continents", fontsize=12)

# Randomly removed the grid and changed legend position
plt.xticks(rotation=45, ha='right')
ax.legend(title="Kinds of Sandwich", bbox_to_anchor=(0.5, 1.15), loc='upper center')
plt.tight_layout()
plt.show()