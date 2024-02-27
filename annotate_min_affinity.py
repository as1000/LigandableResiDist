import pandas as pd
import numpy as np
import math

df = pd.read_excel("merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation.xlsx")
val1 = df['EC50_MinValue'].tolist()
val2 = df['IC50_MinValue'].tolist()
val3 = df['Kd_MinValue'].tolist()
val4 = df['Ki_MinValue'].tolist()

ec50_symbol = df['EC50_MinValueSymbol'].tolist()
ic50_symbol = df['IC50_MinValueSymbol'].tolist()
kd_symbol = df['Kd_MinValueSymbol'].tolist()
ki_symbol = df['Ki_MinValueSymbol'].tolist()

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

df.to_excel("merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation_min_value.xlsx", index=False)
