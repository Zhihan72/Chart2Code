import matplotlib.pyplot as plt

resource_categories = [
    'Agriculture & Livestock',
    'Infrastructure & Trade',
    'Defense & Security',
    'Healthcare',
    'Education',
    'Environment & Forestry'
]

resource_allocation = [20, 15, 12, 10, 10, 8]

# Use a single color for all data groups
single_color = ['#6c5b7b']

explode = (0, 0.1, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    resource_allocation, explode=explode, labels=resource_categories, colors=single_color*len(resource_allocation),
    autopct='%1.1f%%', startangle=90, shadow=True, wedgeprops=dict(edgecolor='grey', linestyle='dotted')
)

for text in texts:
    text.set_fontsize(11)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')

ax.set_title("Resource Allocation in Eldoria", fontsize=16, fontweight='bold', pad=10)

ax.legend(wedges, resource_categories, title="Categories", loc="upper right", fontsize=9)

plt.grid(True)

plt.tight_layout()

plt.show()