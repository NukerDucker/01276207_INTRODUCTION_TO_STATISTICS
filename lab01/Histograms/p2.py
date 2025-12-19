import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(1000)

sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red')

plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Customized Histogram with Density Plot')

plt.show()