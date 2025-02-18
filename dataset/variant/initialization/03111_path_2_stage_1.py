import matplotlib.pyplot as plt
import numpy as np

# Wind directions
directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

# Wind frequencies
spring_winds = np.array([8, 12, 15, 10, 6, 4, 3, 5])
summer_winds = np.array([5, 6, 8, 15, 18, 10, 4, 2])
autumn_winds = np.array([3, 5, 10, 8, 9, 14, 17, 10])
winter_winds = np.array([10, 7, 4, 3, 2, 5, 12, 18])

wind_data = [spring_winds, summer_winds, autumn_winds, winter_winds]

# Angles for plotting
angles = np.linspace(0, 2 * np.pi, len(directions), endpoint=False).tolist()
angles += angles[:1]  # Close the plot

# Append the first data point for closure
for i in range(len(wind_data)):
    wind_data[i] = np.append(wind_data[i], wind_data[i][0])

fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))

# Colors and shortened labels
colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D']
labels = ['Spr', 'Sum', 'Aut', 'Win']

# Plot data
for data, color, label in zip(wind_data, colors, labels):
    ax.plot(angles, data, marker='o', linestyle='-', color=color, linewidth=2, label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Annotate max value for each season
for data, label in zip(wind_data, labels):
    max_idx = np.argmax(data[:-1])
    ax.annotate(f'{label} Max: {data[max_idx]}', xy=(angles[max_idx], data[max_idx]), 
                xytext=(angles[max_idx] + 0.1, data[max_idx] + 2), textcoords='data', 
                arrowprops=dict(arrowstyle="->", color='gray'), ha='center', fontsize=10, color='black')

# Customize appearance
ax.set_xticks(angles[:-1])
ax.set_xticklabels(directions, fontsize=12)
ax.set_yticklabels([])
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

ax.set_title("Wind Patterns in Mystic Isles", fontsize=16, fontweight='bold', pad=30)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10, title='Seasons', title_fontsize='13')

plt.tight_layout()
plt.show()