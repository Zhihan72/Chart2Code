import numpy as np
import matplotlib.pyplot as plt

planets = ['Zog', 'Vega', 'Orion']
cuisines = ['Martian Delicacies', 'Saturnine Savories']
popularity_scores = np.array([
    [70, 90],
    [60, 95],
    [80, 70]
])

fig, ax = plt.subplots(figsize=(10, 5))

# Plot horizontal bars for each planet for each cuisine
for i, (planet, score_row) in enumerate(zip(planets, popularity_scores)):
    offsets = np.arange(len(cuisines))
    ax.barh(y=offsets + i*(len(cuisines)+1), width=score_row, height=0.6, label=planet, color='blue', alpha=0.8)

# Set y-ticks to label each cuisine and planet group
ax.set_yticks(offsets + (len(planets)-1)*(len(cuisines)+1)/2)
ax.set_yticklabels(cuisines)

# Add legend and show plot
ax.legend(title='Planets')
plt.xlabel('Popularity Scores')
plt.title('Popularity Scores of Cuisines on Different Planets')

plt.show()