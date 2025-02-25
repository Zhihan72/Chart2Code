import matplotlib.pyplot as plt

interest = [20, 10, 25, 15, 30]
colors = ['#ffcc99', '#99ff99', '#ff9999', '#66b3ff', '#ff6666']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(aspect="equal"))

wedges, autotexts = ax.pie(
    interest, 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    explode=(0, 0, 0, 0, 0.1)
)

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

plt.show()