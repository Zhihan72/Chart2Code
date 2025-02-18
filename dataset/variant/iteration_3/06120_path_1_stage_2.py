import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

categories = ['Intellect', 'Physical', 'Emotional', 'Spiritual', 'Social']

aries = [8, 7, 5, 6, 7]
taurus = [6, 6, 8, 7, 7]
cancer = [5, 5, 9, 6, 8]
leo = [7, 8, 6, 5, 8]

zodiac_data = np.array([aries, taurus, cancer, leo])
labels = ['Aries', 'Taurus', 'Cancer', 'Leo']

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def plot_radar(ax, data, colors, labels):
    for idx, d in enumerate(data):
        values = d.tolist()
        values += values[:1]
        # Changed marker to 'o' and linestyle to 'dashed'
        ax.plot(angles, values, color=colors[idx], linewidth=2, linestyle='dashed', marker='o')
        ax.fill(angles, values, color=colors[idx], alpha=0.25, label=labels[idx])

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Changed the colors array slightly for variety
colors = ['#ff9966', '#66cc66', '#ffcc00', '#cc66ff']
plot_radar(ax, zodiac_data, colors, labels)

plt.xticks(angles[:-1], categories, color='dimgray', size=10)

ax.set_yticklabels([])
ax.set_ylim(0, 10)

# Change grid style and circle style
for y in range(2, 11, 2):
    ax.add_patch(Circle((0,0), y, transform=ax.transData._b, color='lightblue', alpha=0.15, lw=0.5, zorder=0))
    ax.text(y, -y*0.05, str(y), horizontalalignment='center', color='grey', size=10)

# Adjusted layout with thicker border to emphasize the plot
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('darkblue')
ax.spines['polar'].set_linewidth(2)

ax.set_title('Astrological Qualities Analysis\nRadar Chart of Zodiac Signs', size=14, fontweight='bold', pad=30)

# Adjust legend, placing it inside the plot for a different stylistic approach
ax.legend(loc='best', bbox_to_anchor=(0.1, 0.1), fontsize=9)

plt.tight_layout()
plt.show()