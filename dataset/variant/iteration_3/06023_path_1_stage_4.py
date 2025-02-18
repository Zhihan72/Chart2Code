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
sns.kdeplot(y=tweets_ai, color='purple', shade=True, alpha=0.7, linestyle="--", ax=ax)
sns.kdeplot(y=tweets_blockchain, color='red', shade=True, alpha=0.5, linestyle="-.", ax=ax)

# Changing legend and grid
ax.legend(["AI Tweets", "Blockchain Tweets"], loc='upper left', fontsize=10, frameon=True)
plt.grid(False, linestyle=':', linewidth=0.5)

# Enhancing borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_linestyle(':')
ax.spines['left'].set_linewidth(1.5)

plt.tight_layout()

# Display the plot
plt.show()