import matplotlib.pyplot as plt
import numpy as np

marketing_strategies = ['SEO', 'Content Marketing', 'Social Media Ads', 'Email Marketing', 'Referral Programs']
quarter1 = [30, 25, 20, 15, 5]
quarter2 = [28, 22, 25, 18, 7]
quarter3 = [35, 30, 28, 20, 12]
quarter4 = [40, 35, 30, 25, 15]

quarters = np.array([quarter1, quarter2, quarter3, quarter4])

fig, ax = plt.subplots(figsize=(12, 8))
x_indices = np.arange(len(marketing_strategies))
bar_width = 0.4

colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']

# Plot the bars for each quarter
bottom_pos = np.zeros(len(marketing_strategies))
bottom_neg = np.zeros(len(marketing_strategies))

for i, quarter_data in enumerate(quarters):
    half = len(quarter_data) // 2
    pos = quarter_data[:half]       # Positive side
    neg = quarter_data[half:]       # Negative side
    
    ax.bar(x_indices[:half], pos, width=bar_width, bottom=bottom_pos[:half], color=colors[i], label=f'Quarter {i+1}')
    ax.bar(x_indices[half:], neg, width=bar_width, bottom=bottom_neg[half:], color=colors[i])

    # Update the bottom positions
    bottom_pos[:half] += pos
    bottom_neg[half:] += neg

ax.set_xticks(x_indices)
ax.set_xticklabels(marketing_strategies, rotation=45, ha='right')
ax.axhline(0, color='black', linewidth=0.8) # Central axis

plt.legend()
plt.tight_layout()
plt.show()