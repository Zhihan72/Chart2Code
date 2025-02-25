import matplotlib.pyplot as plt
import numpy as np

companies = ['Epsilon Innovations', 'Alpha Systems', 'GammaTech', 'BetaCorp', 'Delta Ventures']
years = ['2022', '2021', '2020']  # Changed order to match the new subplot arrangement
categories = ['Cybersecurity', 'AI', 'Quantum Computing', 'Robotics', 'IoT']

innovations = np.array([
    [12, 9, 15, 10, 5],    
    [8, 11, 13, 9, 4],     
    [9, 8, 12, 11, 3],     
    [10, 7, 14, 10, 2],    
    [9, 8, 13, 8, 1],      
    [14, 11, 18, 12, 6],   
    [9, 12, 14, 10, 5],    
    [11, 10, 13, 12, 4],   
    [12, 9, 16, 11, 3],    
    [11, 9, 14, 9, 2],     
    [16, 13, 20, 13, 7],   
    [10, 13, 15, 11, 6],   
    [12, 11, 15, 13, 5],   
    [14, 10, 17, 12, 4],   
    [13, 10, 16, 10, 3]    
])

fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

colors = ['#FFD700', '#3CB371', '#FF6347', '#4682B4', '#FF69B4']

# We change the order of the innovations slice assignment to match the new subplot order.
year_indices = [2, 0, 1]  # New order corresponding to indices of years: 2022, 2021, 2020

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