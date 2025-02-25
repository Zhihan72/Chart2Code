import matplotlib.pyplot as plt
import numpy as np

fruits = ["Apple", "Banana", "Cherry", "Date", "Elder"]
years = ["18", "19", "20", "21", "22"]

fruit_production = np.array([
    [150, 180, 200, 220, 240],
    [100, 120, 140, 160, 180],
    [60, 80, 100, 120, 140],
    [20, 40, 60, 80, 100],
    [10, 30, 50, 70, 90]
])

deviations = fruit_production - fruit_production.mean(axis=1, keepdims=True)

bar_width = 0.25
x = np.arange(len(years))

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
new_colors = ['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#4B0082']

# First subplot: Diverging Bar Chart for deviations in fruit production
for i, fruit in enumerate(fruits):
    axs[0].bar(x + i * bar_width, deviations[i], width=bar_width, label=fruit, color=new_colors[i], edgecolor='grey', linestyle='-.')

axs[0].set_title('Deviation from Avg Production', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Yr', fontsize=14)
axs[0].set_ylabel('Production Dev', fontsize=14)
axs[0].set_xticks(x + bar_width * 2)
axs[0].set_xticklabels(years)
axs[0].axhline(0, color='black', linewidth=1)
axs[0].legend(title='Fruit', fontsize=11, title_fontsize='11', loc='best')
axs[0].grid(axis='y', linestyle=':', alpha=0.5)

for i in range(len(fruits)):
    for j in range(len(years)):
        axs[0].text(x[j] + i * bar_width, deviations[i, j] + (3 if deviations[i, j] >= 0 else -6), f'{deviations[i, j]:.0f}', ha='center', va='bottom' if deviations[i, j] >= 0 else 'top', fontsize=9)

average_production = np.mean(fruit_production, axis=1)
axs[1].pie(average_production, labels=fruits, colors=new_colors, autopct='%.1f%%', startangle=90, pctdistance=0.9)
axs[1].set_title('Avg Production Share', fontsize=16, fontweight='bold', pad=20)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)
axs[1].axis('equal')

plt.tight_layout()
plt.show()