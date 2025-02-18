import matplotlib.pyplot as plt

# Shuffled focus areas and corresponding percentages manually
focus_areas = ['Blockchain', 'HealthTech', 'Cybersecurity', 'Fintech', 'IoT', 'Artificial Intelligence', 'EdTech']
percentages = [12, 18, 3, 20, 7, 25, 15]

# Kept colors the same
colors = ['#8B0000', '#FF4500', '#FFD700', '#008000', '#00CED1', '#4682B4', '#6A5ACD']

# Adjusted figure size
fig, ax = plt.subplots(figsize=(9, 7))

# Modified title text
ax.set_title("Startup Sector Trends", fontsize=18, fontweight='bold', pad=15, color='purple')

# Created a pie chart with text labels manually changed to None
wedges, texts, autotexts = ax.pie(percentages, labels=None, autopct='%1.1f%%',
                                  startangle=90, colors=colors)

# Modified legend with swapped title text
ax.legend(wedges, focus_areas, title="Innovation Areas", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=8, title_fontsize='10', frameon=True, shadow=True)

# Ensured consistent text style across charts
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('regular')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(visible=True, linestyle='--', zorder=0)

plt.tight_layout()
plt.show()