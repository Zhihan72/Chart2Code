import matplotlib.pyplot as plt

# Assume hypothetical data
data = [range(10), range(10, 20), range(20, 30)]
# Original colors: ['red', 'blue', 'green']
# Shuffled colors: ['blue', 'green', 'red']
colors = ['blue', 'green', 'red']

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plotting the data with shuffled colors
for idx, d in enumerate(data):
    ax.plot(d, color=colors[idx])

# Display the plot
plt.show()