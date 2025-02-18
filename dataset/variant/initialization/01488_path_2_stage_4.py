import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1500, 1600, 10)

ruff_collars = [10, 15, 25, 35, 50, 60, 75, 85, 90, 95]
puffed_sleeves = [5, 20, 40, 55, 65, 70, 65, 50, 35, 25]

fig, ax = plt.subplots(figsize=(12, 7))

# Assigned different colors for each dataset
collar_color = '#ff6347'  # Tomato
sleeve_color = '#4682b4'  # Steel blue

# Modified marker styles and line styles
ax.plot(decades, ruff_collars, marker='x', linestyle='-.', color=collar_color, linewidth=2.5, label='Elaborate Collars')
ax.fill_between(decades, ruff_collars, color=collar_color, alpha=0.2)

ax.plot(decades, puffed_sleeves, marker='d', linestyle=':', color=sleeve_color, linewidth=2.5, label='Balloon Sleeves')
ax.fill_between(decades, puffed_sleeves, color=sleeve_color, alpha=0.2)

# Altered vertical lines styles
for decade in decades:
    ax.axvline(x=decade, color='gray', linestyle=':', linewidth=0.5, alpha=0.7)

# Updated annotation colors
for i, (decade, rc, ps) in enumerate(zip(decades, ruff_collars, puffed_sleeves)):
    ax.annotate(str(rc), (decade, rc), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=collar_color)
    ax.annotate(str(ps), (decade, ps), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color=sleeve_color)

ax.set_title('Historic Fashion Peaks\nDuring the 16th Century', fontsize=16, fontweight='bold', y=1.05)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Trendiness Score', fontsize=14)
ax.set_xticks(decades)
ax.set_yticks(np.arange(0, 101, 10))

# Adjusted grid style
ax.grid(which='major', axis='both', linestyle=':', linewidth=0.5, alpha=0.8)

# Changed legend location and added border color
ax.legend(title='Apparel Types', loc='upper right', fontsize=12, edgecolor='black', shadow=True)

fig.tight_layout()
plt.show()