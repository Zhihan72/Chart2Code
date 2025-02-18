import matplotlib.pyplot as plt

popularity_percentages = [10, 25, 30, 10, 10, 15]  # Manually shuffled the percentages
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#d3a6e0']

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(edgecolor='black', linestyle='--', linewidth=1.5, alpha=0.8)
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('normal')

ax.grid(color='grey', linestyle='-.', linewidth=0.5)
ax.set_aspect(1.2)

plt.tight_layout()
plt.show()