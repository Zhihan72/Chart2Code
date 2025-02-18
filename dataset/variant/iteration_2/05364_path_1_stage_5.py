import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
new_constructions = np.array([2, 4, 5, 8, 7, 10, 12, 15, 18, 20, 25])

fig, ax1 = plt.subplots(figsize=(14, 7))

color_sequence = ['forestgreen', 'gold', 'darkorange', 'slateblue', 'mediumvioletred', 
                  'dodgerblue', 'indianred', 'mediumpurple', 'royalblue', 'tomato', 'seagreen']

# Use barh to create a horizontal bar chart
bars1 = ax1.barh(years, new_constructions, color=color_sequence, edgecolor='black', linestyle=':', hatch='/', label='Construction Rates')

ax1.set_title("Rate of Construction Over the Decade\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel("Years", fontsize=12)
ax1.set_xlabel("Number of Constructions", fontsize=12)

ax1.legend(loc='lower right', fontsize=10, frameon=False)
ax1.grid(axis='x', linestyle=':', linewidth=0.8, alpha=0.9)

# Adjust text to show values on the bars
for bar in bars1:
    xval = bar.get_width()
    ax1.text(xval + 0.5, bar.get_y() + bar.get_height() / 2, int(xval), va='center', fontsize=10, color='midnightblue')

plt.suptitle("City Development Trends and Efforts", fontsize=14, y=0.97)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()