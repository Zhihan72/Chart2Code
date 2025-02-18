import matplotlib.pyplot as plt

initiatives = ['Disaster Management', 'Wellbeing', 'Crisis Support', 'Pure Water', 'Eco Conservation', 'Education Access', 'Technology for Good']
investment_percentages = [30, 25, 20, 15, 10, 10, 5]

color = '#20B2AA'
explode = (0.1, 0, 0, 0, 0, 0, 0)

plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    investment_percentages, 
    labels=initiatives, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=[color] * len(initiatives),
    explode=explode,
    wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'width': 0.3}  # Adjusted width for donut effect
)

for text in texts:
    text.set_fontsize(12)
    text.set_weight('bold')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_weight('bold')
    autotext.set_color('black')

plt.title("Charitable Group's Fund Allocation\nin Social Efforts (2023)", fontsize=16, fontweight='bold', pad=20)

plt.legend(wedges, initiatives, title="Focus Areas", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

plt.tight_layout()

plt.show()