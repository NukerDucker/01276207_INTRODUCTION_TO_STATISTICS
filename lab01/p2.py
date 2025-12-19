import random

def temperature_stem_leaf(temperatures):
    sorted_temps = sorted(temperatures)

    stems = [str(x)[:-1] for x in sorted_temps]
    leaves = [str(x)[-1] for x in sorted_temps]

    unique_stems = sorted(set(stems))
    for stem in unique_stems:
        print(f'{stem} | ', end="")
        for i, s in enumerate(stems):
            if s == stem:
                print(leaves[i], end="")
        print()

temperatures = [random.randint(15, 35) for _ in range(30)]
print("Daily Temperature Readings (°C) Stem-Leaf Plot:")
temperature_stem_leaf(temperatures)