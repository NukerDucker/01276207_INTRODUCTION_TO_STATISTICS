import numpy as np

def stem_leaf_with_outliers(data):
    q1, q3 = np.percentile(data, [25,75])
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    sorted_data = sorted(data)

    stems = [str(x)[:-1] for x in sorted_data]
    leaves = [str(x)[-1] for x in sorted_data]

    unique_stems = sorted(set(stems))
    for stem in unique_stems:
        print(f'{stem} | ', end="")
        for i, s in enumerate(stems):
            if s == stem:
                if lower_bound <= sorted_data[i] <= upper_bound:
                    print(leaves[i], end="")
                else:
                    print(f"{leaves[i]}*", end="")
        print()

data = [23, 29, 20, 32, 27, 25, 28, 31, 24, 26, 22, 30, 15, 40]
stem_leaf_with_outliers(data)