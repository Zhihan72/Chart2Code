import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data for plotting
time_of_day = np.linspace(0, 24, 100)

tweets_ai = np.piecewise(time_of_day,
                         [time_of_day < 6, (time_of_day >= 6) & (time_of_day < 12), (time_of_day >= 12) & (time_of_day < 18), time_of_day >= 18],
                         [lambda x: 10 + 2*x, lambda x: 25 - 1.5*x, lambda x: 5 + 2.5*x, lambda x: 30 - x])

tweets_blockchain = np.piecewise(time_of_day,
                                 [time_of_day < 6, (time_of_day >= 6) & (time_of_day < 12), (time_of_day >= 12) & (time_of_day < 18), time_of_day >= 18],
                                 [lambda x: 8 + 1.5*x, lambda x: 20 - x, lambda x: 4 + 1.8*x, lambda x: 22 - 0.8*x])

tweets_cryptocurrency = np.piecewise(time_of_day,
                                     [time_of_day < 6, (time_of_day >= 6) & (time_of_day < 12), (time_of_day >= 12) & (time_of_day < 18), time_of_day >= 18],
                                     [lambda x: 15 + 1.8*x, lambda x: 30 - 0.5*x, lambda x: 10 + x, lambda x: 24 - 0.6*x])

tweets_climate = np.piecewise(time_of_day,
                              [time_of_day < 6, (time_of_day >= 6) & (time_of_day < 12), (time_of_day >= 12) & (time_of_day < 18), time_of_day >= 18],
                              [lambda x: 12 + 2*x, lambda x: 22 - x, lambda x: 8 + 1.2*x, lambda x: 26 - 0.7*x])

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

sns.kdeplot(tweets_ai, color='blue', shade=True, alpha=0.6, ax=ax, label='AI')
sns.kdeplot(tweets_blockchain, color='green', shade=True, alpha=0.6, ax=ax, label='Blockchain')
sns.kdeplot(tweets_cryptocurrency, color='red', shade=True, alpha=0.6, ax=ax, label='Cryptocurrency')
sns.kdeplot(tweets_climate, color='purple', shade=True, alpha=0.6, ax=ax, label='Climate')

# Customize text
ax.set_title('Tweet Density by Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hour', fontsize=14)
ax.set_ylabel('Density', fontsize=14)
plt.xticks(np.arange(0, 25, step=1), labels=[f'{int(i)} AM' if i < 12 else ('Noon' if i == 12 else f'{int(i)-12} PM') for i in np.arange(0, 25, step=1)])
ax.legend()

plt.tight_layout()
plt.show()