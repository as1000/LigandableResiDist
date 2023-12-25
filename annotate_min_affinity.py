import pandas as pd
import numpy as np
import math

df = pd.read_excel("/Users/ananthansadagopan/Downloads/merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation.xlsx")
val1 = df['EC50_MinValue'].tolist()
val2 = df['IC50_MinValue'].tolist()
val3 = df['Kd_MinValue'].tolist()
val4 = df['Ki_MinValue'].tolist()

ec50_symbol = df['EC50_Symbol'].tolist()
ic50_symbol = df['IC50_Symbol'].tolist()
kd_symbol = df['Kd_Symbol'].tolist()
ki_symbol = df['Ki_Symbol'].tolist()

min_val_list = []
type_list = []
symbol_list = []

q=0
while q<len(val1):
    temp_list = [val1[q], val2[q], val3[q], val4[q]]
    if temp_list != temp_list:
        min_val_list.append(np.nan)
        symbol_list.append(np.nan)
        type_list.append(np.nan)
        q=q+1
    else:
        temp_list = [1000000000000000000000000000 if math.isnan(x) else x for x in temp_list]
        min_val = min(temp_list)
        min_val_list.append(min_val)
        if min_val == val1[q]:
            symbol_list.append(ec50_symbol[q])
            type_list.append('EC50')
        elif min_val == val2[q]:
            symbol_list.append(ic50_symbol[q])
            type_list.append('IC50')
        elif min_val == val3[q]:
            symbol_list.append(kd_symbol[q])
            type_list.append('Kd')
        elif min_val == val4[q]:
            symbol_list.append(ki_symbol[q])
            type_list.append('Ki')
        else:
            symbol_list.append(np.nan)
            type_list.append(np.nan)
        q=q+1

df['MinValue'] = min_val_list
df['MinValue_Type'] = type_list
df['MinValue_Symbol'] = symbol_list

"""
df = pd.read_excel("/Users/ananthansadagopan/Downloads/idmapping_2023_11_17.xlsx")
pdbID = df['From'].tolist()
uniprot = df['Entry'].tolist()
entryname = df['Entry Name'].tolist()
protname = df['Protein names'].tolist()
gene_names = df['Gene Names'].tolist()
org = df['Organism'].tolist()
brenda = df['BRENDA'].tolist()
func = df['Function [CC]'].tolist()

uniprot_dict = dict(zip(pdbID, uniprot))
entryname_dict = dict(zip(pdbID, entryname))
protname_dict = dict(zip(pdbID, protname))
gene_names_dict = dict(zip(pdbID, gene_names))
org_dict = dict(zip(pdbID, org))
brenda_dict = dict(zip(pdbID, brenda))
func_dict = dict(zip(pdbID, func))

df2 = pd.read_excel("/Users/ananthansadagopan/Downloads/merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation_min_value.xlsx")
pdbID_values = df2['Entry ID'].tolist()

final_uniprot = []
final_entryname = []
final_protname = []
final_gene_names = []
final_org = []
final_brenda = []
final_func = []

q=0
while q<len(pdbID_values):
    try:
        final_uniprot.append(uniprot_dict[pdbID_values[q]])
        final_entryname.append(entryname_dict[pdbID_values[q]])
        final_protname.append(protname_dict[pdbID_values[q]])
        final_gene_names.append(gene_names_dict[pdbID_values[q]])
        final_org.append(org_dict[pdbID_values[q]])
        final_brenda.append(brenda_dict[pdbID_values[q]])
        final_func.append(func_dict[pdbID_values[q]])
    except:
        final_uniprot.append(np.nan)
        final_entryname.append(np.nan)
        final_protname.append(np.nan)
        final_gene_names.append(np.nan)
        final_org.append(np.nan)
        final_brenda.append(np.nan)
        final_func.append(np.nan)
    q=q+1

df2['Uniprot_ID'] = final_uniprot
df2['Uniprot_Entry_Name'] = final_entryname
df2['Uniprot_Protein_Name'] = final_protname
df2['Uniprot_Gene_Names'] = final_gene_names
df2['Uniprot_Organism'] = final_org
df2['Uniprot_BRENDA'] = final_brenda
df2['Uniprot_Function'] = final_func

df2.to_excel("/Users/ananthansadagopan/Downloads/merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation_min_value_uniprot.xlsx", index=False)
"""