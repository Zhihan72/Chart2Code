import matplotlib.pyplot as plt

data = [
    [4.3, 4.5, 4.7, 4.6, 4.8, 4.4, 4.9, 4.6, 4.7, 4.5, 4.6],
    [6.7, 6.8, 6.9, 6.8, 6.7, 6.9, 7.0, 6.8, 6.9, 6.7, 7.1],
    [6.1, 6.3, 6.2, 6.5, 6.4, 6.5, 6.2, 6.6, 6.7, 6.8, 6.4],
    [5.8, 5.7, 5.9, 5.8, 5.9, 6.0, 5.6, 6.1, 5.9, 5.8, 6.0]
]

fig, ax = plt.subplots(figsize=(10, 6))

ax.boxplot(
    data, 
    patch_artist=False,
    notch=True, 
    vert=True
)

plt.show()