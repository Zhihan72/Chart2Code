import matplotlib.pyplot as plt

languages = ['Py', 'JS', 'Java', 'C++', 'Ruby', 'Go', 'Rust', 'PHP']
usage_percentages = [29, 24, 16, 12, 7, 5, 4, 3]

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FFA07A', '#98FB98', '#C2C2F0']

fig, ax = plt.subplots(figsize=(9, 9))
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

ax.pie(usage_percentages, labels=languages, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
ax.axis('equal')

ax.set_title('Lang Usage in OSS - 2025', fontsize=15, fontweight='bold', pad=20)
ax.legend(languages, loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()