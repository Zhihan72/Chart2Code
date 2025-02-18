import matplotlib.pyplot as plt

sectors = ['Wind Power', 'Solar Power', 'Biomass Energy', 'Geothermal Energy', 'Hydroelectric Energy']  # Changed order
investment_distribution = [35, 25, 20, 10, 10]

colors = ['#FFD700', '#FF6347', '#8A2BE2', '#4682B4', '#7CFC00']
markers = ['D', 'o', 'v', '^', 's']
linestyles = ['-', '--', '-.', ':', '-.']

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

# Altered title
ax.set_title('Global Sector Investment in Renewable Resources for 2040', fontsize=16, fontweight='heavy', pad=30)

# Altered legend labels
ax.legend(wedges, ['Wind', 'Solar', 'Bio', 'Geo', 'Hydro'], title="Energy Types", loc="upper right", fontsize=9, markerscale=1.5)

ax.grid(visible=True, linestyle=linestyles[1], linewidth=0.7, color='grey')
plt.gca().spines['top'].set_color('orange')
plt.gca().spines['right'].set_color('orange')

plt.tight_layout()
plt.show()