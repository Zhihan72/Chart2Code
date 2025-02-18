import matplotlib.pyplot as plt
import numpy as np

# Data: Monthly growth of solar production for countries
country_labels = ['USA', 'China', 'India', 'Japan']
growth_usa = [3.1, 2.8, 3.6, 4.0, 5.2, 3.8, 4.1, 4.7, 5.0, 4.5, 3.9, 4.3]
growth_china = [4.5, 4.2, 4.8, 5.0, 5.3, 4.9, 5.1, 5.4, 5.7, 5.8, 5.2, 5.0]
growth_india = [3.5, 3.6, 3.8, 4.1, 3.9, 4.0, 3.7, 4.2, 4.5, 4.3, 3.4, 3.9]
growth_japan = [4.2, 4.1, 4.3, 4.6, 4.9, 4.8, 5.0, 4.5, 5.1, 4.8, 4.2, 4.7]

growth_combined = growth_usa + growth_china + growth_india + growth_japan

fig, ax = plt.subplots(figsize=(14, 8))

# Create a histogram
n, bins, patches = ax.hist(growth_combined, bins=np.arange(2.5, 6.5, 0.5),
                           edgecolor='navy', color='orange', alpha=0.85, rwidth=0.8)

# Titles and labels
ax.set_title('Solar Growth 2045', fontsize=18, fontweight='bold', color='darkgreen')
ax.set_xlabel('Growth %', fontsize=14, color='darkred')
ax.set_ylabel('Frequency', fontsize=14, color='darkred')

# Adding a legend with different styles
ax.legend(country_labels, title='Countries', loc='upper left', fontsize=12, edgecolor='purple', facecolor='lightyellow', framealpha=0.5)

# Adding annotations for each bar
for count, rect in zip(n, patches):
    height = rect.get_height()
    ax.annotate(f'{int(count)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=10, color='maroon')

# Changing line styles
ax.grid(visible=True, linestyle=':', linewidth=1, color='gray')

plt.xticks(np.arange(2.5, 6.5, 0.5), color='navy', rotation=45)
plt.tight_layout()
plt.show()