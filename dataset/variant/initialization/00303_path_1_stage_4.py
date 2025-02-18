import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
vector_art = np.array([50, 60, 70, 40, 35, 55, 45, 80, 65, 30, 75])
pixel_art = np.array([70, 25, 62, 20, 65, 22, 72, 45, 35, 60, 55])
concept_art = np.array([47, 42, 38, 35, 50, 43, 45, 46, 40, 48, 44])
cyberpunk = np.array([100, 25, 95, 80, 15, 50, 105, 10, 90, 65, 35])
doodle_art = np.array([5, 40, 55, 25, 65, 10, 30, 60, 35, 45, 40])

cumulative_vector_art = vector_art
cumulative_pixel_art = cumulative_vector_art + pixel_art
cumulative_concept_art = cumulative_pixel_art + concept_art
cumulative_cyberpunk = cumulative_concept_art + cyberpunk
cumulative_doodle_art = cumulative_cyberpunk + doodle_art

average_popularity = (vector_art + pixel_art + concept_art + cyberpunk + doodle_art) / 5

plt.figure(figsize=(16, 9))

plt.fill_between(years, 0, cumulative_vector_art, color='#66B2FF', label='Doodle Matrix', alpha=0.8)  # Randomly altered label
plt.fill_between(years, cumulative_vector_art, cumulative_pixel_art, color='#99FF99', label='Pixel Jam', alpha=0.6)  # Randomly altered label
plt.fill_between(years, cumulative_pixel_art, cumulative_concept_art, color='#FFCC66', label='Conceptual Fusion', alpha=0.8)  # Randomly altered label
plt.fill_between(years, cumulative_concept_art, cumulative_cyberpunk, color='#C299FF', label='Neon Vision', alpha=0.6)  # Randomly altered label
plt.fill_between(years, cumulative_cyberpunk, cumulative_doodle_art, color='#FF9999', label='Sketch Surge', alpha=0.8)  # Randomly altered label

plt.plot(years, average_popularity, color='brown', linewidth=2.5, linestyle='-', marker='o', markerfacecolor='yellow', label='Mean Style Index')  # Randomly altered title

plt.title('Fluctuations in Graphic Creations\nfrom 2010 to 2020 with Median Fame', fontsize=16, fontweight='bold', pad=20)  # Randomly altered title
plt.xlabel('Timeline', fontsize=12)  # Randomly altered label
plt.ylabel('Fame Meter', fontsize=12)  # Randomly altered label

plt.xticks(years, rotation=90, ha='center')

plt.grid(visible=True, linestyle=':', alpha=0.7, axis='both')

plt.legend(loc='upper right', title='Artistic Dynamics')  # Randomly altered legend title

plt.tight_layout()

plt.show()