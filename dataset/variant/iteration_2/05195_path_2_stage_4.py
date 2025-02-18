import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
species_a = [50, 60, 70, 80, 85, 90, 95, 100, 110, 120, 130]
species_b = [30, 32, 34, 35, 38, 40, 45, 47, 50, 55, 58]
species_c = [20, 18, 15, 17, 16, 19, 22, 25, 27, 29, 30]

data = np.array([species_a, species_b, species_c])
new_colors = ['#ff6347', '#4682b4', '#3cb371']

fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, data, colors=new_colors, alpha=0.7)

plt.show()