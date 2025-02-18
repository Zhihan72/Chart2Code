import matplotlib.pyplot as plt
import numpy as np

# New Title and Labels
# Title: "Era of Shifting Media: Digital Ascendant"
# X-axis: 'Time Periods'
# Y-axis: 'Adoption Rate (%)'

decades = np.array(['1980s', '1990s', '2000s', '2010s', '2020s'])

# Usage values remain unchanged
vhs_usage = [80, 60, 20, 0, 0]
dvd_usage = [5, 60, 80, 40, 10]
bluray_usage = [0, 10, 50, 70, 45]
digital_usage = [0, 1, 10, 75, 90]

# Setup the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting media type usage over the decades
ax.plot(decades, vhs_usage, label='Tape', marker='o', linestyle='-', linewidth=2, color='#FF5733')
ax.plot(decades, dvd_usage, label='Disc', marker='^', linestyle='--', linewidth=2, color='#3375FF')
ax.plot(decades, bluray_usage, label='Blu', marker='s', linestyle=':', linewidth=2, color='#33FF5E')
ax.plot(decades, digital_usage, label='Stream', marker='D', linestyle='-.', linewidth=2, color='#FF33B8')

# Altered Titles and Labels
ax.set_title("Era of Shifting Media: Digital Ascendant", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time Periods', fontsize=12, fontweight='bold')
ax.set_ylabel('Adoption Rate (%)', fontsize=12, fontweight='bold')

# Customize the legend
ax.legend(title='Technology', fontsize=10, title_fontsize='12', loc='upper left')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate significant trends
ax.annotate('Tape Peak', xy=('1980s', 80), xytext=('1990s', 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='darkred')
ax.annotate('Stream Supremacy', xy=('2020s', 90), xytext=('2010s', 60),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='navy')

# Highlight specific decades
highlight_decades = ['2000s', '2010s']
for decade in highlight_decades:
    ax.axvline(decade, color='grey', linestyle='--', linewidth=1, alpha=0.5)

plt.tight_layout()
plt.show()