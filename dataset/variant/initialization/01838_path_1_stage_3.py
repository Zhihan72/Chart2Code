import matplotlib.pyplot as plt
import numpy as np

languages = ['JavaScript', 'C#', 'Ruby', 'Python', 'Java', 'Go', 'Others']
usage_percentages = [23, 12, 8, 28, 16, 5, 8]

fig, ax = plt.subplots(figsize=(12, 7))
x_pos = np.arange(len(languages))

new_colors = ['#66b3ff', '#ffcc99', '#ff9999', '#99ff99', '#c2c2f0', '#ffb3e6', '#c2f0c2']
bars = ax.bar(x_pos, usage_percentages, color=new_colors, width=0.6)

ax.set_title("Global Usage of Programming Languages in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Programming Languages", fontsize=12)
ax.set_ylabel("Usage Percentage (%)", fontsize=12)
ax.set_ylim(0, 35)
ax.set_xticks(x_pos)
ax.set_xticklabels(languages, rotation=45, ha='right', fontsize=10)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), 
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()