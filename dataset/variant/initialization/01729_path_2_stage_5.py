import matplotlib.pyplot as plt
import numpy as np

countries = ['USA', 'China', 'Germany', 'India', 'Brazil']
total_investments = np.array([50, 70, 35, 65, 40])

# Consistent single color for all bars
single_color = '#20B2AA'

fig, ax = plt.subplots(figsize=(12, 7))

# Apply the single color to all data groups
ax.bar(countries, total_investments, color=single_color, edgecolor='black', width=0.6)

# Remove the title, labels, grid lines, and border for a minimalistic style
for i, investment in enumerate(total_investments):
    ax.text(i, investment + 1, f"${investment}B", color='black', ha='center', va='bottom', fontsize=10)

# Turn off axes borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)

plt.tight_layout()
plt.show()