import matplotlib.pyplot as plt

# Randomly altered textual elements
regions_altered = ['Europe', 'Latin America & Caribbean', 'Asia', 'Antarctica', 'Oceania', 'North America', 'Atlantis', 'Africa']
usage_percentages_altered = [15, 7, 53, 0.1, 3, 10, 0.9, 12]
colors = ['#66B2FF', '#FFD700', '#FF9999', '#A9A9A9', '#FF6347', '#FFCC99', '#8A2BE2', '#99FF99']
explode = (0, 0, 0.1, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
plt.pie(usage_percentages_altered, labels=regions_altered, autopct='%1.1f%%', startangle=90, colors=colors, 
        explode=explode, shadow=True)

# Randomly altered title
plt.title('2023 Regional Share of Net Users Worldwide', fontsize=16, fontweight='bold')
plt.axis('equal')

plt.tight_layout()
plt.show()