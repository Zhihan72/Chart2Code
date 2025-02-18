import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Wind', 'Fossil Fuels', 'Solar', 'Geothermal', 'Hydrogen']
energy_usage = np.array([15, 10, 25, 10, 20])

colors = ['#FF4500', '#32CD32', '#FFD700', '#9400D3', '#4682B4']
explode = (0.1, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.2f%%',
    startangle=120,
    colors=colors,
    explode=explode,
    shadow=False
)

plt.setp(autotexts, size=8, weight="normal", color='blue')
plt.setp(texts, size=12, weight='light')

plt.title(
    'Intergalactic Energy Sources: Usage in 2077',
    fontsize=14, weight='normal', pad=15
)

ax.legend(
    wedges, energy_sources, title="Energy Types",
    loc="upper right", bbox_to_anchor=(1.3, 1), fontsize=9
)

ax.grid(True)

plt.tight_layout()
plt.show()