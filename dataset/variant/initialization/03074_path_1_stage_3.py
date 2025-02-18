import matplotlib.pyplot as plt

energy_sources = ['Hydropower', 'Biomass', 'Wind', 'Solar', 'Ocean', 'Geothermal']
energy_share = [20, 15, 25, 30, 5, 5]
colors = ['#00FA9A', '#8B4513', '#87CEEB', '#FFD700', '#4682B4', '#FF6347']
explode = (0.05, 0, 0, 0.1, 0, 0)  # Altered values for slight variation

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    energy_share, labels=energy_sources, autopct='%1.1f%%',
    startangle=120, colors=colors, explode=explode, shadow=False,  # Changed shadow option to False
    textprops=dict(color='blue'), wedgeprops=dict(width=0.35, edgecolor='grey')  # Altered the width and added edgecolor
)

plt.setp(autotexts, size=9, weight="normal")  # Modified text size and weight
plt.setp(texts, size=11)

ax.set_title(
    "Future Green Energy Distribution in 2050:\nMoving Towards Sustainability", 
    fontsize=14, fontweight='normal', pad=15  # Changed size and padding
)

# Removed legend from the plot
ax.grid(visible=True, linestyle='--', color='grey')  # Added a grid

plt.tight_layout()
plt.show()