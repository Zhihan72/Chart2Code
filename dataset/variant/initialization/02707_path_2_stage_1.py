import matplotlib.pyplot as plt

initial_grant_budget = 200
grant_changes = {
    'Quantum Algorithms': 25,
    'Quantum Hardware': -10,
    'Software Development': 15,
    'Quantum Cryptography': -5,
    'International Collaboration': 30,
    'Education & Outreach': 5
}

cumulative_grants = [initial_grant_budget]
grant_labels = ['Initial Budget']
for sector, change in grant_changes.items():
    cumulative_grants.append(cumulative_grants[-1] + change)
    grant_labels.append(sector)

bar_colors = ['#8fd175' if change >= 0 else '#d17575' for change in grant_changes.values()]

fig, ax = plt.subplots(figsize=(12, 7))

for i in range(1, len(cumulative_grants)):
    start_value = cumulative_grants[i-1]
    end_value = cumulative_grants[i]
    ax.bar(grant_labels[i], end_value - start_value, bottom=start_value, color=bar_colors[i-1], edgecolor='black')
    ax.plot([i-1, i], [start_value, end_value], color='gray', linewidth=1.5)

plt.xlabel('Research Sectors', fontsize=12)
plt.ylabel('Grants (Million $)', fontsize=12)
plt.title('The Evolution of Quantum Computing\nResearch Grants: 2025 Budget Adjustments', fontsize=14, fontweight='bold', pad=20)

for i in range(1, len(cumulative_grants)):
    change_value = grant_changes[grant_labels[i]]
    ax.text(i, cumulative_grants[i] + (2 if change_value > 0 else -3), 
            f"{change_value:+}M", ha='center', va='bottom' if change_value > 0 else 'top', 
            color='black', fontsize=10, fontweight='bold')

for i in range(len(cumulative_grants)):
    ax.text(i, cumulative_grants[i] + 2, f"{cumulative_grants[i]}M", ha='center', 
            va='bottom', color='black', fontsize=10)

plt.xticks(rotation=30, ha='right', fontsize=10)

plt.tight_layout()

plt.show()