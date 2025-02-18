import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

energy_sources = ['Hydropower', 'Wind', 'Fossil Fuels', 'Solar']
consumption_2023 = [30, 25, 20, 10]
consumption_2022 = [28, 24, 22, 11]

gradients = [cm.get_cmap('YlOrRd')(np.linspace(0.2, 0.8, len(energy_sources))),
             cm.get_cmap('GnBu')(np.linspace(0.2, 0.8, len(energy_sources)))]

fig, axs = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("Comparative Energy use in EcoVille: 2022 vs. 2023", fontsize=16, fontweight='bold', y=0.98)

# Reverse the order of the data to swap the subplots
for ax, consumption, year, gradient in zip(axs, [consumption_2022, consumption_2023], [2022, 2023], gradients[::-1]):
    wedges, texts, autotexts = ax.pie(
        consumption, 
        labels=['Solar', 'Fossil Fuels', 'Hydropower', 'Wind'],  # Shuffled labels
        autopct='%1.1f%%', 
        startangle=90,  # Changed start angle
        colors=[gradient[i] for i in range(len(energy_sources))],
        wedgeprops=dict(width=0.2, edgecolor='gray'),  # Altered wedge width and edgecolor
        pctdistance=0.75  # Changed percentage distance
    )
    
    plt.setp(autotexts, size=10, weight="bold", color='black')  # Altered auto text style
    
    centre_circle = plt.Circle((0, 0), 0.70, fc='ivory')  # Changed center circle color
    ax.add_artist(centre_circle)

    ax.set_title(f"{year} Renewable Energy Sources", fontsize=13, fontweight='bold', pad=15)

fig.legend(wedges, ['Solar', 'Fossil Fuels', 'Hydropower', 'Wind'], title="Energy Types", loc="upper right", frameon=False, ncol=2)

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()