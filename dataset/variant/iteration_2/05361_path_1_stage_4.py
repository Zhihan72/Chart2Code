import matplotlib.pyplot as plt
import numpy as np

companies = ['Epsilon Innovations', 'Alpha Systems', 'GammaTech', 'BetaCorp', 'Delta Ventures']
years = ['2022', '2021', '2020']
categories = ['Cybersecurity', 'AI', 'Quantum Computing', 'Robotics', 'IoT']

innovations = np.array([
    [10, 7, 12, 9, 1],    
    [11, 11, 15, 9, 5],     
    [12, 8, 13, 11, 3],     
    [8, 9, 14, 12, 2],    
    [10, 9, 11, 8, 6],     
    [13, 13, 18, 11, 4],   
    [14, 10, 12, 10, 5],    
    [11, 12, 14, 13, 7],   
    [14, 8, 16, 10, 3],    
    [9, 11, 13, 9, 2],     
    [15, 12, 20, 13, 4],   
    [10, 11, 17, 11, 6],   
    [9, 13, 15, 12, 5],   
    [13, 11, 16, 10, 4],   
    [12, 10, 14, 8, 2]  
])

fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

# Manually shuffled colors.
colors = ['#4682B4', '#FF69B4', '#FFD700', '#3CB371', '#FF6347']
year_indices = [2, 0, 1]

for i, ax in enumerate(axes):
    year_data = innovations[year_indices[i] * len(companies):(year_indices[i] + 1) * len(companies)]
    x = np.arange(len(categories))
    
    for j in range(len(companies)):
        ax.bar(x + j * 0.15, year_data[j], width=0.1, color=colors[j], align='center', label=companies[j] if i == 0 else "")
    
    ax.set_title(f"Year {years[i]} Innovations", fontsize=14)
    ax.set_xlabel("Tech Categories", fontsize=12)
    ax.set_xticks(x + 0.3)
    ax.set_xticklabels(categories, rotation=45, ha='right')
    ax.grid(True, linestyle='--', linewidth=0.5)

axes[0].set_ylabel("Innovations Count", fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, title='Firm Names')

fig.suptitle("Top Tech Competition: Firms in Techville (2020-2022)", fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()