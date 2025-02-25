import matplotlib.pyplot as plt
import numpy as np

pets = ['Birds', 'Dogs', 'Rabbits', 'Reptiles', 'Cats']
adoption_rates = [350, 300, 120, 80, 50]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2F0C2']

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    adoption_rates,
    labels=pets,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=(0.05, 0.05, 0.05, 0.05, 0.05),
    shadow=True
)

plt.title('Shelter Adoption Stats\nPast Year Overview', fontsize=16, fontweight='bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

for text in texts:
    text.set_fontsize(11)

for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.annotate(f'Adopted: {adoption_rates[i]}',
                xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=10, color='darkblue',
                arrowprops=dict(arrowstyle="-", color='gray'))

ax.legend(wedges, pets, title="Pet Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()