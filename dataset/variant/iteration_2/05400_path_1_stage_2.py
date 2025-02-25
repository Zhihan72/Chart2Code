import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2031)

electric_cars = [50, 55, 60, 75, 90, 110, 140, 170, 210, 260, 320, 390, 470, 560, 660, 770, 890, 1020, 1160, 1310, 1470]
electric_bikes = [30, 35, 40, 50, 70, 95, 120, 150, 190, 230, 280, 340, 410, 490, 580, 680, 790, 910, 1040, 1180, 1330]
electric_buses = [5, 10, 15, 20, 30, 45, 60, 80, 100, 130, 160, 200, 250, 310, 380, 450, 530, 620, 720, 830, 950]

# New data series
electric_trucks = [10, 15, 20, 25, 35, 50, 70, 95, 120, 155, 190, 235, 290, 355, 430, 515, 610, 715, 830, 955, 1090]
electric_scooters = [10, 12, 14, 18, 22, 26, 31, 37, 44, 52, 61, 71, 82, 94, 107, 121, 136, 152, 169, 187, 206]

ev_data = np.vstack([electric_cars, electric_bikes, electric_buses, electric_trucks, electric_scooters])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, ev_data, labels=['Cars', 'Bikes', 'Buses', 'Trucks', 'Scooters'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854'], alpha=0.85)

ax.set_title('EV Adoption in Electrotown', fontsize=16, fontweight='bold')
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('EV Count', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(loc='upper left', title='Types', bbox_to_anchor=(1, 1))

total_evs = [sum(x) for x in zip(electric_cars, electric_bikes, electric_buses, electric_trucks, electric_scooters)]
ax.plot(years, total_evs, color='black', linewidth=2, label='Total')

for idx, ev_count in enumerate([electric_cars, electric_bikes, electric_buses, electric_trucks, electric_scooters]):
    ax.annotate(f'{ev_count[-1]:,}', xy=(years[-1], sum(ev_data[:, -1])-sum(ev_data[:idx, -1])), 
                xytext=(years[-1]+0.5, sum(ev_data[:, -1])-sum(ev_data[:idx, -1])+50),
                textcoords='offset points', va='center', fontsize=10)

plt.tight_layout()
plt.show()