import matplotlib.pyplot as plt

# Updated data for the fleet composition
ship_types = ['Exploration', 'Defense', 'Cargo', 'Scientific', 'Diplomatic', 'Medical', 'Transport']
percentages = [20, 30, 15, 10, 10, 5, 10]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors, labels=ship_types)

ax.set_title("Galactic Federation Fleet Composition\nShip Types and Capabilities", fontsize=14, fontweight='bold')

plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=9)

ax.legend(wedges, ship_types, title="Ship Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()