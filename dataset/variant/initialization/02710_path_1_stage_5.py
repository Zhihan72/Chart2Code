import matplotlib.pyplot as plt

regions_altered = ['Africa', 'Latin America & Caribbean', 'Oceania', 'Asia', 'Atlantis', 'Europe', 'Antarctica', 'North America']
usage_percentages_altered = [12, 7, 3, 53, 0.9, 15, 0.1, 10]

# Shuffled colors list without using random
colors = ['#FFCC99', '#8A2BE2', '#A9A9A9', '#99FF99', '#66B2FF', '#FFD700', '#FF6347', '#FF9999']

explode = (0, 0.1, 0, 0.1, 0, 0, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(usage_percentages_altered, labels=regions_altered, autopct='%1.1f%%', startangle=45, colors=colors,
        explode=explode, shadow=False, wedgeprops={'edgecolor': 'black'})

plt.title('2023 Global Net User Distribution by Region', fontsize=14, fontweight='normal')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.gca().set_prop_cycle(None)
plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['right'].set_linewidth(2)
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['bottom'].set_linewidth(2)

plt.tight_layout()
plt.show()