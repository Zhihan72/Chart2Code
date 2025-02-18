import matplotlib.pyplot as plt
import numpy as np

pets = ['Birds', 'Dogs', 'Rabbits', 'Reptiles', 'Cats']
adoption_rates = [350, 300, 120, 80, 50]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2F0C2']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Changed explode parameter to create variety
wedges, texts, autotexts = ax.pie(
    adoption_rates,
    labels=pets,
    colors=colors,
    autopct='%1.1f%%', 
    startangle=90,  # Changed start angle for a different chart orientation
    explode=(0.1, 0.05, 0, 0.05, 0.1),  # Modified explosion values
    shadow=True
)

# Changed chart title style
plt.title('Adoption Overview for Pets\nIn the Last Year', fontsize=18, fontweight='normal', style='italic')

# Modify auto text style
for autotext in autotexts:
    autotext.set_color('black')  # Changed color
    autotext.set_weight('normal')  # Changed weight

# Changed text font size
for text in texts:
    text.set_fontsize(12)

# Changed annotation style
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f'{adoption_rates[i]} adopted',  # Changed annotation text
                xy=(x, y), xytext=(1.4*np.sign(x), 1.2*y),  # Changed position
                horizontalalignment=horizontalalignment, fontsize=9, color='maroon',
                arrowprops=dict(arrowstyle="->", color='cornflowerblue'))  # Changed arrow style and color

# Changed legend style
ax.legend(wedges, pets, title="Types of Pets", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))

# Added grid to the background of the chart
plt.grid(which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()