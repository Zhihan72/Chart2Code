import matplotlib.pyplot as plt

focus_areas = ['Blockchain', 'HealthTech', 'Cybersecurity', 'Fintech', 'IoT', 'Artificial Intelligence', 'EdTech']
percentages = [12, 18, 3, 20, 7, 25, 15]

# Use a single color for all wedges
single_color = '#4682B4' 

fig, ax = plt.subplots(figsize=(9, 7))
ax.set_title("Startup Sector Trends", fontsize=18, fontweight='bold', pad=15, color='purple')

# Apply the single color consistently across all data groups
wedges, texts, autotexts = ax.pie(percentages, labels=None, autopct='%1.1f%%',
                                  startangle=90, colors=[single_color]*len(focus_areas))

ax.legend(wedges, focus_areas, title="Innovation Areas", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=8, title_fontsize='10', frameon=True, shadow=True)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('regular')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(visible=True, linestyle='--', zorder=0)

plt.tight_layout()
plt.show()