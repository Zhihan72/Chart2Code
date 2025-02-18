import matplotlib.pyplot as plt

commodities = ['Martian Minerals', 'Earthly Technologies', 
               'Agricultural Products', 'Water Resources', 
               'Medical Supplies']
trade_volumes = [200, 150, 180, 120, 90]
new_colors = ['#6495ED', '#FFD700', '#ADFF2F', '#FF69B4', '#00CED1']

fig, ax1 = plt.subplots(1, 1, figsize=(8, 7))

wedges, texts = ax1.pie(trade_volumes, colors=new_colors, wedgeprops=dict(width=0.3))
ax1.set(aspect="equal")

plt.legend(wedges, commodities, title="Commodities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.show()