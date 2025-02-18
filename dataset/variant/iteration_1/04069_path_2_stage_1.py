import numpy as np
import matplotlib.pyplot as plt

# Define performance aspects
aspects = ['Speed', 'Accuracy', 'Memory Usage', 'Battery Life', 'Latency', 'Scalability']
num_aspects = len(aspects)

# Performance scores including an additional Company E
companyA_scores = [85, 70, 60, 75, 90, 65]
companyB_scores = [80, 75, 70, 65, 85, 60]
companyC_scores = [75, 80, 85, 70, 80, 75]
companyD_scores = [70, 65, 80, 80, 75, 85]
companyE_scores = [88, 77, 69, 74, 91, 67]  # New company data

# Combine into a data array
data = [companyA_scores, companyB_scores, companyC_scores, companyD_scores, companyE_scores]

# Names and colors including Company E
names = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
colors = ['#2E8B57', '#FF6347', '#1E90FF', '#FFD700', '#FF69B4']  # Added color for Company E

# Calculate angles for the radar plot
angles = np.linspace(0, 2 * np.pi, num_aspects, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each company's data
for scores, name, color in zip(data, names, colors):
    scores += scores[:1]
    ax.fill(angles, scores, color=color, alpha=0.25, label=name)
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color=color)

# Customize the radar chart
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(aspects, fontsize=10)
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 20))
ax.set_yticklabels(map(str, range(0, 101, 20)), fontsize=8)

# Title and legend setup
plt.title('Tech Giant Performance Comparison in 2023\nEvaluating Key Performance Metrics', size=15, color='navy', y=1.1, ha='center')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), title="Companies")

# Automatically adjust layout for better clarity
plt.tight_layout()

# Show the plot
plt.show()