import matplotlib.pyplot as plt
import numpy as np

worlds = ['Middle-earth', 'Westeros', 'Star Wars Galaxy', 'Star Trek Universe', 'Harry Potter World', 'Narnia', 'Discworld']
languages = [8, 12, 6, 21, 10, 12, 7]  # Manually shuffled values

# Sorting the data by number of languages in descending order
sorted_indices = np.argsort(languages)[::-1]
sorted_worlds = [worlds[i] for i in sorted_indices]
sorted_languages = [languages[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 7))
ax.barh(sorted_worlds, sorted_languages, color='#e6194b', edgecolor='black')
ax.set_xlim(0, max(sorted_languages) + 5)
ax.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()