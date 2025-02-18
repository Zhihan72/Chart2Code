import matplotlib.pyplot as plt

sectors = ['Solar Power', 'Wind Power', 'Hydroelectric Energy', 'Geothermal Energy', 'Biomass Energy']
investment_distribution = [35, 25, 20, 10, 10]

# Modified colors, styles, and elements
colors = ['#FFD700', '#FF6347', '#8A2BE2', '#4682B4', '#7CFC00']
markers = ['D', 'o', 'v', '^', 's']  # Various markers
linestyles = ['-', '--', '-.', ':', '-.']  # Different line styles

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    investment_distribution, 
    labels=sectors, 
    autopct='%1.1f%%', 
    startangle=100,
    colors=colors, 
    wedgeprops=dict(width=0.3, edgecolor='grey', linestyle=linestyles[2]),
    textprops=dict(color="navy")
)

plt.setp(autotexts, size=11, weight="heavy")

ax.set_title('Innovation in Renewable Energy:\nGlobal Sector Investment in 2040', fontsize=16, fontweight='heavy', pad=30)

ax.legend(wedges, ['Solar', 'Wind', 'Hydro', 'Geo', 'Biomass'], title="Sectors", loc="upper right", fontsize=9, markerscale=1.5)

# Alter grid and borders
ax.grid(visible=True, linestyle=linestyles[1], linewidth=0.7, color='grey')
plt.gca().spines['top'].set_color('orange')
plt.gca().spines['right'].set_color('orange')

plt.tight_layout()
plt.show()