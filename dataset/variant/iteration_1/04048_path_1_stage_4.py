import matplotlib.pyplot as plt

nodes = {
    'Solar': 3,
    'Wind': 6,
    'Hydro': 2,
    'Geo': 4,
    'Bio': 5,
    'Storage': 7,
    'Grid': 3,
    'Smart': 6
}

sorted_nodes = sorted(nodes.items(), key=lambda item: item[1], reverse=True)
labels, values = zip(*sorted_nodes)

plt.figure(figsize=(12, 8))
plt.bar(labels, values, color=plt.cm.plasma([val / max(values) for val in values]), edgecolor='gray', linestyle='--', hatch='/')

plt.xlabel('Parts', fontsize=12, fontstyle='italic')
plt.ylabel('Rank', fontsize=12, fontstyle='italic')
plt.title('Random Score of Energy Parts', fontsize=18, fontweight='heavy')

for i, v in enumerate(values):
    plt.text(i, v + 0.2, str(v), ha='center', va='bottom', fontstyle='italic', color='darkred', fontsize=10)

plt.xticks(rotation=30, ha='right', fontsize=10, color='darkblue')
plt.yticks(fontsize=10, color='darkblue')
plt.grid(axis='y', linestyle='-', linewidth=0.5, color='black')

plt.legend(['Components'], loc='upper right', frameon=False, fontsize=10)

plt.tight_layout()
plt.show()