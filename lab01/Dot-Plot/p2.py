from dotplot import dotplot, np, plt
import seaborn as sns
from matplotlib.lines import Line2D

sns.set_theme(style="ticks", font_scale=1.75)
plt.figure(figsize=(20, 8))
exam_scores = np.array([82,82,76,84,76,82,79,83,75,78,85,77,78,82,77,86,87,76,77,86,85,78,86,77,78,84,79,78,75,85,85,86,78,83,84,82,78,77,82,85])
dotplot(input_x=exam_scores, s=400, color='#0054A6')
axes = plt.gca()
axes.set_frame_on(False)
axes.axes.get_yaxis().set_visible(False)

xmin, xmax = axes.get_xlim()
ymin, ymax = axes.get_ylim()
xaxis_line = Line2D(
    (xmin, xmax), (ymin, ymin), linewidth=2, color='black'
)
axes.add_artist(xaxis_line)

score_range = range(exam_scores.min(), exam_scores.max()+1)
axes.set_xticks(score_range)
plt.xlabel('Final Exam Scores', labelpad=20)
plt.show()