import numpy as np
import matplotlib.pyplot as plt

def dotplot(input_x, **args):
    unique_values, counts = np.unique(input_x, return_counts=True)

    scatter_x = []
    scatter_y = []
    for idx, value in enumerate(unique_values):
        for counter in range(1, counts[idx]+1):
            scatter_x.append(value)
            scatter_y.append(counter)

    plt.scatter(scatter_x, scatter_y, **args)

    plt.gca().set_xticks(unique_values)
