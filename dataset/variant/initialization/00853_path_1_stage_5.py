import matplotlib.pyplot as plt
import numpy as np

celestial_bodies = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Asteroids']
missions_data = {
    'Orbiters': [30, 40, 25, 50, 60, 10],
    'Flybys': [50, 50, 30, 40, 35, 70]
}

# Sum up the mission data for each celestial body and sort them
total_missions = [sum(x) for x in zip(*missions_data.values())]
sorted_indices = np.argsort(total_missions)

# Sorted data based on total missions
sorted_bodies = [celestial_bodies[i] for i in sorted_indices]
sorted_totals = [total_missions[i] for i in sorted_indices]

# Create a sorted bar chart
plt.figure(figsize=(12, 8))
plt.bar(sorted_bodies, sorted_totals, color='#FF5733', alpha=0.7)
plt.xlabel('Celestial Bodies')
plt.ylabel('Total Missions')
plt.title('Total Missions for Celestial Bodies Sorted in Ascending Order')
plt.show()