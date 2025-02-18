import matplotlib.pyplot as plt

sectors = ['Solar Power', 'Wind Power', 'Hydroelectric Energy', 'Geothermal Energy', 'Biomass Energy']
investment_distribution = [35, 25, 20, 10, 10]

# Shuffled colors without using random
colors = ['#4682B4', '#FFD700', '#8A2BE2', '#7CFC00', '#FF6347']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    investment_distribution, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=140,
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='w'),
    textprops=dict(color="black")
)

plt.setp(autotexts, size=10, weight="bold")

ax.set_title('Innovation in Renewable Energy:\nGlobal Sector Investment in 2040', fontsize=14, fontweight='bold', pad=20)
plt.text(0, 0, '2040', fontsize=20, ha='center', va='center', fontweight='bold', color='gray', alpha=0.5)

ax.legend(wedges, sectors, title="Energy Sectors", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.tight_layout()
plt.show()