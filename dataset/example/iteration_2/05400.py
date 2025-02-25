import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart visualizes the evolution of electric vehicle (EV) adoption in a fictional city "Electrotown" from 2010 to 2030. Each year shows the number of electric cars, electric bikes, and electric buses introduced.

# Years from 2010 to 2030
years = np.arange(2010, 2031)

# Number of EVs for each category over the years
electric_cars = [50, 55, 60, 75, 90, 110, 140, 170, 210, 260, 320, 390, 470, 560, 660, 770, 890, 1020, 1160, 1310, 1470]
electric_bikes = [30, 35, 40, 50, 70, 95, 120, 150, 190, 230, 280, 340, 410, 490, 580, 680, 790, 910, 1040, 1180, 1330]
electric_buses = [5, 10, 15, 20, 30, 45, 60, 80, 100, 130, 160, 200, 250, 310, 380, 450, 530, 620, 720, 830, 950]

# Create arrays for plotting
ev_data = np.vstack([electric_cars, electric_bikes, electric_buses])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, ev_data, labels=['Electric Cars', 'Electric Bikes', 'Electric Buses'],
             colors=['#66c2a5', '#fc8d62', '#8da0cb'], alpha=0.85)

# Set the title and labels
ax.set_title('Electrotown Electric Vehicle Adoption\n2010-2030', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of EVs', fontsize=14)

# Add grid for readability
ax.grid(True, linestyle='--', alpha=0.5)

# Add legend
ax.legend(loc='upper left', title='EV Types', bbox_to_anchor=(1, 1))

# Overlay line plot for total EVs
total_evs = [sum(x) for x in zip(electric_cars, electric_bikes, electric_buses)]
ax.plot(years, total_evs, color='black', linewidth=2, label='Total EVs')

# Annotate key points
for idx, ev_count in enumerate([electric_cars, electric_bikes, electric_buses]):
    ax.annotate(f'{ev_count[-1]:,}', xy=(years[-1], sum(ev_data[:, -1])-sum(ev_data[:idx, -1])), 
                xytext=(years[-1]+0.5, sum(ev_data[:, -1])-sum(ev_data[:idx, -1])+50),
                textcoords='offset points', va='center', fontsize=10)

# Improve layout
plt.tight_layout()
plt.show()