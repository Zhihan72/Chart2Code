import matplotlib.pyplot as plt

styles = [
    'Modern', 'Classical', 'Art Deco', 'Gothic', 'Futuristic',
    'Baroque', 'Renaissance', 'Neoclassical', 'Minimalist', 'Brutalism', 'Romanesque'
]

percentages = [22.0, 14.0, 10.0, 9.0, 8.0, 5.5, 6.0, 5.0, 6.0, 7.5, 7.0]
total = sum(percentages)
correction = 100 - total
percentages[-1] += correction

assert abs(sum(percentages) - 100) < 1e-9, "Percentages must sum up to 100."

colors = plt.cm.viridis([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.15, 0.25])

explode = tuple(0.1 if p >= 10 else 0 for p in percentages)

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=styles,
    autopct=lambda pct: f'{pct:.1f}%',
    startangle=140,
    colors=colors,
    explode=explode
)

plt.setp(autotexts, size=10, weight='bold', color='white')
plt.setp(texts, size=10)

ax.set_title(
    'Architectural Styles Distribution in Architectura City',
    fontsize=14,
    fontweight='bold'
)

plt.show()