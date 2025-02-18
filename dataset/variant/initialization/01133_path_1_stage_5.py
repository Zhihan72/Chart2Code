import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
python = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
javascript = np.array([30, 35, 40, 50, 55, 60, 60, 62, 65, 68, 70])
java = np.array([50, 45, 40, 35, 30, 25, 20, 20, 18, 17, 15])

bar_width = 0.2

r1 = np.arange(len(years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

colors = ['#F7DF1E', '#b07219', '#701516']  # Keeping the same colors

fig, ax = plt.subplots(figsize=(12, 8))

# Altering different styles for bars
ax.bar(r1, python, color=colors[0], width=bar_width, label='Python', edgecolor='black', hatch='/')
ax.bar(r2, javascript, color=colors[1], width=bar_width, label='JS', edgecolor='gray', hatch='\\')
ax.bar(r3, java, color=colors[2], width=bar_width, label='Java', edgecolor='darkred', hatch='x')

# Styling changes
ax.set_title('Programming Languages (2010-20)', fontsize=16, fontweight='bold', color='darkblue')
ax.set_xlabel('Year', fontsize=12, style='italic')
ax.set_ylabel('% Usage', fontsize=12, fontweight='bold')

ax.legend(loc='lower right', title='Languages', fontsize=10, title_fontsize='12', shadow=True)

ax.set_xticks([r + bar_width for r in range(len(years))])
ax.set_xticklabels(years, rotation=45, ha="right", fontsize=10)

ax.grid(axis='y', linestyle='-.', alpha=0.5, color='grey')

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.5)
    spine.set_color('cornflowerblue')

plt.tight_layout()
plt.show()