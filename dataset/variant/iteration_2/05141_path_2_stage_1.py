import matplotlib.pyplot as plt
import numpy as np

# Adoption data for different types of pets
pets = ['Dogs', 'Cats', 'Rabbits', 'Birds', 'Reptiles']
adoption_rates = [350, 300, 120, 80, 50]

# Define colors - shuffled
colors = ['#99FF99', '#FF9999', '#C2F0C2', '#FFCC99', '#66B3FF']

# Create figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

# Plot a pie chart with altered stylistic elements
wedges, texts, autotexts = ax.pie(
    adoption_rates,
    labels=pets,
    colors=colors,
    autopct='%1.1f%%',
    startangle=110,  # shifted start angle
    pctdistance=0.90,  # altered percentage distance
    wedgeprops=dict(width=0.3, edgecolor='black'),  # changed wedge properties
    explode=(0.08, 0.08, 0.08, 0.08, 0.08),  # altered explode effect
    shadow=True
)

# Draw a white circle at the center for a donut chart
centre_circle = plt.Circle((0,0),0.60,fc='white')  # altered center circle size
fig.gca().add_artist(centre_circle)

# Set the title
plt.title('Adoption Rates of Different Pets\nin the Last Year at Our Shelter',
          fontsize=18, fontweight='heavy', color='darkgreen')  # altered title style

# Customize and position percentage labels
for autotext in autotexts:
    autotext.set_color('black')  # altered text color
    autotext.set_weight('normal')  # changed text weight
    autotext.set_fontsize(9)  # altered font size

# Customize the category labels
for text in texts:
    text.set_fontsize(10)  # changed font size

# Annotations outside the pie chart wedges
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f'{adoption_rates[i]} adoptions',
                xy=(x, y), xytext=(1.4*np.sign(x), 1.2*y),  # changed text position
                horizontalalignment=horizontalalignment, fontsize=9, color='maroon',
                arrowprops=dict(arrowstyle="-|>", color='black'))  # altered arrow style and color

# Randomly alter the legend position and style
ax.legend(wedges, pets, title="Types of Pets", loc="upper right", bbox_to_anchor=(1.2, 1.0))

# Enhance layout and display the chart
plt.tight_layout()
plt.show()