import matplotlib.pyplot as plt
import numpy as np

# Data for chart
pets = ['Dog', 'Cat', 'Rabbit', 'Bird']
adoption_rates = [350, 300, 120, 80]
new_colors = ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3']  # New colors for each pet

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    adoption_rates,
    labels=pets,
    colors=new_colors,  # Applied new color set
    autopct='%1.1f%%',
    startangle=110,
    pctdistance=0.90,
    wedgeprops=dict(width=0.3, edgecolor='black'),
    explode=(0.08, 0.08, 0.08, 0.08),
    shadow=True
)

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('Pet Adoption Rates', fontsize=18, fontweight='heavy', color='darkgreen')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('normal')
    autotext.set_fontsize(9)

for text in texts:
    text.set_fontsize(10)

for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f'{adoption_rates[i]}',
                xy=(x, y), xytext=(1.4*np.sign(x), 1.2*y),
                horizontalalignment=horizontalalignment, fontsize=9, color='maroon',
                arrowprops=dict(arrowstyle="-|>", color='black'))

ax.legend(wedges, pets, title="Pets", loc="upper right", bbox_to_anchor=(1.2, 1.0))

plt.tight_layout()
plt.show()