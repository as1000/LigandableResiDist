import pandas as pd
import numpy as np
import scipy.stats
import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.ticker as mtick
from matplotlib import ticker
import seaborn as sns
from matplotlib.colors import ListedColormap
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import statistics
from statsmodels.stats.proportion import proportions_ztest

plt.rcParams["font.family"] = "Arial"
sns.set(rc={'figure.figsize':(5,5)})
sns.set(font_scale=1.3)
plt.rcParams.update({'font.size': 12})

def split_advanced(strng, sep, pos):
    strng = strng.split(sep)
    return sep.join(strng[:pos]), sep.join(strng[pos:])

working_dir = "/path/to/working_dir/"

df = pd.read_excel(working_dir + "merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx")
#df = df[df['Enzyme_Class']!="No_Annotation"]
lys_dist = [x for x in df['min_distance_from_ligand_to_lys_NZ'].tolist() if x == x]
cys_dist = [x for x in df['min_distance_from_ligand_to_cys_SG'].tolist() if x == x]

vals_to_iterate = [lys_dist, cys_dist]
labels = ['Straight Line Distance to Lysine NZ (Å)', 'Straight Line Distance to Cysteine SG (Å)']
colors = ['blue', 'red']

for a, label, color in zip(vals_to_iterate, labels, colors):
    fig = plt.figure()
    ax = plt.gca()
    sorted_data = np.sort(a)
    yvals = np.arange(len(sorted_data))
    #yvals = np.arange(len(sorted_data)) / float(len(sorted_data))
    plt.plot(sorted_data, yvals, label=label, color=color)
    plt.xlabel(label)
    #plt.ylabel('Cumulative Probability')
    plt.ylabel('Number of Proteins')

    ax.set_facecolor("white")
    ax.grid(False)
    ax.tick_params(axis='x', which='major', bottom=True, labelsize=13, size=4)
    ax.tick_params(axis='y', which='major', left=True, labelsize=13, size=4)
    #ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    #ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1])

    ax.spines['bottom'].set_color('0')
    ax.spines['left'].set_color('0')

    fig.tight_layout()
    dpi_set = 300
    plt.tick_params(bottom='on', left='on')

    fig.savefig(working_dir + "combined_low_and_high_affinity_SLDnoCDF_%s.pdf" % (label.split(" ")[-3]), dpi=dpi_set)
