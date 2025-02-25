import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2030
years = np.arange(2010, 2031)

# Randomly altered data for EVs, preserving the structure
electric_cars = [50, 60, 55, 110, 75, 90, 210, 140, 170, 260, 390, 320, 470, 560, 660, 770, 1160, 890, 1470, 1020, 1310]
electric_bikes = [30, 40, 35, 50, 95, 70, 120, 150, 280, 190, 230, 340, 410, 490, 580, 680, 1040, 790, 910, 1330, 1180]
electric_buses = [10, 5, 15, 30, 45, 20, 60, 80, 130, 100, 160, 200, 250, 310, 450, 380, 530, 620, 830, 950, 720]

ev_data = np.vstack([electric_cars, electric_bikes, electric_buses])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, ev_data, labels=['Electric Cars', 'Electric Bikes', 'Electric Buses'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.85)

ax.set_title('Electrotown Electric Vehicle Adoption\n2010-2030', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of EVs', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper left', title='EV Types', bbox_to_anchor=(1, 1))

total_evs = [sum(x) for x in zip(electric_cars, electric_bikes, electric_buses)]
ax.plot(years, total_evs, color='black', linewidth=2, label='Total EVs')

for idx, ev_count in enumerate([electric_cars, electric_bikes, electric_buses]):
    ax.annotate(f'{ev_count[-1]:,}', xy=(years[-1], sum(ev_data[:, -1])-sum(ev_data[:idx, -1])), 
                xytext=(years[-1]+0.5, sum(ev_data[:, -1])-sum(ev_data[:idx, -1])+50),
                textcoords='offset points', va='center', fontsize=10)

plt.tight_layout()
plt.show()