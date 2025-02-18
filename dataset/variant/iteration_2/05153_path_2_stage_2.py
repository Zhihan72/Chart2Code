import matplotlib.pyplot as plt
import numpy as np

# Define decades as labels
decades = np.array(['Early 80s', 'Mid 90s', 'Noughties', 'Teens', 'Twenties'])

# Usage values for each media type
vhs_usage = [80, 60, 20, 0, 0]
dvd_usage = [5, 60, 80, 40, 10]
bluray_usage = [0, 10, 50, 70, 45]
digital_usage = [0, 1, 10, 75, 90]

# Plot setup
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting each media type's usage
ax.plot(decades, vhs_usage, label='Videotape', marker='o', linestyle='-', linewidth=2, color='#800000')  # Maroon
ax.plot(decades, dvd_usage, label='Disc Format', marker='^', linestyle='--', linewidth=2, color='#1A237E')  # Indigo
ax.plot(decades, bluray_usage, label='Blu Focus', marker='s', linestyle=':', linewidth=2, color='#388E3C')  # Green
ax.plot(decades, digital_usage, label='Data Stream', marker='D', linestyle='-.', linewidth=2, color='#D32F2F')  # Red

# Add titles and labels
ax.set_title("Shifts in Media Dominance:\nVideotapes to Digital Streams", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Era', fontsize=12, fontweight='bold')
ax.set_ylabel('Popularity (%)', fontsize=12, fontweight='bold')

# Customize the legend
ax.legend(title='Tech Mediums', fontsize=10, title_fontsize='12', loc='upper left')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate significant trends
ax.annotate('Videotape Era', xy=('Early 80s', 80), xytext=('Mid 90s', 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='darkred')
ax.annotate('Data Era', xy=('Twenties', 90), xytext=('Teens', 60),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, fontweight='bold', color='navy')

# Highlight specific decades
highlight_decades = ['Noughties', 'Teens']
for decade in highlight_decades:
    ax.axvline(decade, color='grey', linestyle='--', linewidth=1, alpha=0.5)

# Ensure layout does not overlap
plt.tight_layout()
plt.show()