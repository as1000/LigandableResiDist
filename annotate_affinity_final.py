import pandas as pd
import numpy as np

df = pd.read_csv("/Users/ananthansadagopan/Downloads/merged_affinity_sheet.txt", sep="\t")
df['Symbol'] = df['Symbol'].replace(np.nan, "~")
df = df.fillna(method='ffill')
uq_types = list(set(df['Type'].tolist()))
df['Combined'] = df['Entry ID']+df['Ligand ID']
uq_types = sorted(list(set(df['Type'].tolist())))

df2 = pd.read_excel("/Users/ananthansadagopan/Downloads/merged_rcsb_calls_ffilled_filtered_distance_annotated_new.xlsx")
df2['Combined'] = df2['Entry ID'].astype(str)+df2['Ligand ID'].astype(str)

df2_combined_vals = df2['Combined'].tolist()

print(uq_types)
for a in uq_types:
    temp_df = df[df['Type']==a]
    print(temp_df)

    symbols = []
    min_val = []
    max_val = []
    units = []

    q=0
    for b in df2_combined_vals:
        q=q+1
        sub_df = temp_df[temp_df['Combined']==b]
        if len(sub_df.index.tolist())>0:
            symbols.append(sub_df['Symbol'].tolist()[0])
            min_val.append(min(sub_df['Value'].tolist()))
            max_val.append(max(sub_df['Value'].tolist()))
            units.append(sub_df['Unit'].tolist()[0])
        else:
            symbols.append(np.nan)
            min_val.append(np.nan)
            max_val.append(np.nan)
            units.append(np.nan)
        if q%100==0:
            print(q)
    
    df2[a+"_Symbol"] = symbols
    df2[a+"_MinValue"] = min_val
    df2[a+"_MaxValue"] = max_val
    df2[a+"_Unit"] = units

    print(a)

df2.to_excel("/Users/ananthansadagopan/Downloads/merged_rcsb_calls_ffilled_filtered_distance_annotated_affinity_annotation.xlsx", index=False)