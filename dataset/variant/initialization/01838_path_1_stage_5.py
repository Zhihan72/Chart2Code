import matplotlib.pyplot as plt
import numpy as np

languages = ['Java', 'JavaScript', 'Python', 'Go', 'Ruby', 'C#', 'Others']  # Shuffling languages
usage_percentages = [16, 23, 28, 5, 8, 12, 8]  # Rearranging corresponding percentages

fig, ax = plt.subplots(figsize=(12, 7))
x_pos = np.arange(len(languages))

new_colors = ['#ffcc99', '#66b3ff', '#99ff99', '#ffb3e6', '#ff9999', '#c2c2f0', '#c2f0c2']  # Shuffled colors
bars = ax.bar(x_pos, usage_percentages, color=new_colors, width=0.6)

# Altering titles and labels
ax.set_title("Programming Languages Usage Statistics", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Languages of Programming", fontsize=12)
ax.set_ylabel("Percentage (%) in Use", fontsize=12)
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