import matplotlib.pyplot as plt
import numpy as np

devices = ['Smartphones', 'Tablets', 'Laptops', 'Smart TVs', 'Wearables', 'Gaming Consoles']
usage_percentage = [35, 15, 25, 10, 8, 7]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff6666', '#c0c0c0']
explode = (0.1, 0, 0, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    usage_percentage,
    labels=devices,
    colors=colors,
    autopct='%1.1f%%',
    startangle=45,  # Changed start angle for variation
    explode=explode,
    wedgeprops=dict(edgecolor='black', linewidth=1, linestyle='--'),  # Modified edge style
    pctdistance=0.75
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

ax.set_title("TechVille Device Usage Share:\nDiverse Tech Preferences", fontsize=18, fontweight='light', pad=15)

plt.setp(autotexts, size=9, weight='light', color='white')  # Altered text styling
plt.setp(texts, size=11)

ax.text(
    0, 0, 
    'Smart Device\nUsage\n2023', 
    ha='center', va='center', 
    fontsize=10, color='grey', weight='light'  # Different annotation style
)

ax.legend(
    wedges, devices, 
    title="Device Types",  # Changed legend title
    loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9, frameon=False  # Legend without border
)

plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)  # Added grid with dashed lines
plt.tight_layout()

plt.show()