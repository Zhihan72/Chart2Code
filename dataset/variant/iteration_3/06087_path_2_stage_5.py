import matplotlib.pyplot as plt

data = [range(10), range(10, 20), range(20, 30)]
colors = ['blue', 'green', 'red']

fig, ax = plt.subplots(figsize=(8, 6))

for idx, d in enumerate(data):
    ax.plot(d, color=colors[idx])

plt.show()