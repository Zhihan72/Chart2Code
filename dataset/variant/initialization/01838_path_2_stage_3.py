import matplotlib.pyplot as plt
import numpy as np

languages = ['Py', 'JS', 'Java', 'C#', 'Other']
usage_percentages = [28, 23, 16, 12, 8]

fig, ax = plt.subplots(figsize=(12, 7))
x_pos = np.arange(len(languages))
bars = ax.bar(x_pos, usage_percentages, color='#1f77b4', width=0.6)

ax.set_title("Lang Usage in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Langs", fontsize=12)
ax.set_ylabel("Usage (%)", fontsize=12)
ax.set_ylim(0, 35)
ax.set_xticks(x_pos)
ax.set_xticklabels(languages, rotation=45, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()