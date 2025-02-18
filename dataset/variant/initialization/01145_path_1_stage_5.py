import matplotlib.pyplot as plt

groups = ['Sumerians', 'Egyptians', 'Aztecs', 'Incas', 'Romans']
wonders_count = [12, 10, 8, 3, 23]  # Randomly altered values while maintaining structure

colors = ['#ff6699', '#99ccff', '#ffcc00', '#66ff66', '#ff6666']
explode = (0, 0.2, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    wonders_count,
    labels=groups,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140
)

plt.title(
    'Mystical Constructs Legacy',
    fontsize=16,
    fontweight='regular',
    color='darkred',
    pad=15
)

plt.setp(autotexts, size=11, weight='bold', color='navy')
plt.setp(texts, size=11, weight='normal', color='darkgreen')

ax.legend(
    wedges, groups,
    title="Cultures",
    loc='right',
    fontsize=9,
    frameon=True,
    fancybox=True,
    framealpha=0.5
)

plt.tight_layout()
plt.show()