import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2024)
bandwidth = [5, 8, 12, 18, 28, 40, 55, 70, 85, 100, 120, 150, 170, 200]

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, bandwidth, color='darkgreen', marker='s', linestyle='--', linewidth=3, markersize=10, label='Monthly Bandwidth (Mbps)')

milestones = {
    2010: "Video Streaming\nBoom Begins",
    2015: "4K Streaming\nBecomes Common",
    2020: "Shift to\nTeleworking",
    2022: "Rise of\n8K Streaming"
}

for year, event in milestones.items():
    annotation_x = year
    annotation_y = bandwidth[years.tolist().index(year)]
    ax.annotate(
        event,
        xy=(annotation_x, annotation_y), 
        xytext=(annotation_x - 3, annotation_y + 20), 
        textcoords='data',
        arrowprops=dict(arrowstyle="->", color='darkorange'),
        color='darkred', fontsize=10, ha='left', bbox=dict(boxstyle="square,pad=0.3", edgecolor='darkred', facecolor='lightblue')
    )

ax.set_title("Monthly Bandwidth Consumption: 2010-2022\nImpact of Streaming, Gaming, and Teleworking", fontsize=16, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Average Monthly Bandwidth (Mbps)", fontsize=12)

ax.set_xticks(years)
ax.set_xlim(2009, 2023)
ax.set_ylim(0, 220)
ax.yaxis.grid(True, linestyle=':', alpha=0.5)

ax.legend(loc='lower right', frameon=True, edgecolor='gray')

plt.tight_layout()
plt.show()