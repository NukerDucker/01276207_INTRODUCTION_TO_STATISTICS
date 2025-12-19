from dotplot import dotplot, np, plt

hs_heights = np.array([71,67,64,72,65,69,66,68,69,72,69,73,69,72,73,74,76,68,66,63,67,71,72,74,68,69,75,71,72,72,65,66,72,74,66,62,75,75,64,63,64,66,74,67,72,70,71,70,74,68])
dotplot(input_x=hs_heights)
plt.show()

dotplot(input_x=hs_heights, marker='*', color='#C44E52', s=100)
plt.xlabel("Height (Inches)", fontsize=14, labelpad=15)
plt.ylabel("Number of Players", fontsize=14, labelpad=15)
plt.title("High School Basketball Players", fontsize=14, pad=15)

plt.show()