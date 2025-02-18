import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# An animal shelter has compiled data on the adoption rates for different types of pets over the last year. 
# They wish to visualize this data in a pie chart to present it to their stakeholders, highlighting areas of 
# improvement and growth in adoption rates.

# Adoption data for different types of pets
pets = ['Dogs', 'Cats', 'Rabbits', 'Birds', 'Reptiles']
adoption_rates = [350, 300, 120, 80, 50]

# Define colors for each segment
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2F0C2']

# Create figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot a pie chart
wedges, texts, autotexts = ax.pie(
    adoption_rates,
    labels=pets,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='white'),
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

# Draw a white circle at the center of the pie to transform it into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Set the title
plt.title('Adoption Rates of Different Pets\nin the Last Year at Our Shelter', fontsize=16, fontweight='bold')

# Customize and position percentage labels
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Customize the category labels
for text in texts:
    text.set_fontsize(11)

# Add annotations outside the pie chart wedges
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f'{adoption_rates[i]} adoptions',
                xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=10, color='darkblue',
                arrowprops=dict(arrowstyle="-", color='gray'))

# Add a legend for clarity
ax.legend(wedges, pets, title="Types of Pets", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Enhance layout
plt.tight_layout()

# Display the donut pie chart
plt.show()