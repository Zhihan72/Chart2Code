import matplotlib.pyplot as plt

popularity_percentages = [30, 25, 15, 10, 10, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#d3a6e0']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages,
    autopct='%1.1f%%',
    startangle=90,  # Changed from 140 to 90 for stylistic variation
    colors=colors,
    wedgeprops=dict(edgecolor='black', linestyle='--', linewidth=1.5, alpha=0.8)  # Altered border style
)

for autotext in autotexts:
    autotext.set_fontsize(10)  # Changed fontsize from 12 to 10
    autotext.set_fontweight('normal')  # Changed fontweight from bold to normal

# Set gridlines for stylistic effect, although unconventional for pie charts
ax.grid(color='grey', linestyle='-.', linewidth=0.5)

# Slight change in aspect for a stylistic twist
ax.set_aspect(1.2)

plt.tight_layout()
plt.show()