import matplotlib.pyplot as plt
import numpy as np

commodities = ['Martian Minerals', 'Earthly Technologies', 
               'Agricultural Products', 'Water Resources', 
               'Medical Supplies']
trade_volumes = [200, 150, 180, 120, 90]
trade_values = [50, 70, 55, 40, 30]

new_colors = ['#6495ED', '#FFD700', '#ADFF2F', '#FF69B4', '#00CED1']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plotting the bar chart without textual elements
bars = ax1.bar(np.arange(len(commodities)), trade_volumes, color=new_colors)

# Removing title, axis labels, and bar labels
ax1.set_xticks(np.arange(len(commodities)))

# Plotting the pie chart without textual elements
ax2.pie(trade_values, startangle=140, colors=new_colors)

plt.tight_layout()
plt.show()