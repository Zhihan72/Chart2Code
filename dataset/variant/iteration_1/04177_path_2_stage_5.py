import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Butter Pecan']

# Seasonal flavor popularity percentages
winter_popularity = [20, 18, 12, 10, 15, 17]
summer_popularity = [10, 15, 22, 8, 10, 9]
fall_popularity = [18, 17, 15, 14, 10, 11]

colors = plt.cm.viridis(np.linspace(0, 1, len(flavors)))

fig, axs = plt.subplots(1, 3, figsize=(14, 5))
seasonal_popularities = [winter_popularity, summer_popularity, fall_popularity]

for i, ax in enumerate(axs):
    wedges, autotexts = ax.pie(seasonal_popularities[i], colors=colors,
                               startangle=90, pctdistance=0.75,
                               wedgeprops=dict(edgecolor='black', linestyle='-', linewidth=1.5, hatch='\\'))
    
    # Adding grid lines within the subplot
    ax.grid(linestyle='--', linewidth=0.5)

    # Legend added for each pie chart
    ax.legend(flavors, loc='upper left', bbox_to_anchor=(0.9, 1))

fig.tight_layout()
plt.show()