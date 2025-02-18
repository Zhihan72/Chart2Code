import matplotlib.pyplot as plt
import numpy as np

# Backstory: We're presenting the results of a survey on favorite mythical creatures. This survey was held in a fictional world where mythical creatures are a part of daily life. The survey aimed to find out which mythical creature is loved most by the inhabitants.

# Data for the survey
creatures = ['Dragons', 'Unicorns', 'Phoenixes', 'Mermaids', 'Goblins']
popularity = [40, 25, 20, 10, 5]
colors = ['#ff6666','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Plotting the Pie Chart
fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(popularity, colors=colors, labels=creatures, autopct='%1.1f%%',
                                  startangle=140, pctdistance=0.80, explode=[0.1 if p == max(popularity) else 0 for p in popularity])

# Adding annotation for emphasis
for i, (pct, txt) in enumerate(zip(autotexts, texts)):
    txt.set_fontsize(12)
    if popularity[i] == max(popularity):
        txt.set_fontweight('bold')
        txt.set_color('#ff3333')
    txt.set_text('\n'.join(txt.get_text().split()))
    pct.set_fontsize(12)
    pct.set_color('black')

# Titles and customization
plt.title("Inhabitants' Favorite Mythical Creatures\nA Survey from the Enchanted Realms", fontsize=16, fontweight='bold', pad=20)
plt.setp(autotexts, size=12, weight="bold", color="black")

# Add a circle at the center to create a 'donut' appearance
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Ensure equal aspect ratio to make the pie a perfect circle
ax.axis('equal')  

# Legend placed outside the chart
ax.legend(wedges, creatures, title="Mythical Creatures", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()