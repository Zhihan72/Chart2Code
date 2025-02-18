import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

vector_art = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
pixel_art = np.array([20, 22, 25, 35, 45, 55, 60, 62, 65, 70, 72])
concept_art = np.array([50, 48, 47, 46, 45, 44, 43, 42, 40, 38, 35])
cyberpunk = np.array([10, 15, 25, 35, 50, 65, 80, 90, 95, 100, 105])
doodle_art = np.array([5, 10, 25, 40, 60, 65, 55, 45, 40, 35, 30])
retro_art = np.array([15, 17, 20, 25, 30, 33, 35, 36, 38, 40, 42])

cumulative_vector_art = vector_art
cumulative_pixel_art = cumulative_vector_art + pixel_art
cumulative_concept_art = cumulative_pixel_art + concept_art
cumulative_cyberpunk = cumulative_concept_art + cyberpunk
cumulative_doodle_art = cumulative_cyberpunk + doodle_art
cumulative_retro_art = cumulative_doodle_art + retro_art

average_popularity = (vector_art + pixel_art + concept_art + cyberpunk + doodle_art + retro_art) / 6

plt.figure(figsize=(15, 8))

# Apply a single color '#1f77b4' to all data groups
single_color = '#1f77b4'
plt.fill_between(years, 0, cumulative_vector_art, color=single_color, label='Vector', alpha=0.6)
plt.fill_between(years, cumulative_vector_art, cumulative_pixel_art, color=single_color, label='Pixel', alpha=0.6)
plt.fill_between(years, cumulative_pixel_art, cumulative_concept_art, color=single_color, label='Concept', alpha=0.6)
plt.fill_between(years, cumulative_concept_art, cumulative_cyberpunk, color=single_color, label='Cyber', alpha=0.6)
plt.fill_between(years, cumulative_cyberpunk, cumulative_doodle_art, color=single_color, label='Doodle', alpha=0.6)
plt.fill_between(years, cumulative_doodle_art, cumulative_retro_art, color=single_color, label='Retro', alpha=0.6)

plt.plot(years, average_popularity, color='grey', linewidth=1, linestyle='-.', label='Avg Popularity', marker='o')

plt.title('Art Trends (2010-2020)', fontsize=15, fontweight='bold', pad=15)
plt.xlabel('Yr', fontsize=11)
plt.ylabel('Popularity', fontsize=11)

plt.xticks(years, rotation=30, ha='center')
plt.grid(visible=True, linestyle=':', alpha=0.7, axis='x')
plt.legend(loc='upper center', title='Arts', fontsize=9, frameon=True)
plt.tight_layout()
plt.show()