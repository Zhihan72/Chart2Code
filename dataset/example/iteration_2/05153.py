import matplotlib.pyplot as plt
import numpy as np

# Define the backstory and dataset
# Backstory: The chart reflects the passing of time and the shift in popular media formats over the decades
# Title: "Golden Age of Media Formats: VHS, DVDs, Blu-ray, and Digital"

# Define decades as labels [1980s, 1990s, 2000s, 2010s, 2020s]
decades = np.array(['1980s', '1990s', '2000s', '2010s', '2020s'])

# Percentage usage values for each media type across the decades
vhs_usage = [80, 60, 20, 0, 0]
dvd_usage = [5, 60, 80, 40, 10]
bluray_usage = [0, 10, 50, 70, 45]
digital_usage = [0, 1, 10, 75, 90]

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each media type's usage over the decades
ax.plot(decades, vhs_usage, label='VHS', marker='o', linestyle='-', linewidth=2, color='#FF5733')
ax.plot(decades, dvd_usage, label='DVD', marker='^', linestyle='--', linewidth=2, color='#3375FF')
ax.plot(decades, bluray_usage, label='Blu-ray', marker='s', linestyle=':', linewidth=2, color='#33FF5E')
ax.plot(decades, digital_usage, label='Digital', marker='D', linestyle='-.', linewidth=2, color='#FF33B8')

# Add titles and labels
ax.set_title("Golden Age of Media Formats:\nVHS, DVDs, Blu-ray, and Digital (1980s-2020s)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12, fontweight='bold')
ax.set_ylabel('Usage (%)', fontsize=12, fontweight='bold')

# Customize the legend
ax.legend(title='Media Formats', fontsize=10, title_fontsize='12', loc='upper left')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate significant trends
ax.annotate('VHS Dominance', xy=('1980s', 80), xytext=('1990s', 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='darkred')
ax.annotate('Digital Takeover', xy=('2020s', 90), xytext=('2010s', 60),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='navy')

# Highlight specific decades
highlight_decades = ['2000s', '2010s']
for decade in highlight_decades:
    ax.axvline(decade, color='grey', linestyle='--', linewidth=1, alpha=0.5)

# Ensure layout does not overlap
plt.tight_layout()
plt.show()