import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

electric_cars = [50, 60, 55, 110, 75, 90, 210, 140, 170, 260, 390, 320, 470, 560, 660, 770, 1160, 890, 1470, 1020, 1310]
electric_bikes = [30, 40, 35, 50, 95, 70, 120, 150, 280, 190, 230, 340, 410, 490, 580, 680, 1040, 790, 910, 1330, 1180]
electric_buses = [10, 5, 15, 30, 45, 20, 60, 80, 130, 100, 160, 200, 250, 310, 450, 380, 530, 620, 830, 950, 720]

ev_data = np.vstack([electric_cars, electric_bikes, electric_buses])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, ev_data, colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.85)

ax.set_title('EV Adoption\n2010-30', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Num of EVs', fontsize=14)

total_evs = [sum(x) for x in zip(electric_cars, electric_bikes, electric_buses)]
ax.plot(years, total_evs, color='black', linewidth=2)

for idx, ev_count in enumerate([electric_cars, electric_bikes, electric_buses]):
    ax.annotate(f'{ev_count[-1]:,}', xy=(years[-1], sum(ev_data[:, -1])-sum(ev_data[:idx, -1])), 
                xytext=(years[-1]+0.5, sum(ev_data[:, -1])-sum(ev_data[:idx, -1])+50),
                textcoords='offset points', va='center', fontsize=10)

plt.tight_layout()
plt.show()