import matplotlib.pyplot as plt
import numpy as np

commodities = ['Martian Minerals', 'Earthly Technologies', 
               'Agricultural Products', 'Water Resources', 
               'Medical Supplies']
trade_volumes = [200, 150, 180, 120, 90]
new_colors = ['#6495ED', '#FFD700', '#ADFF2F', '#FF69B4', '#00CED1']

fig, ax1 = plt.subplots(1, 1, figsize=(8, 7))

ax1.bar(np.arange(len(commodities)), trade_volumes, color=new_colors)
ax1.set_xticks(np.arange(len(commodities)))

plt.tight_layout()
plt.show()