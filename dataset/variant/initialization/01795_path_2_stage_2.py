import matplotlib.pyplot as plt
import numpy as np

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

colors = ['#8a9a5b', '#b9936c', '#6c5b7b', '#d16ba5', '#9f9f9f', '#ffab84', '#c9cba3', '#6c91bf', '#ef476f', '#ffd166']

explode = (0, 0.1, 0, 0, 0, 0.1, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    resource_allocation, explode=explode, labels=None, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85, shadow=False, wedgeprops=dict(edgecolor='w')
)

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('darkred')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()