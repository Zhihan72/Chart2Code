import matplotlib.pyplot as plt

# Initial budget (in million dollars)
initial_budget = 200

# 2025 grant changes (in million dollars)
grant_changes = {
    'Q. Alg.': 25,
    'Q. Hardware': -10,
    'Software Dev.': 15,
    'Q. Crypto.': -5,
    'Int. Collab.': 30,
    'Edu. & Outreach': 5
}

# Calculate cumulative values
cumulative_values = [initial_budget]
labels = ['Initial']
for sector, change in grant_changes.items():
    cumulative_values.append(cumulative_values[-1] + change)
    labels.append(sector)

# Determine colors
bar_colors = ['#8fd175' if change >= 0 else '#d17575' for change in grant_changes.values()]

# Create plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot bars
for i in range(1, len(cumulative_values)):
    start_val = cumulative_values[i-1]
    end_val = cumulative_values[i]
    ax.bar(labels[i], end_val - start_val, bottom=start_val, color=bar_colors[i-1], edgecolor='black')
    ax.plot([i-1, i], [start_val, end_val], color='gray', linewidth=1.5)

# Labels and title
plt.xlabel('Sectors', fontsize=12)
plt.ylabel('Grants ($M)', fontsize=12)
plt.title('Quantum Research Grants: 2025\nBudget Changes', fontsize=14, fontweight='bold', pad=20)

# Annotate changes
for i in range(1, len(cumulative_values)):
    change_val = grant_changes[labels[i]]
    ax.text(i, cumulative_values[i] + (2 if change_val > 0 else -3),
            f"{change_val:+}M", ha='center', va='bottom' if change_val > 0 else 'top',
            color='black', fontsize=10, fontweight='bold')

# Annotate cumulative values
for i in range(len(cumulative_values)):
    ax.text(i, cumulative_values[i] + 2, f"{cumulative_values[i]}M", ha='center',
            va='bottom', color='black', fontsize=10)

# Add grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust x-axis labels
plt.xticks(rotation=30, ha='right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()