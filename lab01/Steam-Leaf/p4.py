import numpy as np
def basic_stem_leaf(data):
    sorted_data = sorted(data)
    stems = [str(x)[:-1] for x in sorted_data]
    leaves = [str(x)[-1] for x in sorted_data]

    unique_stems = sorted(set(stems))
    for stem in unique_stems:
        print(f'{stem} | ', end="")
        for i, s in enumerate(stems):
            if s == stem:
                print(leaves[i], end="")
        print()

def stem_leaf_with_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = max(set(data), key=data.count)

    basic_stem_leaf(data)

    print("\nSummary Statistics:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

data = [23, 29, 20, 32, 27, 25, 28, 31, 24, 26, 22, 30, 15, 40]
stem_leaf_with_stats(data)