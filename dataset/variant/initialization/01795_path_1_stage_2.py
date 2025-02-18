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

colors = ['#8a9a5b', '#b9936c', '#6c5b7b', '#d16ba5', '#9f9f9f', '#ffab84', '#c9cba3', '#6c91bf']

explode = (0, 0, 0.1, 0, 0.1, 0, 0, 0)  # Changed exploded slices

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    resource_allocation, explode=explode, labels=resource_categories, colors=colors,
    autopct='%1.1f%%', startangle=90, shadow=True, wedgeprops=dict(edgecolor='grey', linestyle='dotted') # Edge color and style change
)

# Fonts and colors are changed back to default, no specific modifications here
for text in texts:
    text.set_fontsize(11)
    text.set_color('black')

for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')

ax.set_title("Resource Allocation in Eldoria", fontsize=16, fontweight='bold', pad=10)  # Adjusted title size and padding

ax.legend(wedges, resource_categories, title="Categories", loc="upper right", fontsize=9)  # Changed legend location

plt.grid(True)  # Added grid for an eccentric design choice

plt.tight_layout()

plt.show()