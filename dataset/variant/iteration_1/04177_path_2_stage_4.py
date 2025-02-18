import matplotlib.pyplot as plt
import numpy as np

# Ice cream flavors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Butter Pecan']

# Seasonal flavor popularity percentages
winter_popularity = [20, 18, 12, 10, 15, 17]
summer_popularity = [10, 15, 22, 8, 10, 9]
fall_popularity = [18, 17, 15, 14, 10, 11]

colors = plt.cm.tab10(np.linspace(0, 1, len(flavors)))

fig, axs = plt.subplots(1, 3, figsize=(14, 5))
seasonal_popularities = [winter_popularity, summer_popularity, fall_popularity]

for i, ax in enumerate(axs):
    wedges, autotexts = ax.pie(seasonal_popularities[i], colors=colors,
                                      startangle=140, pctdistance=0.85,
                                      wedgeprops=dict(edgecolor='w', width=0.3))
    
    # Remove text labels: both pie labels and percentages removed
    for text in autotexts:
        text.set_text('')  # Clearing text labels

fig.tight_layout()
plt.show()