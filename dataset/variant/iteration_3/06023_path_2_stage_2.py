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

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))
sns.kdeplot(tweets_ai, color='blue', shade=True, alpha=0.6, ax=ax)
sns.kdeplot(tweets_blockchain, color='green', shade=True, alpha=0.6, ax=ax)

# Customize text
ax.set_title('Tweet Density by Time', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hour', fontsize=14)
ax.set_ylabel('Density', fontsize=14)
plt.xticks(np.arange(0, 25, step=1), labels=[f'{int(i)} AM' if i < 12 else ('Noon' if i == 12 else f'{int(i)-12} PM') for i in np.arange(0, 25, step=1)])

plt.tight_layout()
plt.show()