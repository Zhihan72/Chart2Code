import matplotlib.pyplot as plt

resource_categories = [
    'Agriculture & Livestock',
    'Magical R&D',
    'Infrastructure & Trade',
    'Defense & Security',
    'Healthcare',
    'Education',
    'Arts & Culture',
    'Environment & Forestry'
]

resource_allocation = [20, 15, 15, 12, 10, 10, 10, 8]

assert sum(resource_allocation) == 100, "The resource allocations must sum up to 100."

colors = ['#8a9a5b', '#b9936c', '#6c5b7b', '#d16ba5', '#9f9f9f', '#ffab84', '#c9cba3', '#6c91bf']

explode = (0, 0.1, 0, 0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    resource_allocation, explode=explode, labels=resource_categories, colors=colors,
    autopct='%1.1f%%', startangle=140, shadow=True, wedgeprops=dict(edgecolor='k')
)

for text in texts:
    text.set_fontsize(9)
    text.set_color('darkblue')

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('darkred')

ax.set_title("Resource Distribution in the Kingdom of Eldoria", fontsize=14, fontweight='bold', pad=20)

ax.legend(wedges, resource_categories, title="Resource Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=9)

plt.tight_layout()

plt.show()