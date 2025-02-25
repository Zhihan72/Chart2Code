import matplotlib.pyplot as plt

# Data for chart
pets = ['Dog', 'Cat', 'Rabbit', 'Bird']
adoption_rates = [350, 300, 120, 80]
new_colors = ['#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    adoption_rates,
    labels=pets,
    colors=new_colors,
    autopct='%1.1f%%',
    startangle=110
)

plt.title('Pet Adoption Rates', fontsize=18, fontweight='heavy', color='darkgreen')

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('normal')
    autotext.set_fontsize(9)

for text in texts:
    text.set_fontsize(10)

ax.legend(wedges, pets, title="Pets", loc="upper right", bbox_to_anchor=(1.2, 1.0))

plt.tight_layout()
plt.show()