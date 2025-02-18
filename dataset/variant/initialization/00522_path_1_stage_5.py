import matplotlib.pyplot as plt

energy_sources = ['Sol', 'Wnd', 'Hydr', 'Bio', 'Geo', 'Nucl', 'Tid']
energy_proportions = [30, 25, 15, 10, 5, 10, 5]

# Randomized stylistic elements
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']
explode = (0.1, 0.1, 0, 0, 0, 0.1, 0.1)  # changed some explode values

fig, ax = plt.subplots(figsize=(8, 8))  # different size
wedges, texts, autotexts = ax.pie(energy_proportions, labels=energy_sources, autopct='%1.1f%%', startangle=90, 
                                  colors=colors, explode=explode, wedgeprops={'edgecolor': 'grey', 'linestyle': '--', 'linewidth': 1.5})

for text in texts:
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')

centre_circle = plt.Circle((0, 0), 0.65, fc='white', linestyle='-', linewidth=1.5)
fig.gca().add_artist(centre_circle)

plt.title('2023 Energy Mix Overview', fontsize=15, fontweight='semibold', pad=15)
plt.legend(wedges, energy_sources, title="Energy Sources", loc="upper right", bbox_to_anchor=(0.9, 0.9), fontsize=10)

plt.tight_layout()
plt.show()