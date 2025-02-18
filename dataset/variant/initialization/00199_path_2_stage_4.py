import numpy as np
import matplotlib.pyplot as plt

decades = np.arange(1970, 2030, 10)

rock = [40, 35, 25, 15, 10, 5]
# disco = [20, 25, 10, 5, 0, 0]  # Removed
pop = [10, 15, 25, 30, 35, 40]
hip_hop = [0, 0, 10, 20, 25, 30]
electronic = [5, 10, 15, 20, 20, 15]
indie = [0, 0, 5, 10, 10, 10]

stacked_data = np.vstack([rock, pop, hip_hop, electronic, indie])  # Removed 'disco'

streaming_services = [0, 0, 5, 20, 50, 70]

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.stackplot(decades, stacked_data, labels=['Rock', 'Pop', 'Rap', 'EDM', 'Alternative'], 
              colors=['#FF6347', '#32CD32', '#FFD700', '#8A2BE2', '#FF69B4'], alpha=0.6)

ax1.set_xlabel("Year", fontsize=14, fontstyle='italic')
ax1.set_ylabel("% Popularity", fontsize=14, fontstyle='italic')
ax1.set_title("Music Evolution & Streaming (1970-2020s)", fontsize=18, fontweight='normal', pad=15)
ax1.set_xticks(decades)
ax1.grid(axis='y', linestyle=':', alpha=0.7)

ax1.annotate('Rap Surge', xy=(2000, 20), xytext=(1980, 60),
             arrowprops=dict(facecolor='blue', arrowstyle='-|>'), fontsize=14, color='darkred')

ax2 = ax1.twinx()
ax2.plot(decades, streaming_services, label='Streaming Services', color='darkgreen', linestyle='-', marker='s')
ax2.set_ylabel("User Percentage", fontsize=14, fontstyle='italic')

ax1.legend(loc='lower right', fontsize=11, title='Music Styles', title_fontsize='13')
ax2.legend(loc='lower left', fontsize=12, bbox_to_anchor=(0.5, 0))

plt.tight_layout()
plt.show()