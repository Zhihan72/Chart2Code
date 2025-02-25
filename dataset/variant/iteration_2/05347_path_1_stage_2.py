import matplotlib.pyplot as plt
import numpy as np

pets = ["Dogs", "Cats", "Rabbits", "Fish", "Birds", "Reptiles", "Hamsters"]
popularity = [45, 30, 5, 7, 6, 4, 3]
colors = ['#66b3ff', '#ff9999', '#ffb3e6', '#c2c2f0', '#99ff99', '#ff6666', '#ffcc99']
explode = (0.05, 0.05, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 10))

ax.pie(popularity, explode=explode, colors=colors, startangle=140, wedgeprops=dict(edgecolor='w', linewidth=2))

plt.show()