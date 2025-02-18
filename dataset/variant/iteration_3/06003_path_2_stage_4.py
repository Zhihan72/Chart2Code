import matplotlib.pyplot as plt
import numpy as np

depts = ['Health', 'Edu', 'Infra', 'Safety', 'Arts']
budget_2020 = [160, 175, 205, 180, 65]
budget_2021 = [150, 195, 215, 185, 70]
budget_2022 = [155, 185, 225, 175, 75]

y = np.arange(len(depts))
width = 0.25

fig, ax = plt.subplots(figsize=(14, 8))

bars_2020 = ax.barh(y - width, budget_2020, height=width, color='skyblue', label='2020')
bars_2021 = ax.barh(y, budget_2021, height=width, color='lightgreen', label='2021')
bars_2022 = ax.barh(y + width, budget_2022, height=width, color='lightcoral', label='2022')

ax.set_title('Dept Budget (2020-22)', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Depts', fontsize=12)
ax.set_xlabel('Millions (USD)', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(depts)

def add_labels(ax, bars):
    for bar in bars:
        xval = bar.get_width()
        ax.text(xval + 3, bar.get_y() + bar.get_height() / 2, f'{xval}', ha='left', va='center', fontsize=10, fontweight='bold')

add_labels(ax, bars_2020)
add_labels(ax, bars_2021)
add_labels(ax, bars_2022)

plt.legend()
plt.tight_layout()
plt.show()