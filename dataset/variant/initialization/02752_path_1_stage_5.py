import matplotlib.pyplot as plt

platforms = ['FB', 'IG', 'YT', 'TW', 'SC', 'TikTok', 'In']
user_percentages = [25, 22, 15, 10, 8, 18, 2]
consistent_color = '#66B3FF'  # Using a single color consistently

plt.figure(figsize=(9, 8))
wedges, texts, autotexts = plt.pie(
    user_percentages, 
    labels=platforms, 
    colors=[consistent_color] * len(platforms),  # Apply consistent color
    startangle=100,  
    autopct='%1.1f%%', 
    pctdistance=0.80 
)

for autotext in autotexts:
    autotext.set_color('blue')
    autotext.set_fontweight('normal')

plt.title('Social Media User Engagement Analysis', fontsize=18, fontweight='normal', pad=25)

plt.legend(wedges, platforms, title='Platforms', loc='upper right', bbox_to_anchor=(1, 1))

plt.grid(True, linestyle='--', linewidth=0.5)

plt.axis('equal')
plt.tight_layout()
plt.show()