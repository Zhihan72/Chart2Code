import matplotlib.pyplot as plt
import numpy as np

# Data
tea_types = ['Matcha (Japan)', 'Masala Chai (India)', 'Moroccan Mint (Morocco)', 
             'Rooibos (South Africa)', 'Hibiscus (Central America)', 'Yerba Mate (Argentina)']
consumption_percentages = [20, 20, 15, 20, 15, 10]
colors = ['#6db33f', '#e07b39', '#9cc3d5', '#d58339', '#a34f4f', '#8B4513']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Donut chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages, labels=tea_types, colors=colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.4), shadow=True, explode=(0.05,) * len(tea_types)
)

# Customizing text properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(11)

# Adding a legend
ax.legend(wedges, tea_types, title="Tea Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Title
plt.title("The World of Exotic Teas: Global Consumption Snapshot", 
          fontsize=14, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()