import matplotlib.pyplot as plt
import squarify

sizes = [7800, 4000, 3500000, 1200, 800000, 3000, 600, 200000, 15000, 1500, 500000, 100, 250, 100000, 1200]

new_colors = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', 
              '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', 
              '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000']

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, color=new_colors, alpha=0.8, pad=3)

# Adding title and axis labels with randomly altered text
plt.title("Arbitrary Treemap Title")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

plt.show()