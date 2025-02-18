import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
new_constructions = np.array([2, 4, 5, 8, 7, 10, 12, 15, 18, 20, 25])

fig, ax1 = plt.subplots(figsize=(14, 7))

bar_width = 0.35
index = np.arange(len(years))

# Colors are manually shuffled
color_sequence = ['forestgreen', 'gold', 'darkorange', 'slateblue', 'mediumvioletred', 
                  'dodgerblue', 'indianred', 'mediumpurple', 'royalblue', 'tomato', 'seagreen']

bars1 = ax1.bar(index, new_constructions, bar_width, color=color_sequence, edgecolor='black', linestyle=':', hatch='/', label='Construction Rates')

# Changed textual elements
ax1.set_title("Rate of Construction Over the Decade\n(2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Years", fontsize=12)
ax1.set_ylabel("Number of Constructions", fontsize=12)
ax1.set_xticks(index)
ax1.set_xticklabels(years)

ax1.legend(loc='lower right', fontsize=10, frameon=False)
ax1.grid(axis='y', linestyle=':', linewidth=0.8, alpha=0.9)

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', fontsize=10, color='midnightblue')

plt.suptitle("City Development Trends and Efforts", fontsize=14, y=0.97)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()