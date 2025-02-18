import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Constructing contextual data
time_of_day = np.linspace(0, 24, 100)
tweets_ai = np.piecewise(time_of_day,
                         [time_of_day < 6, (time_of_day >= 6) & (time_of_day < 12), (time_of_day >= 12) & (time_of_day < 18), time_of_day >= 18],
                         [lambda x: 10 + 2*x, lambda x: 25 - 1.5*x, lambda x: 5 + 2.5*x, lambda x: 30 - x])
tweets_blockchain = np.piecewise(time_of_day,
                                 [time_of_day < 6, (time_of_day >= 6) & (time_of_day < 12), (time_of_day >= 12) & (time_of_day < 18), time_of_day >= 18],
                                 [lambda x: 8 + 1.5*x, lambda x: 20 - x, lambda x: 4 + 1.8*x, lambda x: 22 - 0.8*x])

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Horizontal density plots for tweets
sns.kdeplot(y=tweets_ai, color='green', shade=True, alpha=0.6, ax=ax)  # Changed color to 'green'
sns.kdeplot(y=tweets_blockchain, color='blue', shade=True, alpha=0.6, ax=ax)  # Changed color to 'blue'

# Removing textual elements as directed
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_xticks([])
ax.legend().set_visible(False)

plt.grid(True)

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()