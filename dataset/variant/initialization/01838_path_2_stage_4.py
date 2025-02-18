import matplotlib.pyplot as plt
import numpy as np

languages = ['Py', 'JS', 'Java', 'C#', 'Other']
usage_percentages = [28, 23, 16, 12, 8]

fig, ax = plt.subplots(figsize=(12, 7))
y_pos = np.arange(len(languages))
bars = ax.barh(y_pos, usage_percentages, color='#1f77b4', height=0.6)

ax.set_title("Lang Usage in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Usage (%)", fontsize=12)
ax.set_ylabel("Langs", fontsize=12)
ax.set_xlim(0, 35)
ax.set_yticks(y_pos)
ax.set_yticklabels(languages, fontsize=10)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                ha='left', va='center', fontsize=10, color='black')

plt.tight_layout()
plt.show()