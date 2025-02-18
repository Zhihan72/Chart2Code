import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
hobbies = ['Coding', 'Cooking', 'Gardening', 'Hiking', 'Reading']

interest_coding = np.array([6, 7, 8, 8, 9, 9, 7, 6, 7, 8, 8, 9])
interest_cooking = np.array([5, 6, 6, 8, 9, 9, 8, 7, 6, 6, 7, 8])
interest_gardening = np.array([4, 5, 6, 7, 8, 9, 9, 7, 6, 5, 4, 4])
interest_hiking = np.array([7, 6, 7, 9, 10, 9, 8, 7, 7, 7, 6, 7])
interest_reading = np.array([8, 8, 9, 9, 10, 10, 8, 8, 9, 10, 10, 9])

interest_data = {
    'Coding': interest_coding,
    'Cooking': interest_cooking,
    'Gardening': interest_gardening,
    'Hiking': interest_hiking,
    'Reading': interest_reading
}

# Colors have been shuffled
colors = {
    'Coding': 'red',
    'Cooking': 'purple',
    'Gardening': 'blue',
    'Hiking': 'green',
    'Reading': 'orange'
}

fig, ax = plt.subplots(figsize=(14, 7))
for hobby, interest in interest_data.items():
    ax.plot(months, interest, marker='o', label=hobby, color=colors[hobby], linewidth=2, linestyle='-')

peak_annotations = {
    'Coding': [(4, 'Hackathon Month')],
    'Cooking': [(5, 'Cooking Competition')],
    'Gardening': [(8, 'Harvest Month')],
    'Hiking': [(4, 'Spring Break'), (5, 'Perfect Weather')],
    'Reading': [(9, 'Book Club Month')]
}

for hobby, peaks in peak_annotations.items():
    for m_idx, label in peaks:
        ax.annotate(label,
                    xy=(months[m_idx-1], interest_data[hobby][m_idx-1]),
                    xytext=(months[m_idx-1], interest_data[hobby][m_idx-1] + 1),
                    arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                    fontsize=10, color=colors[hobby])

ax.set_title('Community Interest Levels in Hobbies Over 2023', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Interest Level (1-10)', fontsize=12)
ax.set_xticks(months)
ax.set_yticks(np.arange(0, 11, 1))
ax.legend(loc='upper right', fontsize=10, title='Hobbies')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()