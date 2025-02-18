import matplotlib.pyplot as plt
import numpy as np

# Define decades from 1960 to 2020
decades = np.arange(1960, 2030, 10)

# Artificial data for various music genres
pop_music = np.array([10, 20, 25, 30, 32, 35, 40])
rock_music = np.array([5, 15, 20, 25, 26, 27, 29])
hiphop_music = np.array([0, 0, 5, 10, 15, 20, 25])
jazz_music = np.array([20, 18, 15, 10, 7, 5, 3])

# Plot the line chart
plt.figure(figsize=(14, 8))

# Plot data for each genre with styles
plt.plot(decades, pop_music, marker='o', linestyle='-', color='salmon', linewidth=2, label='Pop')
plt.plot(decades, rock_music, marker='^', linestyle='--', color='dodgerblue', linewidth=2, label='Rock')
plt.plot(decades, hiphop_music, marker='s', linestyle='-.', color='orange', linewidth=2, label='Hip Hop')
plt.plot(decades, jazz_music, marker='p', linestyle='-', color='purple', linewidth=2, label='Jazz')

# Set the title and labels
plt.title('Evolution of Music Genres in Radio Airplay (1960 - 2020)', fontsize=18, fontweight='bold')
plt.xlabel('Decade', fontsize=14)
plt.ylabel('Percentage of Radio Airplay', fontsize=14)

# Add a legend
plt.legend(loc='upper left', fontsize=12, title='Music Genres')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate significant points
highlight_year = 2020
pop_2020 = pop_music[-1]
plt.annotate('Peak Pop Music Airplay', 
             xy=(highlight_year, pop_2020),
             xytext=(highlight_year - 20, pop_2020 + 5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), 
             fontsize=11, color='black', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'))

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()