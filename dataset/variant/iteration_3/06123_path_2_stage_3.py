import matplotlib.pyplot as plt

focus_areas = ['IoT', 'Cybersecurity', 'Blockchain', 'Artificial Intelligence', 'Fintech', 'HealthTech', 'EdTech']
percentages = [7, 3, 12, 25, 20, 18, 15]

# Changed original colors to a different palette
colors = ['#8B0000', '#FF4500', '#FFD700', '#008000', '#00CED1', '#4682B4', '#6A5ACD']

# Altered figure size to make the chart look different
fig, ax = plt.subplots(figsize=(9, 7))

# Changed startangle and removed label lines for a different view
wedges, texts, autotexts = ax.pie(percentages, labels=None, autopct='%1.1f%%',
                                  startangle=90, colors=colors)

# Altered the title style
ax.set_title("Tech Startup Distribution by Focus", fontsize=18, fontweight='bold', pad=15, color='purple')

# Changed legend position and style
ax.legend(wedges, focus_areas, title="Focus Areas", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=8, title_fontsize='10', frameon=True, shadow=True)

# Modified autotexts for a new look
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('regular')

# Introduced grid and border alterations
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(visible=True, linestyle='--', zorder=0)

plt.tight_layout()
plt.show()