import matplotlib.pyplot as plt

initiatives = ['Edu', 'Health', 'Relief', 'Water', 'Env']
investment_percentages = [30, 25, 20, 15, 10]
colors = ['#FA8072', '#20B2AA', '#FFD700', '#4682B4', '#9ACD32']

explode = (0, 0.1, 0, 0, 0)

plt.figure(figsize=(9, 6))
wedges, _, autotexts = plt.pie(
    investment_percentages, 
    labels=initiatives, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode,
    wedgeprops={'edgecolor': 'gray', 'linestyle': '--'}
)

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_fontweight('normal')
    autotext.set_color('darkblue')

plt.title("Investment in Initiatives (2023)", fontsize=14, fontweight='normal', pad=15)

plt.legend(wedges, initiatives, title="Initiatives", loc='upper right', bbox_to_anchor=(1.2, 1), fontsize=11, fancybox=True, shadow=True)

plt.tight_layout()

plt.show()