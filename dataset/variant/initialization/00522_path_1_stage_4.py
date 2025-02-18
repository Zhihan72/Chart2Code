import matplotlib.pyplot as plt

# Shortened labels for the energy sources
energy_sources = ['Sol', 'Wnd', 'Hydr', 'Bio', 'Geo', 'Nucl', 'Tid']
energy_proportions = [30, 25, 15, 10, 5, 10, 5]
single_color = '#32CD32'
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(energy_proportions, labels=energy_sources, autopct='%1.1f%%', startangle=140, 
                                  colors=[single_color] * len(energy_proportions), explode=explode, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('white')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Shortened title and legend title
plt.title('2023 Energy Mix', fontsize=16, fontweight='bold', pad=20)
plt.legend(wedges, energy_sources, title="Sources", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=12)
plt.figtext(0.5, 0.01, "Commitment to clean energy and innovation.", ha="center", fontsize=10, fontstyle='italic')

plt.tight_layout()
plt.show()