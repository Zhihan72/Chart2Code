import matplotlib.pyplot as plt

languages = ['Py', 'JS', 'Java', 'C++', 'Ruby', 'Go', 'Rust', 'PHP']
usage_percentages = [29, 24, 16, 12, 7, 5, 4, 3]

# Stylistic changes
colors = ['#FF9999', '#C2C2F0', '#66B3FF', '#FFD700', '#99FF99', '#FFCC99', '#FFA07A', '#98FB98']
markers = ['o', 'v', '^', '<', '>', 's', 'p', '*']
explode = (0.1, 0.1, 0, 0, 0, 0, 0, 0)
linestyle = ['-', '--', '-.', ':', '-', '--', '-.', ':']

fig, ax = plt.subplots(figsize=(9, 9))

# Modify pie plot with changes
ax.pie(usage_percentages, labels=languages, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=False)

# Hide border
for spine in ax.spines.values():
    spine.set_visible(False)

# Add a grid
ax.grid(False)  # not typically applicable to pie charts

# Modify title
ax.set_title('Language Usage in OSS - 2025', fontsize=13, fontweight='normal', pad=10)

# Modify legend
ax.legend(languages, loc='lower left', bbox_to_anchor=(0.9, 0.5))

plt.tight_layout()
plt.show()