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
sns.kdeplot(y=tweets_ai, label='AI Tweets', color='blue', shade=True, alpha=0.6, ax=ax)
sns.kdeplot(y=tweets_blockchain, label='Blockchain Tweets', color='green', shade=True, alpha=0.6, ax=ax)

# Customizing the plot
ax.set_title('Density of Tweets Over Different Times of the Day\nDuring the Tech Conference 2022', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Time of Day (Hours)', fontsize=14)
ax.set_xlabel('Density of Tweets', fontsize=14)
ax.legend(title='Topics', fontsize=12, title_fontsize=14)
plt.yticks(np.arange(0, 25, step=1), labels=[f'{int(i)} AM' if i < 12 else ('Noon' if i == 12 else f'{int(i)-12} PM') for i in np.arange(0, 25, step=1)])
plt.grid(True)

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()