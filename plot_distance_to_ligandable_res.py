
import pandas as pd 
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors
import matplotlib.patches as mpatches
import collections
import scipy
from matplotlib.ticker import StrMethodFormatter, NullFormatter, ScalarFormatter, FormatStrFormatter
from matplotlib.ticker import PercentFormatter
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.gridspec as gridspec

plt.rcParams["font.family"] = "Arial"
sns.set(rc={'figure.figsize':(6, 3)})
sns.set(font_scale=1)
dpi_set = 1200

df = pd.read_excel("/Users/ananthansadagopan/Documents/ChoudharyLab/PTMs/merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx")

vals = ['min_distance_from_ligand_to_lys_NZ', 'min_distance_from_ligand_to_tyr_OH', 'min_distance_from_ligand_to_met_SD', 'min_distance_from_ligand_to_cys_SG', 'min_distance_from_ligand_to_ligandable_atom']

bins_list = np.arange(0, 20, 0.4)
for a in vals:
    #temp_df = df[df[a]!="Unknown"]
    temp_df = df.dropna(subset=[a])
    ratio_list = [float(x) for x in temp_df[a].tolist()]
    fig, ax = plt.subplots(1, 1)
    ax.hist(ratio_list, density=False, bins=bins_list, color="black", linewidth=0.5, edgecolor="none")
    ax.set_facecolor("white")
    ax.grid(False)
    ax.tick_params(axis='x', which='major', bottom=True, labelsize=14, size=4)
    ax.tick_params(axis='y', which='major', left=True, labelsize=14, size=4)

    ax.spines['bottom'].set_color('0')
    ax.spines['left'].set_color('0')

    ax.set_ylabel("Number of Complexes", fontsize=14, labelpad=10)

    if a == "min_distance_from_ligand_to_lys_NZ":
        ax.set_xlabel('Minimum Distance to Lysine NZ (Å)', fontsize=14, labelpad=10)
    elif a == "min_distance_from_ligand_to_tyr_OH":
        ax.set_xlabel('Minimum Distance to Tyrosine OH (Å)', fontsize=14, labelpad=10)
    elif a == "min_distance_from_ligand_to_met_SD":
        ax.set_xlabel('Minimum Distance to Methionine SD (Å)', fontsize=14, labelpad=10)
    elif a == "min_distance_from_ligand_to_cys_SG":
        ax.set_xlabel('Minimum Distance to Cysteine SG (Å)', fontsize=14, labelpad=10)
    elif a == "min_distance_from_ligand_to_ligandable_atom":
        ax.set_xlabel('Minimum Distance to Ligandable Atom (Å)', fontsize=14, labelpad=10)

    ax.set_xlim([-0.1, 20.1])
    fig.savefig("/Users/ananthansadagopan/Downloads/" + a + "_histogram_PDB_database.pdf", dpi=dpi_set, bbox_inches = 'tight')
