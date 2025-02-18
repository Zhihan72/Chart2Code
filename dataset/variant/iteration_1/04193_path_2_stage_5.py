import matplotlib.pyplot as plt
import numpy as np

seasons = ['Winter', 'Autumn', 'Spring', 'Summer']
apples_consumption = [220, 150, 180, 130]

sorted_indices = np.argsort(apples_consumption)
sorted_seasons = [seasons[i] for i in sorted_indices]
sorted_apples_consumption = [apples_consumption[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(sorted_seasons, sorted_apples_consumption, color='skyblue', edgecolor='gray', linestyle='-', hatch='//')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=9)

ax.set_xlabel('Fruit Seasons', fontsize=11)
ax.set_ylabel('Apples Eaten (kg)', fontsize=11)
ax.set_title('Apples Eaten by Each Season', fontsize=16, fontweight='bold', pad=10)

ax.yaxis.grid(False)
plt.legend(['Apples'], loc='upper left', fontsize=10)

for spine in ax.spines.values():
    spine.set_edgecolor('purple')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()