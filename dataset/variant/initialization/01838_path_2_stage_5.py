import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
languages = ['Py', 'JS', 'Java', 'C#', 'Other']
usage_percentages = [28, 23, 16, 12, 8]

# Create a figure and axis with altered size
fig, ax = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(languages))

# Alter stylistic elements randomly
bars = ax.barh(y_pos, usage_percentages, color='#ff7f0e', height=0.5, edgecolor='grey', linestyle='--')

# Setting a different style for the title and labels
ax.set_title("Lang Usage in 2023", fontsize=18, fontweight='light', pad=15, color='darkblue')
ax.set_xlabel("Usage (%)", fontsize=12, color='brown')
ax.set_xlim(0, 35)
ax.set_yticks(y_pos)
ax.set_yticklabels(languages, fontsize=10, fontstyle='italic')

# Adding grid lines with a different style and color
ax.xaxis.grid(True, linestyle='-.', linewidth=0.6, color='gray', alpha=0.5)

# Randomly altering annotations
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),
                textcoords="offset points",
                ha='center', va='center', fontsize=9, color='darkred')

# Randomly remove borders
for spine in ax.spines.values():
    spine.set_visible(False)

# Display plot with altered style
plt.tight_layout()
plt.show()