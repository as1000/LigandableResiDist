import pandas as pd
import numpy as np
import os
import re

working_dir = "/path/to/working_dir/"
final_df = pd.read_excel(working_dir + "merged_rcsb_calls_ffilled_filtered.xlsx")

all_pdbs = final_df['Entry ID'].tolist()
all_ligands = final_df['Ligand ID'].tolist()

tyr_dist = []
cys_dist = []
met_dist = []
lys_dist = []

q=0
while q<len(all_pdbs):
    temp_file = working_dir + "min_distance_from_" + str(all_pdbs[q]) + "_to_" + str(all_ligands[q]) + ".csv"

    try:
        df = pd.read_csv(temp_file)
    except:
        tyr_dist.append(float("nan"))
        cys_dist.append(float("nan"))
        met_dist.append(float("nan"))
        lys_dist.append(float("nan"))
        q=q+1
        continue

    tyr_df = df[df['Residue_Type']=="TYR"]
    cys_df = df[df['Residue_Type']=="CYS"]
    met_df = df[df['Residue_Type']=="MET"]
    lys_df = df[df['Residue_Type']=="LYS"]

    if len(tyr_df.index.tolist()) == 0:
        tyr_dist.append(float("nan"))
    else:
        tyr_dist.append(min(tyr_df['Min_Distance_from_Reactive_Atom_to_Ligand'].tolist()))
    
    if len(cys_df.index.tolist()) == 0:
        cys_dist.append(float("nan"))
    else:
        cys_dist.append(min(cys_df['Min_Distance_from_Reactive_Atom_to_Ligand'].tolist()))
    
    if len(met_df.index.tolist()) == 0:
        met_dist.append(float("nan"))
    else:
        met_dist.append(min(met_df['Min_Distance_from_Reactive_Atom_to_Ligand'].tolist()))

    if len(lys_df.index.tolist()) == 0:
        lys_dist.append(float("nan"))
    else:
        lys_dist.append(min(lys_df['Min_Distance_from_Reactive_Atom_to_Ligand'].tolist()))

    if q % 10 == 0:
        print(q)
    q=q+1

final_df['min_distance_from_ligand_to_lys_NZ'] = lys_dist
final_df['min_distance_from_ligand_to_tyr_OH'] = tyr_dist
final_df['min_distance_from_ligand_to_met_SD'] = met_dist
final_df['min_distance_from_ligand_to_cys_SG'] = cys_dist

final_df.to_excel(working_dir + "merged_rcsb_calls_ffilled_filtered_distance_annotated.xlsx", index=False)
