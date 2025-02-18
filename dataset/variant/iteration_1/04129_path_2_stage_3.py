import matplotlib.pyplot as plt
import numpy as np

# Data Setup
years = np.array(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
languages = ['Python', 'JavaScript', 'Ruby', 'C++']
participants = np.array([
    [200, 150, 50, 30],
    [220, 160, 55, 35],
    [250, 170, 60, 40],
    [280, 180, 65, 45],
    [320, 200, 70, 50],
    [400, 220, 80, 60],
    [450, 240, 90, 70],
    [500, 260, 100, 80],
])

# Calculate differences from a central axis: mean of participants
mean_participants = np.mean(participants)
participants_delta = participants - mean_participants

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.35
x = np.arange(len(years))

# Plot diverging bars for each language
for i, language in enumerate(languages):
    ax.bar(x, participants_delta[:, i], width=bar_width, label=language, alpha=0.7, edgecolor='black', 
           align='center', bottom=participants_delta[:, i - 1] if i != 0 else 0)

# Custom ticks and axis settings
ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45)
ax.axhline(0, color='black', linewidth=0.8)  # Include central axis line

# Display the plot
plt.tight_layout()
plt.show()