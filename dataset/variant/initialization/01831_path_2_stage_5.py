import matplotlib.pyplot as plt

countries = ['Norway', 'Switzerland', 'Brazil', 'Iceland', 'Sweden', 
             'Finland', 'Belgium', 'Canada', 'Denmark', 'Netherlands']
consumption_kg = [9.9, 7.9, 6.1, 9, 8.2, 12, 6.8, 6.5, 8.7, 8.4]

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['lightcoral', 'skyblue', 'lightgreen', 'plum', 'khaki', 
          'lightpink', 'lightyellow', 'lightgrey', 'thistle', 'lightsalmon']
edge_colors = ['darkred', 'darkblue', 'darkgreen', 'indigo', 'goldenrod', 
               'deeppink', 'darkorange', 'dimgray', 'purple', 'darkorange']

ax.bar(countries, consumption_kg, color=colors, edgecolor=edge_colors)

ax.yaxis.grid(True, linestyle='-', linewidth=0.8, alpha=0.5)
ax.set_axisbelow(True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(1.5)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()