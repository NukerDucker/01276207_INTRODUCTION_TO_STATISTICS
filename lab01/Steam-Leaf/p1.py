def student_heights_stem_leaf(heights):
    sorted_heights = sorted(heights)

    stems = [str(x)[:-1] for x in sorted_heights]
    leaves = [str(x)[-1] for x in sorted_heights]

    unique_stems = sorted(set(stems))
    for stem in unique_stems:
        print(f'{stem} | ', end="")
        for i, s in enumerate(stems):
            if s == stem:
                print(leaves[i], end="")
        print()

heights = [158, 162, 165, 170, 171, 173, 175, 176, 178, 180, 182, 185]
print("Student Heights (cm) Stem-Leaf Plot:")
student_heights_stem_leaf(heights)