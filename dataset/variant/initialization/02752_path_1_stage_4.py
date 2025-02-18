import matplotlib.pyplot as plt

platforms = ['FB', 'IG', 'YT', 'TW', 'SC', 'TikTok', 'In']
user_percentages = [25, 22, 15, 10, 8, 18, 2]
colors = ['#99FF99', '#FF9999', '#FFCC99', '#FFD700', '#FFB6C1', '#66B3FF', '#8A2BE2']

plt.figure(figsize=(9, 8))  # Slightly altered figure size
wedges, texts, autotexts = plt.pie(
    user_percentages, 
    labels=platforms, 
    colors=colors, 
    startangle=100,  # Changed the start angle
    autopct='%1.1f%%', 
    pctdistance=0.80  # Slightly adjust the text position
)

# Iterate over the labels to alter styles randomly
for autotext in autotexts:
    autotext.set_color('blue')  # Alter color from black to blue
    autotext.set_fontweight('normal')  # Change weight from bold to normal

plt.title('Social Media User Engagement Analysis', fontsize=18, fontweight='normal', pad=25)

# Changed legend style
plt.legend(wedges, platforms, title='Platforms', loc='upper right', bbox_to_anchor=(1, 1))

plt.grid(True, linestyle='--', linewidth=0.5)  # Added grid with dashed lines

plt.axis('equal')
plt.tight_layout()
plt.show()