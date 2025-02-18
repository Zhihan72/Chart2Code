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

colors = ['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9400D3']

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(regions))

for idx, (sandwich, color) in enumerate(zip(sandwich_types, colors)):
    ax.bar(regions, popularity[:, idx], bottom=bottom, color=color, label=sandwich, alpha=0.8)
    bottom += popularity[:, idx]

ax.set_title("Worldwide Fascination with Sandwiches:\nStacked Insights of Area Taste", fontsize=16, weight='bold', pad=20)
ax.set_ylabel("Preference Rate (%)", fontsize=12)
ax.set_xlabel("Continents", fontsize=12)

plt.xticks(rotation=45, ha='right')
ax.legend(title="Kinds of Sandwich", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()