import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
df = housing.frame

print("Dataset Head:")
print(df.head())
print("-" * 30)

df['MedInc'].hist(bins=30)

plt.title('Histogram of Median Income (MedInc)')
plt.xlabel('Median Income values')
plt.ylabel('Frequency')

plt.show()