import matplotlib.pyplot as plt
import numpy as np

worlds = ['Middle-earth', 'Westeros', 'Star Wars', 'Harry Potter', 'Narnia', 'Discworld']
languages = [12, 8, 21, 6, 7, 10]

# Consistent color for all bars
single_color = '#4363d8'

fig, ax = plt.subplots(figsize=(12, 7))

ax.bar(worlds, languages, color=single_color)

for i, value in enumerate(languages):
    ax.text(i, value + 0.5, f'{value}', ha='center', fontsize=10, fontweight='bold', color='black')

ax.set_ylim(0, max(languages) + 5)

plt.show()