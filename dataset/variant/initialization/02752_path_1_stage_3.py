import matplotlib.pyplot as plt

platforms = ['IG', 'TikTok', 'FB', 'YT', 'TW', 'SC', 'In']
user_percentages = [22, 18, 25, 15, 10, 8, 2]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FFB6C1', '#8A2BE2']

plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    user_percentages, 
    labels=platforms, 
    colors=colors, 
    startangle=140, 
    autopct='%1.1f%%', 
    pctdistance=0.85
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

plt.title('Social Media User Engagement', fontsize=16, fontweight='bold', pad=20)

plt.legend(wedges, platforms, title='Platforms', loc='center left', bbox_to_anchor=(1, 0.5))

plt.axis('equal')
plt.tight_layout()
plt.show()