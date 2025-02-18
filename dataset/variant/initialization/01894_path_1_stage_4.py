import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Wind', 'Fossil Fuels', 'Solar', 'Geothermal', 'Hydrogen']
energy_usage = np.array([15, 10, 25, 10, 20])

# Adjusted colors, excluding the one for 'Fusion'
colors = ['#32CD32', '#FFD700', '#9400D3', '#D2691E', '#4682B4']

# Adjusted explode tuple, excluding the explode value for 'Fusion'
explode = (0, 0, 0.1, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    energy_usage,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=190,
    colors=colors,
    explode=explode,
    shadow=True
)

plt.setp(autotexts, size=10, weight="bold", color='black')
plt.setp(texts, size=10, weight='bold')

plt.title(
    'Interstellar Power Distribution:\nCosmic Probe into Energy Capacities by 2077',
    fontsize=16, weight='bold', pad=20
)

ax.legend(
    wedges, energy_sources, title="Power Origins",
    loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10
)

plt.tight_layout()
plt.show()