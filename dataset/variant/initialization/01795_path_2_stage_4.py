import matplotlib.pyplot as plt

resource_categories = [
    'Agriculture & Livestock',
    'Magical R&D',
    'Infrastructure & Trade',
    'Defense & Security',
    'Healthcare',
    'Education',
    'Arts & Culture',
    'Environment & Forestry',
    'Space Exploration',
    'Digital Technology'
]

resource_allocation = [18, 13, 12, 11, 9, 9, 8, 7, 8, 5]

assert sum(resource_allocation) == 100, "The resource allocations must sum up to 100."

explode = (0, 0.1, 0, 0, 0, 0.1, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    resource_allocation, explode=explode, labels=resource_categories,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85, shadow=False, wedgeprops=dict(edgecolor='w')
)

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('darkred')

plt.tight_layout()
plt.show()