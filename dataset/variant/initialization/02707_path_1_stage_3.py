import matplotlib.pyplot as plt

initial_budget = 200

grant_changes = {
    'Q. Alg.': 25,
    'Q. Hardware': -10,
    'Software Dev.': 15,
    'Q. Crypto.': -5,
    'Int. Collab.': 30,
    'Edu. & Outreach': 5,
    'Q. Networking': 20,
    'Q. Error Reduction': -8
}

cumulative_values = [initial_budget]
labels = ['Initial']
for sector, change in grant_changes.items():
    cumulative_values.append(cumulative_values[-1] + change)
    labels.append(sector)

bar_colors = ['#8fd175' if change >= 0 else '#d17575' for change in grant_changes.values()]

fig, ax = plt.subplots(figsize=(12, 7))

for i in range(1, len(cumulative_values)):
    start_val = cumulative_values[i-1]
    end_val = cumulative_values[i]
    ax.barh(labels[i], end_val - start_val, left=start_val, color=bar_colors[i-1], edgecolor='black')
    ax.plot([start_val, end_val], [i-1, i-1], color='gray', linewidth=1.5)

plt.ylabel('Sectors', fontsize=12)
plt.xlabel('Grants ($M)', fontsize=12)
plt.title('Quantum Research Grants: 2025\nBudget Changes', fontsize=14, fontweight='bold', pad=20)

for i in range(1, len(cumulative_values)):
    change_val = grant_changes[labels[i]]
    ax.text(cumulative_values[i] + (2 if change_val > 0 else -3), i-1, 
            f"{change_val:+}M", ha='left' if change_val > 0 else 'right', 
            va='center', color='black', fontsize=10, fontweight='bold')

for i in range(len(cumulative_values)):
    ax.text(cumulative_values[i] + 2, i-1, f"{cumulative_values[i]}M", 
            ha='left', va='center', color='black', fontsize=10)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()