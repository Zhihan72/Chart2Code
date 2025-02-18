import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
genres = ['True Crime', 'Business', 'Technology', 'Health', 'Sports', 'Comedy', 'Fantasy']

true_crime = [5, 10, 15, 25, 35, 50, 60, 70, 85, 100]
business = [8, 12, 18, 22, 27, 35, 45, 55, 68, 80]
technology = [10, 15, 25, 30, 40, 52, 60, 75, 83, 95]
health = [6, 9, 14, 18, 27, 35, 40, 50, 65, 72]
sports = [4, 8, 12, 20, 28, 35, 42, 50, 60, 68]
comedy = [9, 14, 20, 26, 34, 40, 52, 60, 75, 88]
fantasy = [3, 8, 15, 23, 30, 38, 48, 55, 62, 70]

data = np.array([true_crime, business, technology, health, sports, comedy, fantasy])
bar_width = 0.1
x = np.arange(len(years))

single_color = '#4682B4'

fig, ax = plt.subplots(figsize=(14, 8))

for i in range(len(genres)):
    ax.bar(x + i * bar_width, data[i], bar_width, color=single_color, edgecolor='black')

ax.set_xticks(x + bar_width * (len(genres) - 1) / 2)

plt.tight_layout()
plt.show()